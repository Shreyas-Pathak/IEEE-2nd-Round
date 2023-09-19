L = list(map(int, input("Enter 5 numbers:(extra numbers entered will be removed) ").split()))
def divisors(n):
    int r = n//2
    for i in range(r):
        if (n%i == 0):
            l.append(i)
    l.append(n)
    l.reverse()
    return l

for i in L:
    total.extend(divisors(i))

total.sort(reverse=True)

for i in total:
    if total.count(i)==5:
        print("The Greatest common divisor of all the above numbers is: ",i)
        break
