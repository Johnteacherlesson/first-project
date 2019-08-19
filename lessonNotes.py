a=10
# global variable
# coding is a procedural langauge

def say10():
    a = 100
    # local variable

    a = 10
    print(a)
    
    b=19
    
    print(b);


say10();

import random
#needed for random number generator

def randgen():
#generate random numbers higher then 50 but lower than 100
   
    a=random.randint(0,101)
    print(a)
    if a<50:
       a=a+10 
       print(a)
       randgen();
       
randgen();


import random



def randLgen():
    g=["N-NANI!","MUDA","5 mins on the clock","burning time"]
    b=random.choice(g)
    print(b)

randLgen();
