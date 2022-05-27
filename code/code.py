#CS21BTECH11056
#this code gives result of probability for different values of p n and k

from cmath import sqrt
import math

def Probability(n,p,k):

    print((1/(2*math.pi*n*p*(1-p))**(0.5))*(math.exp((-1*(k-n*p)**2)/(2*n*p*(1-p)))))


Probability(1000,0.5,500)
Probability(1000,0.5,510)