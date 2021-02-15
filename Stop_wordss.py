
#Step0: Creating a variable that holds stopswords from corpus
#step1: writting your Sentence
#step2: Tokenize with word_
#Step3: Filter out
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
#Step0:
my_stopwords= set(stopwords.words("english"))
#print(my_stopwords)
#Step1:
H= 'Electoral Commission has finalized the registration.'
#Step2:
j= word_tokenize(H)
#Step3:
Filtered=[]
for g in j: 
  if g not in my_stopwords:
    Filtered.append(g)
print("Tokenized",j)
print("Filtered words",Filtered)