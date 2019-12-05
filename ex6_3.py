#!/usr/bin/env python3

import csv
import os
import time


def find_max_price(datafile):
    f = open(datafile)
    dr = csv.DictReader(f, ['time', 'price', 'UNKNOWN']) # NOQA
    # Viết tiếp code vào đây

    try:
        # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
        top1price = 0
        for i in dr:
            if (float(i['price'])) > top1price:
                top1price = float(i['price'])
                timetop = time.strftime('%Y - %m - %d', time.localtime(int(i['time'])))
        result = (top1price, timetop)
        

    finally:
        f.close()

    return result

def solve():
    '''Tìm ngày giá BTC lên cao nhất. Trả về Tuple chứa ngày ở định dạng
    YYYY-mm-dd (VD: 2017-06-19) và giá VND của 1 BTC
    '''
    # http://api.bitcoincharts.com/v1/csv/
    datafile = 'localbtcVND.csv'
    exdir = os.path.dirname(__file__)
    datapath = os.path.join(exdir, datafile)

    result = find_max_price(datapath)
    return result


def main():
    now = time.gmtime(int(time.time()))
    print(now.tm_year, now.tm_mon, now.tm_mday)
    print(solve())


if __name__ == "__main__":
    main()
