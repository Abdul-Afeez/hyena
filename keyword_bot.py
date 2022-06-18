# import spacy
# from collections import Counter
# from string import punctuation
#
# from thefuzz import process
# from thefuzz.fuzz import ratio
#
# nlp = spacy.load("en_core_web_sm")
#
#
# def get_hotwords(text):
#     result = []
#     pos_tag = ['PROPN', 'ADJ', 'NOUN', 'CCONJ', 'CONJ', 'ADJ', 'ADV']  # 1
#     doc = nlp(text.lower())  # 2
#     for token in doc:
#         # 3
#         if (token.text in nlp.Defaults.stop_words or token.text in punctuation):
#             continue
#         # 4
#         if (token.pos_ in pos_tag):
#             result.append(token.text)
#
#     return result  # 5
#
#
# def get_fuzzy_similarity(token=None, dictionary=None):
#     """Returns similar words and similarity scores for a given token
#     from a provided dictionary of words
#
#     Keyword Arguments:
#         token {str} -- the reference word (default: {None})
#         dictionary {list} -- the list of target words (default: {None})
#
#     Returns:
#         [list] -- a list of tuples in the form `(matched_word, similarity score)`
#     """
#
#     if token and dictionary:
#         return process.extractBests(token, dictionary, scorer= ratio, score_cutoff=0)
#     else:
#         return []
#
# def extract_keywords(nlp, sequence, special_tags: list = None):
#     """ Takes a Spacy core language model,
#     string sequence of text and optional
#     list of special tags as arguments.
#
#     If any of the words in the string are
#     in the list of special tags they are immediately
#     added to the result.
#
#     Arguments:
#         sequence {str} -- string sequence to have keywords extracted from
#
#     Keyword Arguments:
#         tags {list} --  list of tags to be automatically added (default: {None})
#
#     Returns:
#         {list} -- list of the unique keywords extracted from a string
#     """
#     result = []
#
#     # custom list of part of speech tags we are interested in
#     # we are interested in proper nouns, nouns, and adjectives
#     # edit this list of POS tags according to your needs.
#     pos_tag = ['PROPN','NOUN','ADJ']
#
#     # create a spacy doc object by calling the nlp object on the input sequence
#     doc = nlp(sequence.lower())
#
#     # if special tags are given and exist in the input sequence
#     # add them to results by default
#     if special_tags:
#         tags = [tag.lower() for tag in special_tags]
#         for token in doc:
#             if token.text in tags:
#                 result.append(token.text)
#
#     for chunk in doc.noun_chunks:
#         final_chunk = ""
#         for token in chunk:
#             if (token.pos_ in pos_tag):
#                 final_chunk = final_chunk + token.text + " "
#         if final_chunk:
#             result.append(final_chunk.strip())
#
#     for token in doc:
#         if (token.text in nlp.Defaults.stop_words or token.text in punctuation):
#             continue
#         if (token.pos_ in pos_tag):
#             result.append(token.text)
#     return list(set(result))
#
# # print(keywords)
# # print(get_fuzzy_similarity('Nigerian retail-tech startup', keywords))
# # print(get_fuzzy_similarity('TradeDepot raises $110m', keywords))
# # print(get_fuzzy_similarity('Series B funding round', keywords))
#
#
# # print(get_fuzzy_similarity('Nigerian retail-tech startup TradeDepot raises $110m Series B funding round', keywords))
#
# # output = get_hotwords('''applications have now opened for the latest edition, with successful applicants to receive 12 weeks of intensive online training, access to a world-class mentor, and US$5,000 in seed capital to prove the concept, plus access to further funding. They will also gain access to the TEF network of startups.''')
# # print(output)