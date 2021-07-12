# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 22:49:39 2021

@author: sly
"""

import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


list1=[]
scrappedReviews_pie =pd.read_csv("scrappedReviews.csv")
global pickle_model
file = open("pickle_model.pkl", 'rb') 
pickle_model = pickle.load(file)

global vocab
file = open("feature.pkl", 'rb') 
vocab = pickle.load(file)

#checks whether a review is '1' == positive or '0' == negative
for x in scrappedReviews_pie['reviews']:
            transformer = TfidfTransformer()
            loaded_vec = CountVectorizer(decode_error="replace",vocabulary=vocab)
            vectorised_review = transformer.fit_transform(loaded_vec.fit_transform([x]))
            list1.append(pickle_model.predict(vectorised_review))   
            list1.append(pickle_model.predict(vectorised_review))
        
#dividing list 1 into list2 and list3        
list2= []
list3= []
for i in range(len(list1)):
    if list1[i]==1:
        list2.append("positive")
    else:
        list3.append("negative")

len(list1) #15382        
len(list2) #13746 --> 89.36%
len(list3) #1636 --> 10.64 %
        
#list2 == all positive reviews 
#list3 == all negative reviews