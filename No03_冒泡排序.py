# 冒泡排序
def maopao(list):
    for j in range(1, len(list)):
        for i in range(len(list)-j):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
            else:
                continue
    print("冒泡排序后列表：", list)


if __name__ == "__main__":
    mp = [11, 21, 13, 24, 35, 16, 37, 28]
    print("冒泡排序前列表：", mp)
    maopao(mp)
