# 调用python3自带函数min()
def xuanze1(list):
    newlist = []
    for i in range(len(list)):
        newlist.append(str(min(list)))
        list.remove(min(list))
    print(", ".join(newlist))

def xuanze2(list):
    for i in range(len(list)-1):
        minindex = i
        for j in range(i+1, len(list)):
            if list[minindex] > list[j]:
                minindex = j
        if i != minindex:
            list[i], list[minindex] = list[minindex], list[i]
    print(list)


if __name__ == '__main__':
    list = [5, 3, 8, 6, 1, 9]
    xuanze2(list)
