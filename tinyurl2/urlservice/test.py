#!/usr/bin/python


def convertTo62(num):
    ret = ""
    encode = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    while num != 0:
        inx = num % 62
        ret += encode[inx:inx+1]
        num //= 62
    print(ret)
    print(len(ret))
    return ret + encode[:6-len(ret)]

print(convertTo62(4134124312341))
print(convertTo62(2412341234))
print(convertTo62(124124124))

