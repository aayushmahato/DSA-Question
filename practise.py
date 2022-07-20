

n = int(input("enetr the lenght of list = "))
a = []
for k in range(n):
    x = int(input("enter the number = "))
    a.append(x)
print(a)

def sort(a):
    for i in range(0,n-1):
        for j in range(0,n-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a

sort(a)
z = int(input("enetr = "))

print(a[z-1])

c = int(input("enetr = "))
print(a[len(a)-c])




