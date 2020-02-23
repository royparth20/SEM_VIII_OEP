def xyz(temp):
    # print(temp)
    if temp == 0:
        return 0
    l1 = [2, 3]
    for i in l1:
        print(i)
        x = xyz(i-1)
        if x == 0:
            return 0
        else:
            print(temp)
            return i-1

def temp(x):
    if x==0:
        return 0
    for i in range(x):
        print(x)
        return temp(x-1)-1
# print(xyz(None))
def pqr():
    print("pqr")
    return 0


def abc():
    pqr()
    print("abc")
    return 1


# print(abc())
temp(int(input("Enter NO : ")))