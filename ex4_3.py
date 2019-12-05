#!/usr/bin/env python3


def solve(words):
    '''Trả về list chứa điểm tương ứng của các từ trong `words`

    Nếu a b c d (không phân biệt chữ hoa thường) .... lần lượt bằng 1 2 3 4 ...
    thì từ ``attitude`` có giá trị bằng 100.
    (http://www.familug.org/2015/05/golang-tinh-tu-cung-9gag.html)

    Gợi ý::

      import string
      print(string.ascii_lowercase)
    '''

    result = []

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    import string
    a = {i: j for i, j in zip(string.ascii_uppercase, range (1, 27))}
    for w in words:
        s= sum([a[i] for i in w.upper()])
        result.append(s)                                                                           

    return result


def main():
    words = ['numpy', 'django', 'saltstack', 'discipline',
             'Python', 'FAMILUG', 'pymi']

    print(solve(words))


if __name__ == "__main__":
    main()
