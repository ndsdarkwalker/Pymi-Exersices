#!/usr/bin/env python3


def solve(input_data):
    '''Kiểm tra input_data có phải là palindrome không.

    Một string được gọi là `palindrome` nếu viết xuôi hay ngược đều thu được
    kết quả như nhau (không phân biệt hoa thường, bỏ qua dấu space).
    String phải dài hơn 2 chữ cái.
    Ví dụ các palindrome: 'civic', 'Able was I ere I saw Elba', 'Noon'

    :rtype: bool
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    data = input_data.lower().replace(' ', '')
    if len(data) <= 2:
        result = False
    elif data[::-1] == data:
        result = True
    else:
        result = False

    return result


def main():
    print(solve('Able was I ere I saw Elba'))


if __name__ == "__main__":
    main()
