from flask import Flask, request, jsonify
from goose import Goose
from newspaper import Article


app = Flask(__name__)
app.debug = True


@app.route('/api')

def articleExtractor():
    articleObject = []
    url = request.args.get('url','')
    phrasesBlackList = ["Image copyright AFP", "Image copyright Reuters Image caption", "Getty Images Image caption", "AFP Image caption","Image caption"]

    
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    
    
    articleObject.append(article.title)
    
    #clean up article body from unwanted phrase, then add it
    rawArticleText = article.text[:]
    for blackListedPhrase in phrasesBlackList:
        rawArticleText = rawArticleText.replace(blackListedPhrase,'')
    articleObject.append(rawArticleText)

    articleObject.append(article.authors)
    articleObject.append(article.top_image)
    
    #clean up summary from unwanted phrase, then add it
    rawSummaryText = article.summary
    for blackListedPhrase in phrasesBlackList:
        rawSummaryText = rawSummaryText.replace(blackListedPhrase,'')
    articleObject.append(rawSummaryText)
    
    
    return jsonify(articleText=articleObject[1], articleTitle=articleObject[0], articleAuthors=articleObject[2], articleTopImage=articleObject[3], articleNLPSummary=articleObject[4])
    #return jsonify(articleObject)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
