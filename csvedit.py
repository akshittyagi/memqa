import os
import csv
import pickle as pkl
import random

data = []
count = 0
ques = {}

test = pkl.load(open('Elementary-NDMC-Test.jsonl_FORMATTED.pkl', 'r'))
qu = {}
for key, value in test.iteritems():
    parts = value.split('+')
    # print parts
    choices = parts[1].split('/')
    text = choices[ord(parts[-1]) - ord('A')]
    qu[parts[0]] = text
    # print parts[0]
    # print parts[-1]
    count += 1
print count
count = 0
print "Created data"


# test2 = pkl.load(open('newtest.pkl', 'r'))
# qu = {}
# for key, value in test.iteritems():
#     parts = value.split('+')
#     # print parts
#     qu[parts[0]] = parts[-1]
#     # print parts[0]
#     # print parts[-1]
#     count += 1
# print count
# count = 0
# print "Created data"

import random

cnt = 0

with open('4thgrade.csv') as fil:
    reader = csv.reader(fil, delimiter=',')
    for row in reader:
        data.append(row)

idx = 1
count = 1
newdata = []

cnt1 = 0
cnt2 = 0
cc = 0
newdata.append(data[0])
while (idx < len(data) - 4):
    row = data[idx]
    temp = row
    a = random.randint(0,100)
    if row[2] == 'A':
        cc += 1
    if count is not 0 and row[0] in qu:
        ques[row[0]] = qu[row[0]]
        # print row[0]
        # print qu[row[0]]          
        cnt = 0
        # print "CNT", cnt
        # print row[2], qu[row[0]]

        while(cnt<4):
            temp2 = data[idx+cnt]
            if a < 98:
                cnt1 += 1
                if data[idx+cnt][3] == qu[row[0]]:
                    temp2[4] = '1'
                else:
                    temp2[4] = '0'
            
            else:
                cnt2 += 1
                op = a % 4
                ans = chr(ord('A') + op)
                if data[idx+cnt][3] == ans:
                    temp2[4] = '1'
                else:
                    temp2[4] = '0'
            newdata.append(temp2)
            cnt += 1
        idx = idx + cnt
    else:
        newdata.append(temp)
    # print row[0]
    # print row[1]
    count += 1
    idx += 1
print cc
print cnt1, cnt2
with open('newnewgrade.csv', 'w') as newfil:
    writer = csv.writer(newfil, delimiter=',')
    for row in newdata:
        # print row
        writer.writerow(row)



