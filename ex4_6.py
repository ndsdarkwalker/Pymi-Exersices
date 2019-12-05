#!/usr/bin/env python3


def solve(text):
    '''Bóc tách từ `text` ra một list các số theo thứ tự chúng xuất hiện.

    VD: 'Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu'
    -> [60, 20, 0]

    NOTE: không dùng `re` library
    '''

    result = []

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    a = []
    for s in text:
        if s.isdigit():
            a.append(s)
        else:
            if a:
                result.append(int(''.join(a)))
                a = []
    if a:
        result.append(int(''.join(a)))


    return result


def main():
    ss = 'Bé lên 3 bé đi lớp 4'
    print(solve(ss))
    assert solve(ss) == [3, 4]


if __name__ == "__main__":
    main()
