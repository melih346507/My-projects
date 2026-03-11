func = input("Write your function (ax^b+c)")

num =[]
katsayi = []
us = []

for i in range(len(func)):
    if func[i].isdigit():
        num.append(int(func[i]))

for i in range(len(num)):
    if (i+1) < len(num) and i%2 == 0:
        a = num[i] * num[i+1]
        katsayi.append(a)
        x = num[i+1] - 1
        us.append(x)


for a in range(len(katsayi)):
    print(f"{katsayi[a]}x^{us[a]}",end="")
    if a+1 < len(katsayi):
        print("+",end="")
