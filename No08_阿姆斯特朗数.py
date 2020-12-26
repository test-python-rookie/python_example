def amstl(num):
    temp = num
    sum = 0
    list = []
    n = len(str(num))
    if num >= 0:
        while temp > 0:
            digit = temp % 10
            sum += digit ** n
            m = "%d**%d" % (digit, n)
            list.append(m)
            temp = temp // 10
        print(" + ".join(list), " = ", sum)
        if num == sum:
            print(num, "是阿姆斯特朗数")
        else:
            print(num, "不是阿姆斯特朗数")
    else:
        print(num, "不是阿姆斯特朗数")

def shu():
    while 1:
        i = input("判断请按1，显示请按2，退出请按3：")
        if i == "1":
            try:
                num = int(input("请输入一个数字："))
                amstl(num)
            except ValueError:
                print("您输入的不是数字！！！")
        elif i == "2":
            try:
                num = int(input("请输入一个数字："))
                list = []
                while num >= 0:
                    temp = num
                    n = len(str(num))
                    sum = 0
                    while temp > 0:
                        digit = temp % 10
                        sum += digit ** n
                        temp = temp // 10
                    if num == sum:
                        list.append(str(sum))
                    num -= 1
                print(", ".join(list))
            except ValueError:
                print("输入错误，请重新输入！！！")
        elif i == "3":
            break
        else:
            print("输入错误，请重新输入！！！")

if __name__ == '__main__':
    shu()