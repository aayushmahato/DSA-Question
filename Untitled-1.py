
# creating array
n = int(input("enetr the lenght of list = "))
a = []
for k in range(n):
    x = int(input("enter the number = "))
    a.append(x)
print(a)

# for rotating array 
m = int(input("enetr the shifts = "))

for count in range(m):
    z = a[0]
    for i in range(1,n):
        a[i-1] = a[i]
    a[n-1] = z

print(a)