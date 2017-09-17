from flask import Flask, request, jsonify
from goose import Goose
app = Flask(__name__)
app.debug = True

@app.route("/api")
def articleExtractor():
    
    url = request.args.get('url','')
    
    articleObject = []
    
    print("Program started ...")
    
    articleExtractor = Goose()
    article = articleExtractor.extract(url=url)
    
    #build article content
    articleBody = ""
    for letter in article.cleaned_text:
        articleBody+=str(letter.encode('utf-8', 'ignore'))
    

    articleObject.append(article.title)
    articleObject.append(article.meta_description)
    articleObject.append(articleBody)
    
    #return article main text
    return jsonify(articleObject)
if __name__ == "__main__":
    app.run(host="0.0.0.0")
