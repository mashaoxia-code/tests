'''大树数乘法'''
# coding=utf8

import sys


class Solution(object):

    def list2str(self,li):
        while li[0] == 0:
            del li[0]
        res = ''
        for i in li:
            res += str(i)
        return res

    def multi(self,stra, strb):
        aa = list(stra)
        bb = list(strb)
        lena = len(stra)
        lenb = len(strb)
        result = [0 for i in range(lena + lenb)]
        for i in range(lena):
            for j in range(lenb):
                result[lena - i - 1 + lenb - j - 1] += int(aa[i]) * int(bb[j])
        for i in range(len(result) - 1):
            if result[i] >= 10:
                result[i + 1] += result[i] // 10
                result[i] = result[i] % 10
        return self.list2str(result[::-1])


if __name__ == '__main__':

    s = Solution()
    if len(sys.argv) != 3:
        print('请输入两个參数')
        exit()
    a = sys.argv[1]
    b = sys.argv[2]
    res = s.multi(a, b)
    print('multi', res)
    print('ok', int(a) * int(b))

