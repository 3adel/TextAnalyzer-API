# Adel Shehadeh, 2017
# Based on python-goose: https://github.com/grangier/python-goose

from goose import Goose

#a function

def article_extractor(url):
    
    articleObject = []
    
    print("Program started ...")
    
    articleExtractor = Goose()
    article = articleExtractor.extract(url=url)
    
    #build article content
    articleBody = ""
    for letter in article.cleaned_text:
        articleBody+=str(letter.encode('utf-8', 'ignore'))
    

    #save article content in a file
    f1=open('./output.txt', 'w+')
    f1.write(article.title + '\n')
    f1.write(article.meta_description + '\n')
    f1.write(articleBody)
    f1.close()
    
    articleObject.append(article.title)
    articleObject.append(article.meta_description)
    articleObject.append(articleBody)
    
    return articleObject


print(article_extractor('http://www.bbc.com/news/world-us-canada-41134799'))
