'''用一个数组实现两个栈，只需处理整型，实现l_pop/l_push/r_pop/r_push'''
# coding=utf8

import sys


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack(object):
    def __init__(self):
        self.top = None

    def peek(self):
        if self.top == None:
            return None
        else:
            return self.top.val

    def l_push(self, n):
        n = Node(n)
        n.next = self.top
        self.top = n
        return n.val

    def l_pop(self):
        if self.top == None:
            return ('Stack L is empty')
        else:
            tmp = self.top.val
            self.top = self.top.next
            return tmp

    def r_push(self, n):
        n = Node(n)
        n.next = self.top
        self.top = n
        return n.val

    def r_pop(self):
        if self.top == None:
            return ('Stack R is empty')
        else:
            tmp = self.top.val
            self.top = self.top.next
            return tmp


if __name__ == '__main__':

    s = Stack()
    argv = sys.argv
    data = argv[1]
    for n in eval(data):
        s.l_push(n)
    print(s.l_pop())
    print(s.l_pop())
    print(s.l_pop())
    print(s.l_pop())

    for n in range(len(eval(data))-1,-1,-1):
        da = eval(data)
        s.r_push(da[n])
    print(s.r_pop())
    print(s.r_pop())
    print(s.r_pop())
    print(s.r_pop())


'''测试运行：Python array.py [1,2,3,4]'''
