import os
import pickle as pkl

from data import DataReader

dirname = 'AI2-ScienceQuestions-V1-Feb2016/AI2-Elementary-NDMC-v1'
prefix = 'Elementary-NDMC-'

trainPath = os.path.join(dirname, prefix+'Train.jsonl')
testPath = os.path.join(dirname, prefix+'Test.jsonl')
devPath = os.path.join(dirname, prefix+'Dev.jsonl')

reader = DataReader(trainPath, testPath, devPath)

reader.createDataSet('Train')
reader.createDataSet('Dev')
reader.createDataSet('Test')