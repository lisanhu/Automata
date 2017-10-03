"""
Comparing 2 DFA
using two input files
format following dfa_simp
"""
from dfa_simp import minimize, print_dfa


def apply_config(config, dfa):
    ndfa = dict()
    for k in dfa:
        ndfa[config[k]] = list(map(lambda n: config[n], dfa[k]))
    return ndfa


def exact_dfa_comp(dfa1: {int: [int]}, dfa2: {int: [int]}):
    if dfa1.keys() != dfa2.keys():
        return False
    for k in dfa1.keys():
        if dfa1[k] != dfa2[k]:
            return False
    return True


def dfa_comp(dfa1: {int: [int]}, dfa2: {int: [int]}) -> bool:
    from itertools import permutations
    for cfg in permutations(dfa2.keys()):
        dfa = apply_config(cfg, dfa2)
        if exact_dfa_comp(dfa1, dfa):
            return True
    return False


if __name__ == '__main__':
    dfa1 = minimize('input1.txt')
    dfa2 = minimize('input2.txt')
    print(dfa_comp(dfa1, dfa2))
