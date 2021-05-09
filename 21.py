num = int(input("輸入查詢組數N為:"))
data = {'123 456':9000,'456 789':5000,'789 888':6000,'336 558':10000,'775 666':12000,'566 221':7000} 
x = []
for i in range(num):
    ans = input()
    x.append(ans)

for i in range(num):
    if (x[i] in data) == True:
        print(data[x[i]])
    else:
        print("error")