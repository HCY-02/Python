num = int(input())
mid = num//2
str1 = ""
for i  in range(1,mid+1):
    str1 = ""
    for x in range(mid-i+1):
        str1 += " "
    for y in range(1,i+i):
        str1 += "*"
    print(str1)

str1 = ""
for i in range(num):
    str1 += "*"
    
print(str1)

for i  in range(mid,0,-1):
    str1 = ""
    for x in range(mid-i+1):
        str1 += " "
    for y in range(1,i+i):
        str1 += "*"
    print(str1)