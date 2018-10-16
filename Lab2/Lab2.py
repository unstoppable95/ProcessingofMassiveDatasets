import math
from decimal import Decimal
from itertools import combinations



def main():
    n =  10000#liczb osob
    prob = 0.1 #prawdopodobienstwo przenocowania w hotelu
    numHotels= 100 #liczba hoteli
    numDays = 100 #liczba dni

    prob1 = prob*prob*(1/numHotels)
    prob2 = prob1**2

    cEstimated=(n**2/2)*(numDays**2/2)*prob2

    print(prob1,prob2,cEstimated)



    comb=combinations(range(n),2)
    print(list(comb))


if __name__=="__main__":
    main()