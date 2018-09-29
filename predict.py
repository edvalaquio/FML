import sys
import pandas as pd
import numpy as np
import pickle

from tensorflow.keras.preprocessing.text import Tokenizer
#from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
#from tensorflow.keras.layers import Activation, Dense, Dropout
#from sklearn.preprocessing import LabelEncoder
#import sklearn.datasets as skds
from pathlib import Path


# load our saved model
#model = load_model('FML_model.h5')
model = load_model('FML_model.h5')
# load tokenizer
tokenizer = Tokenizer()
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


def main():

	logFile = sys.argv[1]
	to_predict = Path(logFile).read_text()

	x_tokenized = tokenizer.texts_to_matrix([to_predict], mode='tfidf')

	prediction = model.predict(x_tokenized)

	#print(" ".join(str(x) for x in np.argsort(prediction)[0][:-5:-1]))
	#print(" ".join(str(y) for y in np.sort(prediction)[0][:-5:-1]))

	myDict = {}
	preds = np.argsort(prediction)[0][:-5:-1] 
	percents = np.sort(prediction)[0][:-5:-1]

	for i in range(0,4):
		myDict[str(preds[i])] = float(percents[i])
		 
	print(myDict)



if __name__ == "__main__":
	if len(sys.argv) == 2:
		main()
	exit()
