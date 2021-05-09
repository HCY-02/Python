i = int(input("組數為:"))
x = []
for x in range(i):
    inp = input("第"+str(x+1)+"組:")
    mid = inp.find(' ')
    ans = int(inp[:mid])*250 + int(inp[mid+1:])*175
    x.append(ans)

for y in range(i):
    print("第"+str(y+1)+"組應收費用:"+str(x[y]))