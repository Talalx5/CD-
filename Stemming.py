
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


stemmer = PorterStemmer()
content = """Cake is a form of sweet food made from flour, sugar, and other ingredients, that is usually baked.In their oldest forms, cakes were modifications of bread, but cakes now cover a wide range of preparations 
that can be simple or elaborate, and that share features with other desserts such as pastries, meringues, custards, and pies."""
tk_content=word_tokenize(content)
stemmed_words = [stemmer.stem(i) for i in tk_content] 


print(stemmed_words)