import math
import matplotlib.pyplot as plt
from FFT_Reverse import Reverse


def FFT(alist):
    N = len(alist)
    origin_index = [i for i in range(len(alist))]
    rvrs_index = Reverse(origin_index)
    new_alist = [i for i in range(len(alist))]

    for k in range(len(alist)):
        new_alist[k] = alist[rvrs_index[k]]
    alist = new_alist

    A = alist
    M = int(math.log(N, 2))

    for L in range(1, M+1):
        temp = [i for i in range(N)]
        B = int(math.pow(2, L-1))
        if B == 1:
            for i in range(0, N, 2):
                temp[i] = A[i] + A[i+B]*1
                temp[i+B] = A[i] - A[i+B]*1

            A = temp

        else:

            for k in range(int(N/math.pow(2, L))):
                for i in range(B):
                    temp[k*B*2+i] = A[k*B*2+i] + A[k*B*2+i + B] * (math.cos(math.pi * i/ B) - 1j * math.sin(math.pi * i/ B))
                    temp[k*B*2+i + B] = A[k*B*2+i] - A[k*B*2+i + B] * (math.cos(math.pi * i/ B) - 1j * math.sin(math.pi * i/ B))
            A = temp

            for i in range(N):
                A[i] = math.sqrt(math.pow(A[i].real, 2)+math.pow(A[i].imag, 2))
                if A[i] < math.exp(-3):
                    A[i] = 0
        A_max = max(A)
        for i in range(N):
            A[i] = A[i]/float(A_max)
    return A


if __name__=="__main__":
    F = int(input("请输入信号频率F："))
    N = int(input("请输入采样长度N："))
    T = float(input("请输入采样时间T："))
    x = [i for i in range(N)]
    b = [math.cos(T*2*i*math.pi/float(F)) for i in range(N)]
    y = FFT(b)
    print(FFT(b))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    plt.show()