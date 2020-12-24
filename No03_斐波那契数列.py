def fei():
    a, b = 0, 1
    list = []
    while b < 1000:
        list.append(str(b))
        a, b = b, a+b
    # print(list)
    print(", ".join(list))  # join只用于str类型

if __name__ == "__main__":
    fei()