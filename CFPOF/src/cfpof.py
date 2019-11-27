#-*- coding:Utf-8 -*-

__author__ = "under submission for cnria20"

import os
import time
import sys
import random


def trouver(tab,i,j,x):
    m=int((i+j)/2)
    if m==0 or (tab[m-1]<x and x<=tab[m]):
        return m
    if tab[m]<x:
        return trouver(tab,m+1,j,x)
    return trouver(tab,i,m,x)

def combin(n, k):
    """Nombre de combinaisons de n objets pris k a k"""
    if k>n or n==0: return 0 
    if k > n//2:
        k = n-k
    x = 1
    y = 1
    i = n-k+1
    while i <= n:
        x = (x*i)//y
        y += 1
        i += 1
    return x
 
 
benchmarks=["chess.num", "connect.num", "Organistion.num", "Person.num"] #   
    
if __name__ == "__main__":
    myArgs={}
    for myArg in sys.argv:
        myArg = myArg.split(":")
        myArgs[myArg[0]]=myArg[1]
    try:   
        if myArgs["dataset"] not in benchmarks:
            print("There is no database named",myArgs["dataset"],"in our benchmarks.")
            sys.exit(1)
    except KeyError:
        print("No given dataset.")
        sys.exit(1)
         
    dataset = "../Datasets/"+myArgs["dataset"]
    print("===========================BEGIN===========================\n===============Under submission for CNRIA'20===============\nCFPOF calculation ... \nDataset : ",myArgs["dataset"].split("/")[-1])
    beginTime1 =time.process_time()
    data, somWeight , supportSet= {}, [],{}
    tid=0
    m,M=1,3
    try:
        M= int(myArgs["maxLength"])
        print("\tMaximum length :",M)
    except KeyError:
        M=3
        print("\tNo given maximum length constraint.\n\t\tMaximum length :",M,"by default.")
    som=0
    Cnk={}
    with open(dataset, 'r') as base:
        line=base.readline()
        while line :#and tid<10000:
            itemset = line.replace("\n","").split(" ") #itemset[0] contient l'id de l'instance
            data[tid]=itemset
            X={}
            for item in itemset[1:]:
                try:
                    supportSet[item][tid]=tid
                except KeyError:
                    supportSet[item]={}
                    supportSet[item][tid]=tid
            size=len(itemset)-1
            maxLen=min([size,M])
            try:
                som+=Cnk[size][-1]
            except KeyError:
                Cnk[size]=[0]
                for k in range(1,maxLen+1):
                    Cnk[size].append(Cnk[size][k-1]+combin(maxLen, k))
                som+=Cnk[size][-1]
            somWeight.append(som)
            line=base.readline()
            tid+=1
    del base
    endTime1 = time.process_time() - beginTime1
    print("\tPreprocessing time (s) :",endTime1)
    sampleSize=1000
    try:
        sampleSize= int(myArgs["sampleSize"])
        print("\tSample size :",sampleSize)
    except KeyError:
        sampleSize=1000
        print("\tNo given sample size.\n\t\tSample size :",sampleSize,"by default.")
    beginTime =time.process_time()
    scores={}
    listSupp={}
    for k in range(sampleSize):
        alea=somWeight[-1]*random.random()
        indiceTrans = trouver(somWeight, 0, len(somWeight), alea)
        trans = data[indiceTrans]
        wTab = Cnk[len(trans)-1][1:]
        aleaPattern=wTab[-1]*random.random()
        nbItems = m+trouver(wTab, 0, len(wTab), aleaPattern)
        pattern = random.sample(trans[1:], k=nbItems)
        pattern.sort()
        try:
            supp=list(listSupp[str(pattern)])
        except KeyError:
            supp=list(supportSet[pattern[0]])
            for i in range(1, len(pattern)):
                X=[]
                if len(supp)<len(supportSet[pattern[i]]):
                    for tid in supp:
                        try:
                            X.append(supportSet[pattern[i]][tid])
                        except:
                            X
                else:
                    for tid in supportSet[pattern[i]]:
                        try:
                            X.append(supp[tid])
                        except:
                            X
                supp=list(X)
            listSupp[str(pattern)]=list(supp)  
        for tid in supp:
            try:
                scores[tid]+=1
            except KeyError:
                scores[tid]=1
    
    maxScore = max([v for (key, v) in scores.items()])
    for tid in scores:
        scores[tid] /= maxScore 
        """score contains the transaction cfpof identified by their tid"""
    endTime = time.process_time() - beginTime
    print("\tCFPOF computational time (s) :",endTime)
    print("============================END============================")
    try:
        printed=int(myArgs["printCFPOF"])
        if printed==1:
            print(scores)
    except KeyError:
        ok=""
        
        
