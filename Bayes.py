# -*- coding:UTF-8 -*-

import numpy as np
from sklearn.naive_bayes import MultinomialNB
# X = np.random.randint(5, size=(6, 100))
# y = np.array([1, 2, 3, 4, 5, 6])

class RSP():
    def __init__(self):
        self.clf = MultinomialNB()
        self.traind=False


    def train(self,human,ai):
        if len(ai)<100 or len(human)!=len(ai):
            return
        y=np.array(ai[2:])
        x=[]
        # sliding window
        wind_len=2
        for i in range(len(human)-wind_len):
            temp=human[i:(i+wind_len)].copy() + ai[i:(i+wind_len)].copy()
            x.append(temp)
        X=np.array(x)
        self.clf.fit(X,y)
        self.traind=True

    def predict(self,input):
        return self.clf.predict(np.array(input))


if __name__ =='__main__':
    human = [0, 0, 0, 2, 0, 1, 2, 0, 2, 1, 0, 0, 0, 2, 0, 2, 2, 1, 0,
             2, 2, 0, 0, 1, 1, 0, 0, 2, 2, 1, 1, 0, 2, 2, 1, 0, 1, 1,
             2, 2, 1, 1, 0, 0, 2, 2, 1, 1, 0, 2, 0, 0, 0, 1, 0, 2, 2,
             2, 2, 1, 1, 0, 1, 2, 0, 2, 1, 2, 0, 1, 0, 2, 1, 1, 2, 0,
             2, 1, 0, 2, 1, 0, 1, 2, 0, 2, 1, 0, 2, 1, 0, 0, 0, 1, 2,
             2, 1, 2, 0, 1]
    ai = [0, 1, 1, 1, 2, 2, 1, 1, 2, 2, 0, 0, 1, 1, 0, 2, 1, 2, 0, 1,
          2, 2, 2, 0, 2, 0, 0, 1, 0, 2, 2, 1, 1, 0, 2, 1, 0, 0, 2, 1,
          1, 2, 0, 1, 1, 0, 0, 1, 1, 1, 2, 2, 0, 1, 0, 2, 2, 2, 0, 0,
          1, 1, 0, 2, 2, 2, 1, 0, 1, 2, 0, 0, 2, 1, 2, 1, 2, 2, 1, 0,
          2, 1, 0, 0, 2, 2, 2, 1, 0, 2, 1, 0, 1, 1, 0, 2, 2, 1, 1, 2]

    a = RSP()
    a.train(human, ai)

    s = [0, 0, 2, 2]
    h = a.predict([s])
    print((h[0] + 1) % 3)
    i=0
    # play 100 times
    while i<100:
        b = input()
        c = input()
        s[0], s[1], s[2], s[3] = s[1], int(b), s[3], int(c)
        h = a.predict([s])
        print((h[0] + 1) % 3)

"""
    human2 = [0, 0, 0, 1, 0, 2, 2, 2, 2, 1, 1, 0, 1, 2, 0, 2, 1, 2, 0, 1, 0, 2, 1, 1, 2, 0, 2, 1, 0, 2, 1, 0, 1, 2, 0,
              2, 1, 0, 2, 1, 0, 0, 0, 1, 2, 2, 1, 2, 0, 1]
    ai2 = [2, 2, 0, 1, 0, 2, 2, 2, 0, 0, 1, 1, 0, 2, 2, 2, 1, 0, 1, 2, 0, 0, 2, 1, 2, 1, 2, 2, 1, 0, 2, 1, 0, 0, 2, 2,
           2, 1, 0, 2, 1, 0, 1, 1, 0, 2, 2, 1, 1, 2]

    print(human+human2)
    print(ai+ai2)

    w=0
    l=0
    t=0
    for i in range(50):
        if human2[i]==ai2[i]:
            t+=1
        elif (human2[i]+1)%3==ai2[i]:
            l+=1
        else:
            w+=1
    print(w+17,l+19,t+14,w+l+t)


if __name__ =='':
    human=[0,0,0,2,0,1,2,0,2,1,0,0,0,2,0,2,2,1,0,2,2,0,0,1,1,0,0,2,2,1,1,0,2,2,1,0,1,1,2,2,1,1,0,0,2,2,1,1,0,2]
    ai = [0,1,1,1,2,2,1,1,2,2,0,0,1,1,0,2,1,2,0,1,2,2,2,0,2,0,0,1,0,2,2,1,1,0,2,1,0,0,2,1,1,2,0,1,1,0,0,1,1,1]
    f = open('css.txt', 'r')
    result = list()
    h=[]
    human2=[]
    ai2=[]
    '''
    
    for line in open('css.txt'):
        line = f.readline()
        for x in line:
            if x=='R':h.append(0)
            elif x=='S':h.append(2)
            elif x=='P':h.append(1)
    for i in range(len(h)):
        if i%2==0: human2.append(h[i])
        else: ai2.append(h[i])

    print(len(human2),len(ai2))
    print(human2,ai2)
    '''
    human2=[0, 0, 0, 1, 0, 2, 2, 2, 2, 1, 1, 0, 1, 2, 0, 2, 1, 2, 0, 1, 0, 2, 1, 1, 2, 0, 2, 1, 0, 2, 1, 0, 1, 2, 0, 2, 1, 0, 2, 1, 0, 0, 0, 1, 2, 2, 1, 2, 0, 1]
    ai2 = [2, 2, 0, 1, 0, 2, 2, 2, 0, 0, 1, 1, 0, 2, 2, 2, 1, 0, 1, 2, 0, 0, 2, 1, 2, 1, 2, 2, 1, 0, 2, 1, 0, 0, 2, 2, 2, 1, 0, 2, 1, 0, 1, 1, 0, 2, 2, 1, 1, 2]

    a=RSP()
    a.train(human+human2,ai+ai2)

    s=[0,0,2,2]
    h = a.predict([s])
    print((h[0] + 1) % 3)
    while 1:
        b=input()
        c=input()
        s[0],s[1],s[2],s[3]=s[1],int(b),s[3],int(c)
        h=a.predict([s])
        print((h[0]+1)%3)
"""