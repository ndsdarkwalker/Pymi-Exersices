#!/usr/bin/env python3

term1 = {'math': 3, 'python': 5, 'data': 2}
term2 = {'math': 7, 'python': 9, 'SQL': 8, 'HTML': 6}
data = [term1, term2]


def solve(term1, term2):
    '''Trả về result là dict chứa bảng điểm của các môn học sau hai học kỳ.
    Biết điểm số được chọn là điểm số ở lần học sau cùng.
    '''

    result = {}
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    for i in term1:
        if i not in term2:
            term2[i] = term1[i]
    result = term2
    
    return result


def main():
    # Một học viên có bảng điểm học kỳ 1 trong term1
    # Học kỳ 2, học thêm/lại có bảng điểm trong term2

    print(solve(*data))


if __name__ == "__main__":
    main()
