import os
import json
import pickle as pkl

class DataReader():

    def __init__(self, Train, Test, Dev):
        
        ''' Should be JSON files '''
        self.pathToTrain = Train
        self.pathToTest = Test
        self.pathToDev = Dev

    def createDataSet(self, flag):

        filepath = ""
        if flag is 'Train':
            filepath = self.pathToTrain
        elif flag is 'Dev':
            filepath = self.pathToDev
        else:
            filepath = self.pathToTrain
        
        fil = open(filepath, 'r')
        data = {}
        for line in fil:
            js = json.loads(line)
            key = js['id']
            question = js['question']['stem']
            if len(js['question']['choices']) is not 4:
                print "-----------!!!!!!!!!!!!!--------------"
                print js['question']['choices']
                print "-----------!!!!!!!!!!!!!--------------"
                continue
            answerChoiceA = js['question']['choices'][0]['text']
            answerChoiceB = js['question']['choices'][1]['text'] 
            answerChoiceC = js['question']['choices'][2]['text']
            answerChoiceD = js['question']['choices'][3]['text']
            correct = js['answerKey']
            
            # Format : QUESTIONTEXT+A/B/C/D+CORRECTANSWER
            # print "ID", key, " TEXT: ", question + '+' + answerChoiceA + '/' + answerChoiceB + '/' + answerChoiceC + '/' + answerChoiceD + '+' + correct
        
            data[key] = question + '+' + answerChoiceA + '/' + answerChoiceB + '/' + answerChoiceC + '/' + answerChoiceD + '+' + correct
        
        pkl.dump(data, open(filepath+'_FORMATTED.pkl', 'w'))
        print "Saving for ", flag, " at ", filepath+'_FORMATTED.pkl'
    

class TupleReader():

    def __init__(self, path):
        self.path = path
    
    def readTuples(self, delim):

        fil = open(self.path, 'r')
        tuples = []
        for line in fil:
            splits = line.split(delim)
            if len(splits) > 3:
                temp = []
                temp[0] = splits[0]
                temp[1] = splits[1]
                temp[2] = ""
                for idx in range(2,len(splits)):
                    temp[2] += splits[idx]
                splits = temp
            tuples.append(splits)
        
        pkl.dump(tuples, open(self.path+'_FORMATED.pkl', 'w'))
        print "Saving for ", self.path, " at ", self.path+'_FORMATED.pkl'
