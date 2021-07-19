from util import *

# Add your import statements here




class Evaluation():


	def precision(self, doc_IDs_ordered, query_id, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at at given value of k

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""
		lis = []
		for quer in qrels:
			id_q = int(quer['query_num'])
			if query_id == id_q:
				lis.append(int(quer['id']))
		precision = -1
		count = 0
		#Fill in code here
		d = doc_IDs_ordered[0]
		for docID in d[:k]:
			if(docID in lis):
				count = count+1
		precision = count / k
		return precision


	def recall(self, doc_IDs_ordered, query_id, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at at given value of k

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1
		lis = []
		for quer in qrels:
			id_q = int(quer['query_num'])
			if query_id == id_q:
				lis.append(int(quer['id']))
		
		
		#Fill in code here
		count = 0
		d = doc_IDs_ordered[0]
		for docID in d[:k]:
			if(docID in lis):
				count = count+1
		if(len(lis) != 0):
			recall = count / len(lis)
		return recall


	def fscore(self, doc_IDs_ordered, query_id, qrels, k):
		"""
		Computation of f-score of the Information Retrieval System
		at a given value of k

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary

		Returns
		-------
		float
			The f-score value as a number between 0 and 1
		"""

		fscore = -1
		lis = []
		for quer in qrels:
			id_q = int(quer['query_num'])
			if query_id == id_q:
				lis.append(int(quer['id']))
		
		#Fill in code here
		count = 0
		d = doc_IDs_ordered[0]
		for docID in d[:k]:
			if(docID in lis):
				count = count+1
		recall = count / len(lis)
		precision = count / k
		if((precision + recall)==0):
			fscore = 0
		else:
			fscore = (2*precision*recall)/(precision+recall)


		return fscore

	def AveragePrecision(self, query_doc_IDs_ordered, query_id, qrels, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""
		lis = []
		for quer in qrels:
			id_q = int(quer['query_num'])
			if query_id == id_q:
				lis.append(int(quer['id']))
		precision = -1
		count = 0
		#Fill in code here
		sum = 0
		ct = 0
		for kk in range(1,k+1):
			d = query_doc_IDs_ordered[0]
			for docID in d[:kk]:
				ct = ct + 1
				if(docID in lis):
					count = count+1
			precision = count / kk
			sum = sum + precision
		return sum/ct





