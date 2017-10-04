"""
Comparing 2 DFA
using two input files
format following dfa_simp
"""
from dfa_simp import minimize, print_dfa


def apply_config(config, s, f, dfa):
    ndfa = dict()
    nf = list(map(lambda n: config[n], f))
    ns = config[s]
    for k in dfa:
        ndfa[config[k]] = list(map(lambda n: config[n], dfa[k]))
    return ns, nf, ndfa


def exact_dfa_comp(dfa1: {int: [int]}, dfa2: {int: [int]}):
    if dfa1.keys() != dfa2.keys():
        return False
    for k in dfa1.keys():
        if dfa1[k] != dfa2[k]:
            return False
    return True


def dfa_comp(s1, f1, dfa1: {int: [int]}, s2, f2, dfa2: {int: [int]}):
    from itertools import permutations
    for cfg in permutations(dfa2.keys()):
        s, f, dfa = apply_config(cfg, s2, f2, dfa2)
        # if exact_dfa_comp(dfa1, dfa) and s == s1 and set(f) == set(f1):
        if exact_dfa_comp(dfa1, dfa):
            return True, (s, f, dfa)
    return False, None



