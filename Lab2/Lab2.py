from itertools import combinations
from random import *
from math import *
from collections import Counter

def makeSimulation(n,prob,numHotels,numDays):

    dictMain = {}
    #{dict[day]:{numhotel:[list of people]}}
    for i in range(1, numDays + 1):
        dictMain[i] = {}
        for j in range(1, n + 1):
            isGo = choices([1, 0], [prob, 1.0-prob])
            if (isGo[0] == 1):
                numHotel = randint(1, numHotels)
                if (numHotel not in dictMain[i]):
                    dictMain[i][numHotel] = []
                    dictMain[i][numHotel].append(j)
                else:
                    dictMain[i][numHotel].append(j)

    #make combination pairs of people in dict[day][numHot]
    dictPom = {}
    for day in dictMain:
        dictPom[day] = {}
        for numHot in dictMain[day]:
            pairsComb = combinations(dictMain[day][numHot], 2)
            dictPom[day][numHot] = list(pairsComb)

    #make pair's meeting counter ex.{(100,200}:8}
    dictPairCount = {}
    for day in dictPom:
        for numHot in dictPom[day]:
            for pair in dictPom[day][numHot]:
                if (pair not in dictPairCount):
                    dictPairCount[pair] = 1
                else:
                    dictPairCount[pair] += 1

    numberOfPairsPeople = 0
    numberOfPairsPeopleDays = 0
    uniquePeople = []
    dictHist = {}
    for x in dictPairCount:
        if (dictPairCount[x] not in dictHist):
            dictHist[dictPairCount[x]] = 1
        else:
            dictHist[dictPairCount[x]] += 1
        if dictPairCount[x] > 1:
            if (x[0] not in uniquePeople):
                uniquePeople.append(x[0])
            if (x[1] not in uniquePeople):
                uniquePeople.append(x[1])
            numberOfPairsPeople += 1
            numberOfPairsPeopleDays += (factorial(dictPairCount[x]) / (factorial(2)*factorial(dictPairCount[x]-2)))

    numberOfPeople = len(uniquePeople)
    return numberOfPairsPeople,numberOfPairsPeopleDays,numberOfPeople,dictHist

def main():
    sumNumPairs=0
    sumNumPairsDays=0
    sumNumPeople=0
    sumHist={}
    numIter=10
    for i in range (0,numIter):
        numPairs,numPairsDays,numPeople,hist=makeSimulation(10000,0.1,100,100)
        sumNumPairs +=numPairs
        sumNumPairsDays +=numPairsDays
        sumNumPeople +=numPeople
        dict1=Counter(hist)
        dict2=Counter(sumHist)
        sumHist=dict1+dict2

    #normalize results
    numPeople=int(sumNumPeople/numIter)
    numPairsDays=int(sumNumPairsDays/numIter)
    numPairs=int(sumNumPairs/numIter)
    Hist = {k: int(v/numIter) for k, v in sumHist.items()}
    print("Liczba symulacji: "+ str(numIter)+ '\n'+"Liczba podejrzanych par: " + str(numPairs) +'\n' + "Liczba podejrzanych par ludzi i dni: " + str(int(numPairsDays)) +'\n' +"Liczba podejrzanych ludzi: " + str(numPeople)+'\n'+"Histogram :" +'\n' +str(Hist))

if __name__=="__main__":
    main()