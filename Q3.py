L = eval(input("Enter a list of characters: "))
total = [[]]
a = 1
for i in L:
    for j in range(0,a):
          l = total[j]
          l = l + [i]
          total.append(l)
    a = a*2      

print (total)
    
 
      
