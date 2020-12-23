def shuchu(str):
    if str == "乘法" or str == "加法" or str == "除法" or str == "减法":
        print("=================================================九九{}表=================================================".format(str))
        for i in range(1, 10):
            for j in range(1,i+1):
                if str == "乘法":
                    print("{} * {} = {}".format(j, i, j*i), end="\t")
                elif str == "加法":
                    print("{} + {} = {}".format(j, i, j+i), end="\t")
                elif str == "除法":
                    print("{} ÷ {} = {}".format(j*i, j, i), end="\t")
                elif str == "减法":
                    print("{} - {} = {}".format(j+i, j, i), end="\t")
            print()
        print("=================================================九九{}表=================================================".format(str))
    else:
        print("输入错误！！")

if __name__ == "__main__":
    shuchu("乘法")