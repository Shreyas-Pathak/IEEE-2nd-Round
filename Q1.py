
s1 = input(str("Enter a string: "))
s2 = input(str("Enter another string: "))
L1 = []
for i in s1:
    L1.append(i)
  
L2=[]
for i in s2:
    L2.append(i)
  
L1.sort()
L2.sort()

if(len(L1) != len(L2)):
    print("Strings are not balanced.")

elif(len(L1) == len(L2)):
           if ( L1 == L2):
               print("Strings are balanced.")

           else:
               print("Strings are not balanced.")
        
