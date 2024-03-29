import math

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk



# nltk.download('stopwords')
# nltk.download('punkt')

class Tokenizer:
    points = {
        'h1': 4,
        'h2': 3,
        'h3': 2,
        'h4': 1,
        'h5': 1,
        'h6': 1,
        'p': 1,
        'li': 1,
        'div': 1
    }
    def __init__(self):
        from app.tools.printer import Printer
        self.printer = Printer
    def tokenize(self, block):
        # tokens = word_tokenize(block)
        tokens = block.split(' ')
        # convert to lower case
        tokens = [w.lower() for w in tokens]
        # remove punctuation from each word
        import string
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens]
        # remove remaining tokens that are not alphabetic
        words = [word for word in stripped if word.isalpha()]
        # filter out stop words
        sw_nltk = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
        # self.printer.basic_print(sw_nltk)
        tokens = [word for word in words if word not in sw_nltk]
        return tokens


class JITIndexer(Tokenizer):

    def __init__(self, article):
        super().__init__()
        self.score = 0
        self.article = article

    def scorer(self):
        for tag, block in self.article.items():
            self.score += len(self.tokenize(block)) * self.points.get(tag, 0)
        self.printer.basic_print(f'Current / New article score:  {self.score}')
        return self.score


class ComparativeScorer(Tokenizer):

    def __init__(self, index, document):
        super().__init__()
        if 'str' in str(type(document)):
            merged_document = document
        elif 'dict' in str(type(document)):
            merged_document = ''
            for tag, block in document.items():
                merged_document += f'{merged_document} {block}'
        else:
            merged_document = ''
        self.index = index
        self.jit_score = JITIndexer(document).scorer()
        self.tokenized_document = list(set(self.tokenize(merged_document)))
        self.printer.basic_print('About to compare')

    def scorer(self):
        self.printer.basic_print('Comparing')
        shards = []
        shards_log = []
        missing = 0
        Index = self.index
        for token in self.tokenized_document:
            existing_token = Index.get_or_none(Index.token == token)
            if existing_token:
                shards_log.append({token: existing_token.shard})
                shards.append(existing_token.shard)
            else:
                missing += 1
        comparative_scores = {}
        # self.printer.basic_print(shards_log)
        for shard in shards:
            for job_id, indices in shard.items():
                if not comparative_scores.get(job_id, None):
                    comparative_scores[job_id] = 0
                for tag, frequency in indices.items():
                    comparative_scores[job_id] += self.points.get(tag, 0) * frequency
        self.printer.basic_print(comparative_scores)
        # past_scores = {}
        cannibalism = []
        from app.models.base import Job
        for job_id, comparative_score in comparative_scores.items():
            job = Job.get(Job.id == job_id)
            if ((comparative_score/(int(job.jit_score) or 1))*100) >= 45 and ((comparative_score/(int(self.jit_score) or 1))*100) >= 45:
                cannibalism.append({'job_id': job_id, 'url': job.reference_url, 'jit_score': job.jit_score, 'comparative_score': comparative_score, 'new_article_jit_score': self.jit_score })
            if len(cannibalism) > 5:
                break

        self.printer.print(f'''
        System Output: 
        cannibalism: {cannibalism}
''')
        return cannibalism, self.jit_score, shards_log


class Indexer(Tokenizer):

    def __init__(self, article_id, index, article):
        super().__init__()
        self.index = index
        self.article_id = str(article_id)
        self.article = article
        self.tokenized_document = None

    def bulk_tokenize(self):
        for tag, document in self.article.items():
            self.add_index(tag, document)

    def bulk_remove_index(self):
        for tag, document in self.article.items():
            self.remove_index(document)

    def remove_index(self, block):
        tokens = self.tokenize(block)
        processed_tokens = {}
        for token in tokens:
            Index = self.index
            existing_token = Index.get_or_none(Index.token == token)
            if not processed_tokens.get(token, None) and existing_token and existing_token.shard.get(self.article_id,
                                                                                                     None):
                del existing_token.shard[self.article_id]
                processed_tokens[token] = True
                self.printer.basic_print(existing_token.shard)
                existing_token.shard = existing_token.shard
                existing_token.total = len(existing_token.shard.keys())
                if existing_token.total:
                    existing_token.save()
                else:
                    existing_token.delete().execute()

    def add_index(self, tag, block):
        tokens = self.tokenize(block)
        processed_tokens = {}
        for token in tokens:
            Index = self.index
            existing_token = Index.get_or_none(Index.token == token)
            # self.printer.basic_print('existing_token == ', existing_token)
            if not processed_tokens.get(token, None) and existing_token and existing_token.shard.get(self.article_id,
                                                                                                     {}).get(tag, None):
                del existing_token.shard[self.article_id][tag]
                processed_tokens[token] = True
                # self.printer.basic_print(existing_token.shard)
            elif not processed_tokens.get(token, None) and existing_token:
                processed_tokens[token] = True
            if existing_token:
                existing_shard = existing_token.shard
                if existing_token.shard.get(self.article_id, None):
                    article_index = existing_shard[self.article_id]
                    article_tag_frequency = article_index.get(tag, 0)
                    new_shard = {**existing_shard,
                                 self.article_id: {**article_index, tag: article_tag_frequency + 1}}
                else:
                    new_shard = {**existing_shard, self.article_id: {tag: 1}}
                existing_token.total = len(existing_token.shard.keys())
                existing_token.shard = new_shard
                existing_token.save()
            else:
                new_token = Index()
                new_token.token = token
                new_token.shard = {self.article_id: {tag: 1}}
                new_token.total = 1
                new_token.save()
                processed_tokens[token] = True
