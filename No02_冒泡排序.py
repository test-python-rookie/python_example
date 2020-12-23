def maopao():
    list = [9,8,7,6,5,4,3,2,1]
    for j in range(len(list)):
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
            else:
                continue
    print(list)

if __name__ == "__main__":
    maopao()
