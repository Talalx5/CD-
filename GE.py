

import spacy

Comp = spacy.load('en_core_web_sm')
sentence = "he drinks a cup of tea"
doc = Comp(sentence)

for token in doc:
    ancestors = [t.text for t in token.ancestors] 
    children = [t.text for t in token.children]
    print(token.text, "\t", token.i, "\t", 
          token.pos_, "\t", token.dep_, "\t", 
          ancestors, "\t", children)