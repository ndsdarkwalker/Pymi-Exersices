#!/usr/bin/env python3

'''
Input: một số nguyên trong range(1,13,1). # start=1, stop=13, step=1
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28
'''


def solve(input_data):
    '''Trả về 1 `list` chứa 2 phần tử, ví dụ:

        input_data: 2
        output: ("February", 28)

    :param input_data: tháng bất kì
    :rtype: list
    '''
    assert (input_data in range(1, 13, 1)), "Tháng không tồn tại"
    result = ["MONTH", "DATE"]

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    '''for i in range (1, 13, 1):
        if i == 1:
            print("Jan", 31)
        elif i == 2:
            print("Feb", 28)
        elif i == 3: 
            print("Mar", 31)
        elif i == 4:
            print("Apr", 30)
        elif i == 5:
            print("May", 31)
        elif i == 6:
            print("Jun", 30)
        elif i == 7:
            print("Jul", 31)
        elif i == 8:
            print("Agu", 31)
        elif i == 9:
            print("Sep", 30)
        elif i == 10:
            print("Oct", 31)
        elif i == 11:
            print("Nov", 30)
        else:
            print("Dec", 31)'''
    month = (("January", 31), ("February", 28), ("March", 31), ("April", 30), ("May", 31), ("June", 30), ("July", 31), ("August", 31), ("September", 30), ("Octorber", 31), ("November", 30), ("December", 31))
    result = month[input_data -1 ]

    return result


def main():
    month, day = solve(2)
    print(month, day)


if __name__ == "__main__":
    main()
