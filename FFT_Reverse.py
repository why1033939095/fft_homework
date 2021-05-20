import math

def Reverse(alist):
    N = len(alist)
    M = int(math.log(N, 2))
    new =[i for i in range(N)]
    new[0] = alist[0]
    new[-1] = alist[-1]
    for i in range(1, N-1):
        if len(bin(i)[2:]) < M:
            origin_index = '0'*(M-len(bin(i)[2:])) + bin(i)[2:]
        else:
            origin_index = bin(i)[2:]
        new_index = ""
        l = [origin_index[j] for j in range(len(origin_index)-1, -1, -1)]
        for s in l:
            new_index += s
        index = int(new_index, 2)
        new[i] = alist[index]
    return new





if __name__=="__main__":
    alist = [i for i in range(32)]
    res = Reverse(alist)
    print(res)
    print("取其中的第四个元素:"+str(res[3]))
