a = input("ENTER A WORD")
for i in a:
     if (i == 'A'):
         print("A as found")
         break
     else:
         print("A not found")
         
         
         
         
         for x in range (10):
             if x % 20 == 0:
                 print("twist")
                 
                 
                 
             elif x % 15 == 0:
                 pass
             elif x % 5 == 0:
                 print("fizz")
             elif x % 3 == 0:
                 print("buzz")
             else:
                 print(x)
 
 
 # break cuts the statament  and goes to the next code
 # pass is null 
 # continue leaves the statment 
 #

var = 10            
while var > 0:
    var = var -1
    if var == 5:
        continue
    print('\ncurrent variable value:', var)
print("\ngood bye!")
    
