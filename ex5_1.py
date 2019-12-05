#!/usr/bin/env python3


data = {
    'xanh lá': '#3cba54',
    'vàng': '#f4c20d',
    'đỏ': '#db3236',
    'xanh da trời': '#4885ed',
}


def solve(colors):
    '''Ghi ra file index.html code HTML để tạo ra logo của Google với màu sắc
    chính xác.
    Biết cách để tạo chữ G màu xanh da trời dùng code HTML sau::

      <span style="color:#4885ed">G</span>

    Return list chứa các tuple, mỗi tuple  chứa chữ cái trong 'Google' và màu
    của nó.
    Gợi ý: dùng `zip`

        In [1]: list(zip(['xanh', 'do'], ['XXX', 'YYY']))
        Out[1]: [('xanh', 'XXX'), ('do', 'YYY')]
    '''
    result = []

    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    textzip = list(zip(['#4885ed', '#db3236', '#f4c20d', '#4885ed', '#3cba54','#db3236' ], ['G', 'o', 'o', 'g', 'l', 'e']))
    result = [(i[1], i[0]) for i in textzip] 
    with open ("index.html", "wt") as f:
        for i in result:
            f.write('<span style="color:{}">{}</span>'.format(i[1], i[0]))


    return result


def main():
    '''Biết mã hex của các màu trong Google logo là:
    '''
    colors = data
    print(solve(colors))


if __name__ == "__main__":
    main()
