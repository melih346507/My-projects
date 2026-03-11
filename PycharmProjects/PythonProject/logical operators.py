
#or


#temp = 59
#is_raining = False

#if temp > 35 or temp < 0 or is_raining:
#    print("İçerde kal")
#else:
#    print("Dışarı çıkabilirsin")

# and, not
temp = 50
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is Cold outside")
    print("It is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside")
    print("It is sunny")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is not sunny")
elif temp <= 0 and not is_sunny:
    print("It is Cold outside")
    print("It is not sunny")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside")
    print("It is not sunny")
