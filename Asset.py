#Asset Depreciation

class Asset:


    def __init__(self,c=0.0,s=0.0,l=0):
        self.setCost(c)
        self.setSalVal(s)
        self.setLife(l)
        self._error = ""
        if self.isValid():
            self.buildAsset()

    def setCost(self,c):
        self._cost = c
    def getCost(self):
        return self._cost

    def setSalVal(self, s):
        self._salVal = s
    def getSalVal(self):
        return self._salVal

    def setLife(self, t):
        self._life = t
    def getLife(self):
        return self._life

    def isValid(self):
        valid = True
        if self._cost <= 0:
            self._error = "Cost must be positive."
            valid = False
        elif self._salVal < 0:
            self._error = "Salvage cannot be negative"
            valid = False
        elif self._salVal > self._cost:
            self._error = "Salvage cannot be more than cost"
            valid = False
        elif self._life <=0:
            self._error = "Life must be positive"
            valid = False
        return valid

    def getError(self):
        return self._error

    def getRate(self):
        rate = 1/(self._life)
        return rate

    def getDDRate(self):
        ddrate = (1/(self._life)) * 2
        return ddrate

    def buildAsset(self):

        #build arrays the size of life
        self._bbal = [0] * self._life
        self._dep = [0] * self._life
        self._ebal = [0] * self._life
        self._bbal[0] = self._cost

        #build arrays for double dep size of life
        self._ddbbal = [0] * self._life
        self._dddep = [0] * self._life
        self._ddebal = [0] * self._life
        self._ddbbal[0] = self._cost
        
        self._sdep = self.getStraight()
        ddrate = self.getDDRate()

        for i in range(0, self._life):
            if i>0: #this is fine
                self._bbal[i] = self._ebal[i-1]
                self._ddbbal[i] = self._ddebal[i-1]
            #mapped out double schedule but not sent to Dep yet
            #this is for reference
            self._dddep[i] = self._ddbbal[i] * ddrate
            self._ddebal[i] = self._ddbbal[i] - self._dddep[i]
            
           

            if(self._dddep[i] < self._sdep):
                self._dep[i] = self._sdep
            else:
                self._dep[i] = self._bbal[i] * ddrate
                     
            self._ebal[i] = self._bbal[i] - self._dep[i]
            
            if(self._ebal[i] < self._salVal):
                self._ebal[i] = self._salVal
                self._dep[i] = self._bbal[i] - self._salVal
      

    def getAnDep(self, yr):
        return self._dep[yr-1]
        
    def getBegBal(self, yr):
        return self._bbal[yr-1]

    def getEndBal(self, yr):
        return self._ebal[yr-1]

    def getStraight(self):
        straight = (self._cost - self._salVal) / self._life
        return straight

   

    
