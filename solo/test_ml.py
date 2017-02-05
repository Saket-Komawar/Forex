#!/usr/bin/python
'''
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
from sklearn.cross_validation import  cross_val_score
import cPickle
import sys
'''

import os
import commands
def get_prediction(features, path):
	string = ''
	for key in features:
		string += str(key) + ' '
	try:
		# ret = os.system('Rscript ./solo/r-prediction.R ' + string + " | python ./solo/a.py")
		tup = ()
		tup = commands.getstatusoutput('Rscript ./solo/r-prediction.R ' + string + " | python ./solo/a.py")
		ret = tup[1]
		print "Saket" + str(ret)
		return ret
	except Exception as e:
		print e
		score = -1
		return score
	try:
		f = open('./solo/result.csv', 'r')
		score = float(f.read())
	except Exception as e:
		print e
		return 0
	return score
    

if __name__ == '__main__':
	get_prediction('/home/ashish/codes/axis-bank/demo.test', None)
