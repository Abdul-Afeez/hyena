from app.tools.parser import Parser

parser = Parser({
   "url":"https://techcabal.com/",
   "h1":[
      [
         "h1",
         "class",
         "single-article-title",
         "0"
      ],
      "text"
   ],
   "date":[
      [
         "span",
         "class",
         "single-article-date",
         "0"
      ],
      "text"
   ],
   "date_engine":[
      "_january_01_1970"
   ],
   "description":[
      [
         "meta",
         "property",
         "og:description",
         "0"
      ],
      "content"
   ],
   "main_content":[
      [
         "main",
         "",
         "",
         1
      ],
      "contents"
   ],
   "terminator":"Share this article",
   "unwanted_blocks":[
      [
         [
            "div",
            "class",
            "single-article-category",
            "0"
         ],
         "tag",
         True
      ],
      [
         [
            "div",
            "class",
            "list-newsletter-form shortcode",
            "0"
         ],
         "tag",
         True
      ]
   ],
"bad_signatures": [[["div", "class", "single-article-category", "0"], "text", "newsletters"]],"image_source": "TechCabal"
})
data = parser.extract('', '''
<!doctype html>
<html lang="en-US" class="no-js">
<head>
   <meta name="description" content="Here’s a list of 22 things that happened for the first time in the African tech scene in 2022" />
	<meta property="og:title" content="22 things that happened for the first time in 2022 in the African tech scene | TechCabal" />
	<meta property="og:description" content="Here’s a list of 22 things that happened for the first time in the African tech scene in 2022" />
</head>
<body>
    <div class="main-content">
        <main>
    <div class="content">
        <article>
            <div class="single-article-meta">
                <div class="single-article-category">
                    <a href="https://techcabal.com/category/african-tech-roundup/">African Tech Roundup</a>
                </div>
                <h1 class="single-article-title">22 things that happened for the first time in 2022 in the African tech scene</h1>
                <div class="single-article-info">
                    <span class="single-article-author">By
                                                        <a href="https://techcabal.com/author/daniel/" title="Posts by Daniel Adeyemi" rel="author">Daniel Adeyemi</a>                                                </span>
                    <span class="single-article-date">Dec 30, 2022</span>
                </div>
                                       
            <div class="single-article-main">
                <div class="single-article-content" id="single-article">                    
<div id="list-newsletter-form" class="list-newsletter-form shortcode">
    <h2>Get the best African tech newsletters in your inbox</h2>
</div>      
        </section>
</main>
</div>
</body>
</html>

''')
print(data)