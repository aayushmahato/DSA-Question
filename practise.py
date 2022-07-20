
# creating array
n = int(input("enetr the lenght of list = "))
a = []
for k in range(n):
    x = int(input("enter the number = "))
    a.append(x)
print(a)

# sorting the array
def sort(a):
    for i in range(0,n-1):
        for j in range(0,n-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a

sort(a)

# to find kth min element of array
z = int(input("enetr the kth min term = "))
print(a[z-1])

# to find kth max element of array
c = int(input("enetr the kth max term = "))
print(a[len(a)-c])




