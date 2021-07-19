from util import *

# Add your import statements here




class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""
        
		segmentedText = re.compile('[.!?]').split(text)

		#Fill in code here

		return segmentedText





	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""
		punkt_param = PunktParameters()
		abbreviation = ['f', 'fr', 'k'] # depending on where sentence tokenizer is likely to split on abbrevations
		punkt_param.abbrev_types = set(abbreviation)
		tokenizer = PunktSentenceTokenizer(punkt_param)
		tokenizer.train(text)
		segmentedText = tokenizer.tokenize(text)
		return segmentedText