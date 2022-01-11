import numpy as np
import random as rd
import NPermutation
import ObjectiveResult as result

class Structure:
    def __init__(self,n,Ytxt,Nametxt):
        self.n = n
        self.Ytxt = Ytxt
        self.Nametxt = Nametxt
        f = open(Ytxt, "r")
        y = []
        for x in f:
            j = 0
            l = []
            for w in x.split():
                y.append(np.float(w))
        self.y = y
        self.k = int(len(y)/n)
        self.x = None
        self.xNames = None
        self.xY=None

    def ordinaryInitialization(self):
        x = np.zeros((self.n,self.k))
        r = 0
        s = 0
        for i in range(0,len(self.y)):
            if r == self.k:
                s = s + 1
                r = 0
            x[s,r] = i
            r = r + 1
        self.x = x
        self.__updateXNames()
        self.__updateXY()

    def randomInitialization(self):
        ry = rd.sample(range(len(self.y)),len(self.y))
        rx = np.zeros((self.n,self.k))
        r = 0
        s = 0
        for i in ry:
            if r == self.k:
                s = s + 1
                r = 0
            rx[s,r] = i
            r = r + 1
        self.x = rx
        self.__updateXNames()
        self.__updateXY()

    def print(self):
        print()
        print("n = " + str(self.n))
        print("k = " + str(self.k))
        print("Nº of permutation >= " + str(NPermutation.getNPermutation(self.n,self.k)))
        print("Ytxt: " + self.Ytxt)
        print("NameTxt: " + self.Nametxt)
        print("Y:")
        print(self.y)
        print("X:")
        print(self.x)
        print("XName: ")
        print(self.xNames)
        print("Xy: ")
        print(self.xY)
        print("Value: ")
        print(result.result(self.x,self.y))
        print()
    def updateX(self,x):
        self.x = x
        self.__updateXNames()
        self.__updateXY()
    def __updateXNames(self):
        f = open(self.Nametxt,"r")
        yN = []
        s = 0
        r = 0
        for x in f:
            for w in x.split():
                yN.append(w)
        xN = np.empty((self.n, self.k),dtype='object')
        for i in range(0,len(xN[:,0])):
            for j in range(0,len(xN[0,:])):
                xN[i,j] = yN[int(self.x[i,j])]
        self.xNames = xN
    def __updateXY(self):
        y = self.y
        x = self.x
        xy = np.zeros((self.n,self.k))
        for i in range(0, len(x[:, 0])):
            for j in range(0, len(x[0, :])):
                xy[i, j] = y[int(x[i, j])]
        self.xY = xy
    def getX(self):
        return self.x
    def getY(self):
        return self.y




