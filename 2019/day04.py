

if __name__ == "__main__":

    cnt = 0
    for num in range(165432,707912):
        consec = False
        ooo = False
        strnum = str(num)
        if num == 166888:
            pass
        for i in range(1,len(strnum)):
            a = strnum[i]
            b = strnum[i-1]
            if b > a:
                ooo = True
                break
            if b == a:
                consec = True
        if ooo:
            continue
        if consec:
            cnt += 1
    print(cnt)



    cnt = 0
    for num in range(165432,707912):
        consec = False
        ooo = False
        strnum = str(num)
        if num == 166888:
            pass
        for i in range(1,len(strnum)):
            a = strnum[i]
            b = strnum[i-1]
            if b > a:
                ooo = True
                break
            if b == a:
                if i > 1:
                    if strnum[i-2] == b:
                        continue
                if i < len(strnum) - 1:
                    if strnum[i+1] == b:
                        continue
                consec = True
        if ooo:
            continue
        if consec:
            cnt += 1
    print(cnt)