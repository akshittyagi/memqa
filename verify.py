import json 
import pickle as pkl 


def verifyDataSetFile(path):
    
    data = pkl.load(open(path, 'r'))
    count = 0
    for key, value in data.iteritems():
        print key
        print value
        count += 1

    print count


if __name__=="__main__":
    verifyDataSetFile('train.jsonl_FORMATTED.pkl')