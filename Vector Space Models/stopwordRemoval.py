from util import *

# Add your import statements here




class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		stopwordRemovedText = []
		stop_words = set(stopwords.words('english'))
		for word_list in text:
		    stopword_removed = [w for w in word_list if not w in stop_words]
		    stopwordRemovedText.append(stopword_removed)
		#Fill in code here

		return stopwordRemovedText




	