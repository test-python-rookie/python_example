def charu(list):
    for i in range(len(list)):
        index = i - 1
        current = list[i]
        while index >= 0 and list[index] > current:
            list[index + 1] = list[index]
            index -= 1
        list[index + 1] = current
    print(list)



if __name__ == '__main__':
    list = [5, 3, 8, 6, 1, 9]
    charu(list)