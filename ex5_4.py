#!/usr/bin/env python3

NUMBER_OF_LINES = 30000000


def solve(output_path):
    '''Tạo ra 1 file chứa 30 triệu dòng, các dòng lẻ chứa 30 số 1,
    các dòng chẵn chứa giá trị 2 * số dòng hiện tại.

    Sau khi tạo xong file, return result là list chứa 10 dòng cuối theo thứ tự
    dòng xuất hiện trước đứng trước.

    Chú ý: 30 triệu dòng.
    '''
    result = None
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    import os
    with open ('text.txt', 'wt') as f:
        for i in range (1, NUMBER_OF_LINES + 1):
            if i % 2 != 0:
                f.write('{}\n'.format('1' * 30))
            else:
                f.write('{}\n'.format(i * 2))
    f.close()

    f = open('text.txt', 'rt')
    content = f.readlines()
    f.close()
    
    result = content[NUMBER_OF_LINES - 10: NUMBER_OF_LINES]
    os.remove("text.txt")
    #
    #
    #
    #

    import os
    # Xoá file sau khi đã xong vì file này rất lớn
    try:
        os.remove(output_path)
    except OSError as e:
        print(e)

    return result


def main():
    import tempfile
    # tên _ hàm ý rằng ta sẽ không dùng giá trị của nó - convention
    _, output_path = tempfile.mkstemp()
    print('File to write: {0}'.format(output_path))
    for line in solve(output_path):
        print(line.rstrip())


if __name__ == "__main__":
    main()
