from flask import Flask, request, jsonify
from goose import Goose
from newspaper import Article


app = Flask(__name__)
app.debug = True


@app.route('/api')

def articleExtractor():
    articleObject = []
    url = request.args.get('url','')
    
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    
    
    articleObject.append(article.title)
    articleObject.append(article.text[:])
    articleObject.append(article.authors)
    articleObject.append(article.top_image)
    articleObject.append(article.summary)
    
    return jsonify(articleText=articleObject[1], articleTitle=articleObject[0], articleAuthors=articleObject[2], articleTopImage=articleObject[3], articleNLPSummary=articleObject[4])
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
