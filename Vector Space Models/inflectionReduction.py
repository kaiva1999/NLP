from util import *

# Add your import statements here




class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""
		nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
		reducedText = []
		for word_list in text:
		    c= []
		    for token in word_list:
		        c.append(" ".join([w.lemma_ for w in nlp(token)]))
		    reducedText.append(c)
		#Fill in code here
		
		return reducedText


