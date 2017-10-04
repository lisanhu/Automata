from dfa_comp import *


def q2():
    s1, f1, dfa1 = minimize('input1.txt')
    s2, f2, dfa2 = minimize('input2.txt')
    s3, f3, dfa3 = minimize('input3.txt')
    same1, ndfa1 = dfa_comp(s1, f1, dfa1, s3, f3, dfa3)
    same2, ndfa2 = dfa_comp(s2, f2, dfa2, s3, f3, dfa3)
    if same1 or same2:
        print(True)
    else:
        print(False)
        s, f, d = s3, f3, dfa3
        print(s, end=', ')
        print(f)
        print_dfa(d)


def q3():
    s1, f1, dfa1 = minimize('input4.txt')
    # print(s1, f1)
    # print_dfa(dfa1)
    s2, f2, dfa2 = minimize('input5.txt')
    same, ndfa = dfa_comp(s1, f1, dfa1, s2, f2, dfa2)
    if same:
        print(True)
    else:
        print(False)
        s, f, d = s2, f2, dfa2
        print(s, end=', ')
        print(f)
        print_dfa(d)


if __name__ == '__main__':
    q3()
