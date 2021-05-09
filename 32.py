inputt = int(input("輸入一正整數:"))
if (inputt % 11 == 0)&(inputt % 2 == 0)&(inputt % 5 != 0)&(inputt % 7 != 0):
    print(str(inputt)+"為新公倍數?:Yes")
else:
    print(str(inputt)+"為新公倍數?:No")