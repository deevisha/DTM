from __future__ import division
import string
import math

tokenize = lambda doc: doc.lower().split(" ")


document_0=open("finaloutput_asianage1.txt", 'r').read()
document_1=open("finaloutput_dp1.txt", 'r').read()
document_2=open("finaloutput_deccan1.txt", 'r').read()
document_3=open("query.txt", 'r').read()

"""document_3=open("finaloutput_asianage.txt", 'r').read()
document_4=open("finaloutput_asianage.txt", 'r').read()
document_5=open("finaloutput_asianage.txt", 'r').read()
document_6=open("finaloutput_asianage.txt", 'r').read()
document_7=open("finaloutput_asianage.txt", 'r').read()
document_8=open("finaloutput_asianage.txt", 'r').read()
document_9=open("finaloutput_asianage.txt", 'r').read()
document_10=open("query.txt", 'r').read()"""

all_documents = [document_0, document_1, document_2, document_3]
""", document_4, document_5, document_6, document_7, document_8, document_9,document_10"""

def jaccard_similarity(query, document):
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection)/len(union)

def term_frequency(term, tokenized_document):
    return tokenized_document.count(term)
#the contribution of term frequency to document relevance is essentially a sub-linear function
# hence the log to approximate this sub-linear function
def sublinear_term_frequency(term, tokenized_document):
    count = tokenized_document.count(term)
    if count == 0:
        return 0
    return 1 + math.log(count)

def augmented_term_frequency(term, tokenized_document):
    max_count = max([term_frequency(t, tokenized_document) for t in tokenized_document])
    return (0.5 + ((0.5 * term_frequency(term, tokenized_document))/max_count))

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
our_tfidf_comparisons = []

for count_0, doc_0 in enumerate(tfidf_representation):
    if count_0==3:
		for count_1, doc_1 in enumerate(tfidf_representation):
			our_tfidf_comparisons.append((cosine_similarity(doc_0, doc_1), count_0, count_1))

skl_tfidf_comparisons = []

for count_0, doc_0 in enumerate(sklearn_representation.toarray()):
    if count_0==3:
	    for count_1, doc_1 in enumerate(sklearn_representation.toarray()):
			skl_tfidf_comparisons.append((cosine_similarity(doc_0, doc_1), count_0, count_1))

for x in zip(sorted(our_tfidf_comparisons, reverse = True), sorted(skl_tfidf_comparisons, reverse = True)):
    print x