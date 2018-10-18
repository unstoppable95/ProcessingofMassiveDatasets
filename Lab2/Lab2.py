import math
from decimal import Decimal
from itertools import combinations
from random import *
from math import *


def main():
    n =  10000#liczb osob
    prob = 0.1 #prawdopodobienstwo przenocowania w hotelu
    numHotels= 100 #liczba hoteli
    numDays = 100 #liczba dni

    prob1 = prob*prob*(1/numHotels)
    prob2 = prob1**2

    cEstimated=int((n**2/2)*(numDays**2/2)*prob2)

    print("Spodziewane wartości ",cEstimated)

    dictMain = {}
    #make {dict[day]:{numhotel:{list of people}}}
    for i in range(1,numDays+1):
        dictMain[i]={}
        for j in range(1,n+1):
            isGo=choices([1,0],[0.1,0.9])
            if (isGo[0]==1):
                numHotel=randint(1,numHotels)
                if(numHotel not in dictMain[i]):
                    dictMain[i][numHotel]=[]
                    dictMain[i][numHotel].append(j)
                else:
                    dictMain[i][numHotel].append(j)


    #make combination pairs of people in dict[day][numHot]
    dictPom={}
    for day in dictMain:
        dictPom[day]={}
        for numHot in dictMain[day]:
            pairsComb=combinations(dictMain[day][numHot],2)
            dictPom[day][numHot]=list(pairsComb)


    #make pairs counter dict
    dictPairCount={}
    for day in dictPom:
        for numHot in dictPom[day]:
            for para in dictPom[day][numHot]:
                if (para not in dictPairCount):
                    dictPairCount[para]=1
                else:
                    dictPairCount[para]+=1

    numberOfPairsPeople=0
    numberOfPairsPeopleDays=0

    uniquePeople=[]
    dictHist={}
    for x in dictPairCount:
        if (dictPairCount[x] not in dictHist):
            dictHist[dictPairCount[x]] = 1
        else:
            dictHist[dictPairCount[x]] += 1
        if dictPairCount[x]>1:
            if (x[0] not in uniquePeople):
                uniquePeople.append(x[0])
            if(x[1] not in uniquePeople):
                uniquePeople.append(x[1])
            numberOfPairsPeople+=1
            #number of combinations pair's days
            numberOfPairsPeopleDays += (factorial(dictPairCount[x])/(factorial(2)*factorial(dictPairCount[x]-2)))

    numberOfPeople=len(uniquePeople)
    print("Liczba podejrzanych par: " ,numberOfPairsPeople)
    print("Liczba podejrzanych par ludzi i dni: " , int(numberOfPairsPeopleDays))
    print("Liczba podejrzanych ludzi: ", numberOfPeople)
    print("Histogram :")
    print(dictHist)
    #histogram postaci ilosc spotkan - os x ; liczba par o takiej ilosci - os y

if __name__=="__main__":
    main()