#!/usr/bin/env python3

'''
[Không bắt buộc]

Bắt đầu từ góc trên bên trái của ô có kích thước 2x2, và chỉ cho phép di chuyển
sang phải hoặc xuống dưới, có chính xác 6 đường để đi đến góc dưới bên phải.

Có bao nhiêu đường như vậy trong ô 10x10?

Kiểm tra kết quả bằng https://projecteuler.net/problem=15
'''


def solve(input_data):
    result = None
    # Viết code vào đây set result làm kết quả của tính toán
    #
    #
    #
    import math, time

    def count(gridsize):
        p = math.factorial(gridsize*2) / (math,factorial(gridsize**2))
        return p
    tic = time.clock()
    n = count(10)
    toc = time.clock()
    ttime = toc - tic
    print("%s found in %s seconds" %(n, ttime))
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
