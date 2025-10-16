
#
#Final Project
#Author:PRiYA
#
#Iteration and decision making
#imports from your library and the standard library


import csv
print("*******************************************************************")
print("Restaurants in which state might require more frequent inspections.")
print("*******************************************************************")



with open('outbreaks.csv') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    columnnames = next(csvreader)                             
    print("We are going to deal with data about",columnnames)
 
    
    #Restaurants in which state might require more frequent inspections
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    
    for row in csvreader:
   
        '''
        if row[2] == 'California':
            row[3].find('Restaurant')
          '''
        if row[3] == 'Restaurant' and row[2] == 'California':
            c+=1
  
        if row[3] == 'Restaurant' and row[2] == 'Florida':
            d+=1
              
        if row[3] == 'Restaurant' and row[2] == 'Alabama':
            e+=1            
        if row[3] == 'Restaurant' and row[2] == 'Arizona':
            f+=1
        if row[3] == 'Restaurant' and row[2] == 'Alaska':
            g+=1            
        if row[3] == 'Restaurant' and row[2] == 'Colorado':
            h+=1
        if row[3] == 'Restaurant' and row[2] == 'Connecticut':
            i+=1

                #print (row)
    print(f"Restaurants in california:", c)
    print(f"Restaurants in Florida:", d)
    print(f"Restaurants in Alabama:", e)
    print(f"Restaurants in Arizona:", f)
    print(f"Restaurants in Alaska:", g)
    print(f"Restaurants in Colorado:", h)
    print(f"Restaurants in Connecticut:", i)
    
#this way we can find total number of restaurants in all states 
#we can also use fuzzywuzzy library for Approximate matching or substrings matching
#for example where there is restaurant as well as other places written in column
        
topstates = []
topstates.append(c)
topstates.append(d)
topstates.append(e)
topstates.append(f)
topstates.append(g)
topstates.append(h)
topstates.append(i)
topstates.sort(reverse=True)
print(topstates)

#thus states which has caused more outbreaks due to restaurant in data gets printed first
#thus we can find top states which need inspection in restaurants
#and we can also find states which are safer for dineins

#Top states in need to focus on immunization programs?
#we can find in same way as  above using illness data and states
#as where illness would be higher those will need to focus on immunization
print("****************************************************")
print("******Which Pathogen has caused the most chaos?*****")
print("****************************************************")
import collections

with open('outbreaks.csv') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    columnnames = next(csvreader)  

    count = collections.Counter()

   
    for row in csvreader:
        organism = row[6]
        count[organism] += 1

    #Display duplicate or unique organisms
    for organism, n in count.items():
        
        if n>1:
            print(organism," is  seen",n," times")
            
        else:
            
            print(organism," is  seen first  time")

           


'''
To calculate the Rate:
First: work out the difference (increase) between the two numbers you are comparing.
Increase = New Number - Original Number
Then:  divide the increase by the original number and multiply the answer by 100.
% increase = Increase ÷ Original Number × 100.
If your answer is a negative number then this is a percentage decrease.
Read more at: https://www.skillsyouneed.com/num/percent-change.html
'''
print("************************************************")
print("Rate at which illness changed from 1998 to 2015.")
print("************************************************")

import csv
from collections import deque

#import matplotlib #for saving graph as image
#matplotlib.use('Agg') #for saving graph as image
import matplotlib.pyplot as plt

with open('outbreaks.csv') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    columnnames = next(csvreader)                             
   
  
    
    firstyearill = 0 #1998
    secondyearill = 0 #1999
    thirdyearill = 0#2000
    fourthyearill = 0#2001
    fifthyearill = 0#2002
    sixthyearill = 0#2003
    seventhyearill = 0#2004
    eightyearill = 0#2005
    ninethyearill = 0#2006
    tenthyearill = 0#2007
    eleventhyearill = 0#2008
    twelvethyearill = 0#2009
    thirteenyearill = 0#2010
    fourteenyearill = 0#2011
    fifteenyearill = 0#2012
    sixteenyearill = 0#2013
    seventeenyearill = 0#2014
    eighteenyearill = 0#2015
    Rate = deque()
    #The use of a data structure as in unit 6
   
    for row in csvreader:
        if row[0] == '1998':
            firstyearill += int(row[9])
        
   
        if row[0] == '1999':
            secondyearill += int(row[9])
           

        if row[0] == '2000':
            thirdyearill += int(row[9])

   
        if row[0] == '2001':
            fourthyearill += int(row[9])

        if row[0] == '2002':
            fifthyearill += int(row[9])
   
        if row[0] == '2003':
            sixthyearill += int(row[9])
            
        if row[0] == '2004':
            seventhyearill += int(row[9])
        
   
        if row[0] == '2005':
            eightyearill += int(row[9])
           

        if row[0] == '2006':
            ninethyearill += int(row[9])

   
        if row[0] == '2007':
            tenthyearill += int(row[9])

        if row[0] == '2008':
            eleventhyearill += int(row[9])
   
        if row[0] == '2009':
            twelvethyearill += int(row[9])

                   
        if row[0] == '2010':
            thirteenyearill += int(row[9])
        
   
        if row[0] == '2011':
            fourteenyearill += int(row[9])
           

        if row[0] == '2012':
            fifteenyearill += int(row[9])

   
        if row[0] == '2013':
            sixteenyearill += int(row[9])

        if row[0] == '2014':
            seventeenyearill += int(row[9])
   
        if row[0] == '2015':
            eighteenyearill += int(row[9])

   




      
   
    print("Total Illness in 1998 were:", firstyearill)#1998
    print("Total Illness in 1999 were:",secondyearill) #1999
    print("Total Illness in 2000 were:",thirdyearill) #2000
    print("Total Illness in 2001 were:", fourthyearill)#2001
    print("Total Illness in 2002 were:", fifthyearill)#2002
    print("Total Illness in 2003 were:", sixthyearill)#2003
    print("Total Illness in 2004 were:", seventhyearill)#2004
    print("Total Illness in 2005 were:",eightyearill)#2005
    print("Total Illness in 2006 were:",ninethyearill)#2006
    print("Total Illness in 2007 were:",tenthyearill)#2007
    print("Total Illness in 2008 were:",eleventhyearill)#2008
    print("Total Illness in 2009 were:",twelvethyearill)#2009
    print("Total Illness in 2010 were:",thirteenyearill)#2010
    print("Total Illness in 2011 were:", fourteenyearill)#2011
    print("Total Illness in 2012 were:",fifteenyearill)#2012
    print("Total Illness in 2013 were:",sixteenyearill)#2013
    print("Total Illness in 2014 were:",seventeenyearill)#2014
    print("Total Illness in 2015 were:",eighteenyearill)#2015
    
    
    Rate.append(firstyearill) 
    Rate.append(secondyearill)
    Rate.append(thirdyearill) 
    Rate.append(fourthyearill)
    Rate.append(fifthyearill) 
    Rate.append(sixthyearill) 
    Rate.append(seventhyearill)
    Rate.append(eightyearill) 
    Rate.append(ninethyearill)
    Rate.append(tenthyearill) 
    Rate.append(eleventhyearill) 
    Rate.append(twelvethyearill) 
    Rate.append(thirteenyearill) 
    Rate.append(fourteenyearill)
    Rate.append(fifteenyearill) 
    Rate.append(sixteenyearill) 
    Rate.append(seventeenyearill)
    Rate.append(eighteenyearill)
    
    #print("Total Illness in 1998 were:",Rate.popleft())

    Rate = list(Rate)
    #print(Rate)
   #As we obtained illness statistics we can also obtain all these for hospitalizations and fatalities
    
    import Librarywarning 
    
    #File I/O - you must read input from a file and produce an output file.
    Rateofall = Librarywarning.Ratefunction(Rate)
    print(Rateofall)
    with open("Rateofall.dat",'w') as fx:
        for listitem in Rateofall:
            fx.write('%s\n' % listitem)
    fx.close

    print("Average rate of illness in 17 years is:", Librarywarning.Averagerate(Rateofall))

with open('outbreaks.csv') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    columnnames = next(csvreader)
  
    Pathogens = []
    Years = []
    for row in csvreader:
        if row[6] not in Pathogens:
            Pathogens.append(row[6])

        if row[0] not in Years:
            Years.append(row[0])

    #print(Years)
            
    n = len(Pathogens)
    print("There are a total of ",n ,"Pathogens causing diseases till 2015")


#object orientation and use of class
    
    year1 = Librarywarning.Rate(2,2)
    
    print("After 2 years there might be:", year1.increase, "Pathogens")
    
    
    #print(ratefunction.increaseofthree(int(input("After how many years do you want to see total pathogens? "))))

    x = Years
    y = Rate
    plt.plot(x,y)
      
#Labelling x axis 
    plt.xlabel('Years') 
#Labelling y axis 
    plt.ylabel('Illness') 
  
# giving a title 
    plt.title('Illness vs time')
#show the plot 
    plt.show()
    #plt.savefig('Graphillness.png') #to save graph as image
   
    #we can find new pathogens every year by using this but, it is not accurate because data is not proper 
    '''
with open('outbreaks.csv') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    columnnames = next(csvreader)
    
    year1998 = []
    year1999 = []
    for row in csvreader:
        if row[0] == '1998' and row[6] not in year1998:
            year1998.append(row[6])

        if row[0] == '1999' and row[6] not in year1998 and row[6] not in year1999:
            year1999.append(row[6])
    print(len(year1998))
    print("New pathogens in year 1999 are:",len(year1999))
    

'''
print("*************************************************************************")
print("*****As we obtained Rate at which illness changed from 1998 to 2015.*****")
print("we can also obtain analysis about hospitalizations, fatalities with graph")
print("**************************************************************************")


