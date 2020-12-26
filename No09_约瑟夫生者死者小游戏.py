people={}
for x in range(1,31):
    people[x]=1
s, i, j = 0, 1, 0
while i <= 31:
    if i == 31:
        i = 1
    elif j == 15:
        break
    else:
        if people[i] == 0:
            i += 1
            continue
        else:
            s += 1
            if s == 9:
                people[i] = 0
                s = 0
                j += 1
                print(i, "号下船了！！！")
            else:
                i += 1
                continue


