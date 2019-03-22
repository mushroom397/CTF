key = []
for num1 in range(0,10):
    for num2 in range(0,10):
        if num1 + num2 <= 9 :
            res = num1 + num2
            key = str(num1) + " " + "+" + " " + str(num2) + " " + "=" + " " + str(res)
            print(key)
            key = str(res) + " " + "=" + " " + str(num1) + " " + "+" + " " + str(num2)
            print(key)
        if num1 - num2 >= 0:
            res = num1 - num2
            key = str(num1) + " " + "-" + " " + str(num2) + " " + "=" + " " + str(res)
            print(key)
            key = str(res) + " " + "=" + " " + str(num1) + " " + "-" + " " + str(num2)
            print(key)
        if num1 * num2 <= 9:
            res = num1 * num2
            key = str(num1) + " " + "*" + " " + str(num2) + " " + "=" + " " + str(res)
            print(key)
            key = str(res) + " " + "=" + " " + str(num1) + " " + "*" + " " + str(num2)
            print(key)
        if num2 > 0 and num1%num2 == 0:
            res = int(num1 / num2)
            key = str(num1) + " " + "/" + " " + str(num2) + " " + "=" + " " + str(res)
            print(key)
            key = str(res) + " " + "=" + " " + str(num1) + " " + "/" + " " + str(num2)
            print(key)
