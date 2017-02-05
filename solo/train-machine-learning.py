#!/usr/bin/python
import xgboost as xgb
import pandas as pd

def train_model(filename):
    colnames = ['countryCount', 'cityCount', 'importCount', 'exportCount', 'keywordCount', 'iec', 'target']
    train = pd.read_csv(filename, header= None, names = colnames)
    print list(train)
    target = train['target']
    train = train.drop(['target'], axis = 1)
    xgtrain = xgb.DMatrix(train.values, target.values)

    # specify parameters via map, definition are same as c++ version
    param = {'max_depth':20, 'eta':0.1, 'silent':1, 'objective':'binary:logistic', 'early_stop_round': 3 }

    num_round = 5
    bst = xgb.train(param, xgtrain, num_round)
    bst.save_model('xgb.model')

if __name__ == '__main__':
    train_model('/home/ashish/codes/axis-bank/train.csv')