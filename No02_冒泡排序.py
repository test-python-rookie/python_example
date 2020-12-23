def maopao():
    list = [1,2,3,4,5,6,7,8]
    for j in range(len(list)):
        for i in range(len(list)-1-j):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
            else:
                continue
    print(list)

if __name__ == "__main__":
    maopao()
