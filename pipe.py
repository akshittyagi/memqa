import os
import pickle as pkl

from data import DataReader

dirname = 'AI2-ScienceQuestions-V2.1-Jan2018'
prefix = 'ElementarySchool'

trainPath = os.path.join(dirname, prefix, 'Elementary-NDMC-'+'Train.jsonl')
testPath = os.path.join(dirname, prefix, 'Elementary-NDMC-'+'Test.jsonl')
devPath = os.path.join(dirname, prefix, 'Elementary-NDMC-'+'Dev.jsonl')

# reader = DataReader(trainPath, testPath, devPath)
reader = DataReader('/home/akshit/train.jsonl', testPath, devPath)
reader.createDataSet('Train')
reader.createDataSet('Dev')
reader.createDataSet('Test')