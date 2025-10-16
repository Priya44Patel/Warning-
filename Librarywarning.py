#
#Author: PRiYA
#Warning library
#
#



#A custom library (with classes, functions)
  
'''

def ratefunction(Rate):
    for i in range(len(Rate)):
        increase = Rate[i-1] - Rate[i]
        Rate = increase/Rate[i] * 100
        return Rate
print (ratefunction(Rate))

'''

def Ratefunction (Rate):
    
    return [100 * (b - a) / a for a, b in zip(Rate[::1], Rate[1::1])]

#print (Ratefunction(Rate))

def Averagerate(Rateofall):
    avg = sum(Rateofall)/len(Rateofall)
    return avg
'''
def increaseofthree(year):
    n = 202
    return 3 * year + n
'''
# obtained from google
#Ongoing global ecological change will continue to
#produce novel infectious agents at the current rate of three per year.

Rateofnewdiseaseeveryyear = 3

class Rate():

    def __init__(self, year, increase):#,decrease):
        self.year = year
        self.increase = (Rateofnewdiseaseeveryyear * year) + 202
        #self.decrease = (increase-1)
        
    def getyear(self):
        return self.year

    def setyear(self,year):
        self.year = year
    
    def increase(year):
       
        return increase
    
    #def decrease(increase):
        #pass

#to show inheritance
    '''
#assume loss of pathogens due to global warming or some reason would be 1 everyyear

class ratedecrease(Rate):
    def __init__(self, year, increase, decrease):
        Rate.__init__(self, year, increase)
        self.decrease = increase-1
    def decrease(increase):
        return decrease
        
    
year1 = Rate(2,2)
year2 = ratedecrease(2,2,2)
print(year1.increase)
print(year2.decrease)

'''
   
    
    
