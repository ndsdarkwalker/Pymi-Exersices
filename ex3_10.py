#!/usr/bin/env python3

"""
Đọc thêm (không liên quan tới bài này): https://pymi.vn/blog/bankers-rounding/
"""
data = (
    [1, 5, 2, 3, 4],
    [4, 5, 0, 4]
)


def solve(list1, list2):
    '''Find common elements of two given lists.

    Returns a list contains those elements.
    Require: use only lists, if/else and for loops.
    '''
    result = []

    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    for i in data [0]:
        if i in data[1] and i not in result:
            result.append(i)

    return result


def main():
    L1, L2 = data
    print(solve(L1, L2))


if __name__ == "__main__":
    main()
