import json
import pickle as pkl 
path = 'train.jsonl'
js = json.load(open(path, 'r'))
responses = js['responses']

def parseQuestionsAndChoices(ques):

    idx = 0
    optionChoices = ['A','B','C','D','a','b','c','d']
    choices = ""
    qu = ""
    while(idx<len(ques)-2):
        ch1 = ques[idx]
        ch2 = ques[idx+1]
        ch3 = ques[idx+2]

        if(ch1 == '(' and ch2 in optionChoices and ch3==')'):
            temp = idx + 3
            choice = ""
            while(temp<len(ques) and ques[temp]!='('):
                choice += ques[temp]
                temp += 1
            
            idx = temp
            choices += choice
            choices += '/'
        else:
            qu += ques[idx]
            idx += 1
    
    return qu, choices[:-1]



data = {}

for idx, val in enumerate(responses):
    question = val['question']
    answers = val['controllerAnswers']
    ques = question['questionText']
    answer = question['answerText']
    choices = ""
    # # if len(answers) is 4 or len(answers) is 3:
    #     for elem in answers:
    #         choices += elem['selectionText']
    #         choices += '/'

    #     choices = choices[:-1]
    #     cnt2 += 1
    # else:
    #     cnt += 1
    #     print "-=-==-=-=-=-=-=-=-=-=-=-Manual Parsing-==--=-=-=-=-=-=-=-=-=-=-=-=-="
    ques, choices = parseQuestionsAndChoices(ques)
    data[question['id']] = ques + '+' + choices + '+' + answer

pkl.dump(data, open(path+'_FORMATTED.pkl', 'w'))

