#Exercise 10.1 Feature Hasing and LSH

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
#from sklearn.model_selection import train_test_split #Depends on version of sklearn
from sklearn.cross_validation import train_test_split #Depends on version of sklearn
from sklearn.metrics import accuracy_score
import suitcase #own implementation of bags of words
from datetime import datetime


def RandForClassPred(bag_mat,topics_binary):
	#Split into train and test 80/20 
	X_train, X_test, y_train, y_test = train_test_split(bag_mat,topics_binary, test_size=0.2, random_state=123456)
	#Train RandomForest Classifier
	RF = RandomForestClassifier(n_estimators=50, oob_score = True, random_state=123456)
	RF.fit(X_train, y_train)

	pred = RF.predict(X_test) #Create predictions with the test set
	accuracy = accuracy_score(y_test,pred) # The Test Error

	print('Mean accuracy score: {:.3f}\nOut-of-bag error (training error): {:.3f}'.format(accuracy, RF.oob_score_))
	print('The input matrix is {} x {} '.format(len(bag_mat),len(bag_mat[0])))

if __name__ == '__main__':
	#Read in data
	raw_data = pd.read_json('merged.json')
	#Drop those rows that have NA in topics and body => 10377 rows left.
	data = raw_data.dropna(subset=['topics','body'])
	#The array we want to work with
	topics = data['topics'].values.tolist()
	datalines = data['body'].values.tolist()
	#Create output data e.g. [1,0,0,0,1....,1] if 'earn' in topics
	topics_binary = list(map(lambda x: 1 if 'earn' in x else 0,topics))

	#----- Regular bags of words, timing starts--------
	print('For the regular BOW:')
	t0 = datetime.now()
	#Create a bag of words. Input data
	bag_mat = suitcase.OwnBagWords(datalines)
	#All the operations of random forest done. 
	RandForClassPred(bag_mat,topics_binary)
	print('Time regular BOW: {}\n'.format(datetime.now()-t0))

	#----- Hashing the BOW, timing starts--------
	print('For BOW with hashing:')
	t2 = datetime.now()
	#Create a bag of words. Input data
	bag_mat_hash = suitcase.OwnBagWordsHashing(datalines,1000)
	#All the operations of random forest done. 
	RandForClassPred(bag_mat_hash,topics_binary)
	print('Time BOW with hashing: {}\n\nOverall Time: {}'.format(datetime.now()-t2,datetime.now()-t0))




