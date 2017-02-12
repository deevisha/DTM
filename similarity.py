from __future__ import division
import string
import math

tokenize = lambda doc: doc.lower().split(" ")

document_0=open("asianage.txt", 'r').read()
document_1=open("deccan.txt", 'r').read()
document_2=open("deccanchronicle.txt", 'r').read()
document_3=open("dailypioneer.txt", 'r').read()
document_4=open("economictimes.txt", 'r').read()
document_5=open("hindustantimes.txt", 'r').read()
document_6=open("mint.txt", 'r').read()
document_7=open("newindianexpress.txt", 'r').read()
document_8=open("telegraph.txt", 'r').read()
document_9=open("tribuneindia.txt", 'r').read()
document_10=open("timesofindia.txt", 'r').read()
document_11=open("query.txt", 'r').read()

all_documents = [document_0, document_1, document_2, document_3, document_4, document_5, document_6, document_7, document_8, document_9,document_10, document_11]

dict={0: "asianage",
	  1: "deccan",
	  2: "deccanchronicle",
	  3: "dailypioneer",
	  4: "economictimes",
	  5: "hindustantimes",
	  6: "mint",
	  7: "newindianexpress",
	  8: "telegraph",
	  9: "tribuneindia",
	  10: "timesofindia"
}

def term_frequency(term, tokenized_document):
    return tokenized_document.count(term)

#the contribution of term frequency to document relevance is essentially a sub-linear function
# hence the log to approximate this sub-linear function

def sublinear_term_frequency(term, tokenized_document):
    count = tokenized_document.count(term)
    if count == 0:
        return 0
    return 1 + math.log(count)

def inverse_document_frequencies(tokenized_documents):
    idf_values = {}
    all_tokens_set = set([item for sublist in tokenized_documents for item in sublist])
    for tkn in all_tokens_set:
        contains_token = map(lambda doc: tkn in doc, tokenized_documents)
        idf_values[tkn] = 1 + math.log(len(tokenized_documents)/(sum(contains_token)))
    return idf_values

def tfidf(documents):
    tokenized_documents = [tokenize(d) for d in documents]
    idf = inverse_document_frequencies(tokenized_documents)
    tfidf_documents = []
    for document in tokenized_documents:
        doc_tfidf = []
        for term in idf.keys():
            tf = sublinear_term_frequency(term, document)
            doc_tfidf.append(tf * idf[term])
        tfidf_documents.append(doc_tfidf)
    return tfidf_documents

from sklearn.feature_extraction.text import TfidfVectorizer

sklearn_tfidf = TfidfVectorizer(norm='l2',min_df=0, use_idf=True, smooth_idf=False, sublinear_tf=True, tokenizer=tokenize)
sklearn_representation = sklearn_tfidf.fit_transform(all_documents)

def cosine_similarity(vector1, vector2):
    dot_product = sum(p*q for p,q in zip(vector1, vector2))
    magnitude = math.sqrt(sum([val**2 for val in vector1])) * math.sqrt(sum([val**2 for val in vector2]))
    if not magnitude:
        return 0
    return dot_product/magnitude


tfidf_representation = tfidf(all_documents)
cosine_tfidf_comparisons = []

for count_0, doc_0 in enumerate(tfidf_representation):
    if count_0==11:
		for count_1, doc_1 in enumerate(tfidf_representation):
			if count_1!=11:
				cosine_tfidf_comparisons.append((cosine_similarity(doc_0, doc_1), count_0, count_1))

skl_tfidf_comparisons = []

for count_0, doc_0 in enumerate(sklearn_representation.toarray()):
    if count_0==11:
	    for count_1, doc_1 in enumerate(sklearn_representation.toarray()):
			if count_1!=11:
				skl_tfidf_comparisons.append((cosine_similarity(doc_0, doc_1), count_0, count_1))

cosine_ranking=sorted(cosine_tfidf_comparisons, reverse=True)
skl_ranking=sorted(skl_tfidf_comparisons, reverse=True)

for x in zip(cosine_ranking, skl_ranking):
    print x

	
f=open("ranking.txt","w")
for element in cosine_ranking[0:5]:
	doc_number=element[2]
	f.write(dict[doc_number]+"\n")
f.close()