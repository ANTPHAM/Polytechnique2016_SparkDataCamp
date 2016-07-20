import re
import nltk.data 
from nltk.stem.porter import *
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

def terms(doc):
	Terms=[]
	sentences=sent_tokenize(doc.decode("utf-8")) # break the document into sentences could be useful for further extensions
	for sentence in sentences :
		Terms.extend(sentence_terms(sentence.lower())) # add the terms found per sentence
	return Terms
#returns the terms found in one sentence
def sentence_terms(sentence) :
	#sentence=str(sentence.encode("utf-8"))
	stop_words=stopwords.words('english') # get a list of default stopwords
	sentence=re.sub('[?!\\.]+','',sentence).strip() #remove punctuation from sentence because we don't need it anymore
	sentence=re.sub('\s+',' ',sentence)	# remove multiple spaces
	stemmer = PorterStemmer()
	# split the sentence into words
	#if the word is not in the list of stopwords apply stemming on it
	#and then add it to the list. If aterm appears twice then it will be added twice
	terms=[stemmer.stem(w) for w in sentence.split(" ") if w not in stop_words] 
	return terms
	