t = int(input("Enter the number of test cases: "))
for i in range(t):

    number = int(input("Enter the number of numbers you want to input(if nos. entered are more than specified here, the extra numbers will be ignored): "))
    L = list(map(int, input().split()))
    del L[number:]
    print (L)
    even=[]
    odd=[]
    for i in range(len(L)):
        if (i%2==0):
            even.append(abs(L[i]))

        else:
            odd.append(abs(L[i]))

    print(even)
    print(odd)
    even.sort()
    odd.sort()
    a = 0
    b = 0
    if (even[0]>=odd[len(odd)-1]):
        for i in even:
            a = a + i

        for i in odd:
            b = b+i
            
    
        print("The maximum alternating sum is: ", a-b)
        
    else:
        low = even[0]
        del even[0]
        high = odd[len(odd)-1]
        odd.pop()
        odd.append(low)
        even.append(high)
        for i in even:
            a = a + i

        for i in odd:
            b = b+i
            
    
        print("The maximum alternating sum is: ", a-b)
        print()
