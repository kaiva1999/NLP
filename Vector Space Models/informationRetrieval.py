from util import *
import numpy as np
import math
# Add your import statements here




class InformationRetrieval():

	def __init__(self):
		self.index = None
	

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""

		index = {}

		#Fill in code here
		no_docs = len(docIDs)
		no_words = [0]*no_docs
		len_doc = len(docs)
		for i in range(len_doc):
			count = [len(sentence) for sentence in docs[i]]
			no_words[i] = sum(count)
			for sent in docs[i]:
					for token in sent:      # tokenisation 
						if token in index:
							val = index[token]
							if docIDs[i] in val:
								val[docIDs[i]] = val[docIDs[i]]+1
							else:
								val[docIDs[i]]=1
							index[token] = val
						else:
							val = {docIDs[i] : 1}
							index[token] = val

		n_words = len(index)
		f_index = {0:index,1:np.zeros((no_docs,n_words)),2:docIDs}
		index_1 = f_index[1]
		w_index = f_index[0]

		for i in range(len(docIDs)):
			for j in index:
				val = w_index[j]
				if docIDs[i] in val:
					count_word = val[docIDs[i]]
					tf = count_word/no_words[i]
					idf = math.log(no_docs/len(val),10)
					pos = list(w_index).index(j)
					
					index_1[i][pos] = tf*idf
		f_index[0] = w_index
		f_index[1] = index_1	

		self.index = f_index


	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list 
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		doc_IDs_ordered_all = []

		#Fill in code here
		w_index = self.index[0]
		index_1 = self.index[1]
		docIDs = self.index[2]
		no_docs = len(index_1)
		no_word = len(index_1.T)
		word_index = {}
		no_words = [0]*len(queries)
		no_queries = len(queries)

		for i in range(no_queries):
			count_query = [len(sent) for sent in queries[i]]
			no_words[i] = sum(count_query)
			for sent in queries[i]:
				for word in sent:
					if word in w_index:
						if i in word_index:
							cal = word_index[i]
							if word in cal:
								count = cal[word]+1 
								cal[word] = count
							else:
								cal[word] = 1
							word_index[i]= cal
						else:
							cal = {word : 1}
							word_index[i] = cal

		tf_idf = np.zeros((no_queries,len(w_index)))
		for i in range(len(queries)):
			query_word = word_index[i]
			for word in query_word:
				if word in w_index:
					pos = list(w_index).index(word)
					val = word_index[i]
					idf = math.log(no_docs/len(w_index[word]))
					tf = val[word]/no_words[i]
					tf_idf[i][pos] = tf*idf

		sum_val = np.matmul(tf_idf,index_1.T)
		doc_val = np.matmul(index_1,index_1.T)
		query_val = np.matmul(tf_idf,tf_idf.T)
		doc_square = np.sqrt(np.diagonal(doc_val))
		query_square = np.sqrt(np.diagonal(query_val))
		rank_values = {}
		doc_IDs_ordered_all= []
		for i in range(no_queries):
			doc_rank = {}
			for j in range(no_docs):
				denom = doc_square[j]*query_square[i]
				if denom == 0:
					denom = 1
				rank = sum_val[i][j]/denom
				if(rank != 0):
					doc_rank[docIDs[j]] = rank
			rank_v = sorted(doc_rank.items(),key = lambda x:x[1],reverse = True)
			x=[tup[0] for tup in rank_v]
			doc_IDs_ordered_all.append(x)
		return doc_IDs_ordered_all




