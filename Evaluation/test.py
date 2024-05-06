import nltk 
import spacy 

nlp = spacy.load("en_core_web_sm") 


sentence = "It's difficult because I'll have to study hard and a lot, but I think that if you like a subject , you 'll study it easier."

print(list(nlp(sentence)))