
# creating array
n = int(input("enetr the lenght of list = "))
a = []
for k in range(n):
    x = int(input("enter the number = "))
    a.append(x)
print(a)

#reversing an aaray
def reverse(a):
    s = 0
    e = n-1
    while s < e:
        temp = a[s]
        a[s] = a[e]
        a[e] = temp
        s = s + 1
        e = e - 1
    return a

print(reverse(a))




