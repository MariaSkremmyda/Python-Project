import random

def num(my_list, x):
 
    found = True
    for i in range(0, x-2):
     
        for j in range(i+1, x-1):
         
            for k in range(j+1, x):
             
                if (my_list[i] + my_list[j] + my_list[k] == 0):
                    print(my_list[i], my_list[j], my_list[k])
                    found = True    
              
    if (found == False):
        print(" The number node with a zero sum does not exist! ")
 
my_list = random.sample(xrange(-30,30), 30)
x = len(my_list)
num(my_list, x)
