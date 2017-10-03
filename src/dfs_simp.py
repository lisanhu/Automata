"""
Simplify a DFA

input file format: csv
start_state, final_state1, final_state2, ...
state, dest1, dest2, ...
...
"""


def parse_input(input_name: str) -> (int, [int], dict):
    input_file = open(input_name)
    lines = input_file.readlines()
    input_file.close()
    fields = lines[0].split(',')
    start_state = int(fields[0])
    final_states = []
    for s in fields[1:]:
        final_states.append(int(s))
    lines = lines[1:]
    transition = dict()
    for line in lines:
        fields = line.split(',')
        state = int(fields[0])
        transition[state] = list(map(lambda s: int(s), fields[1:]))
    return start_state, final_states, transition


def find_group(state, groups: [set]):
    for g in groups:
        if state in g:
            return g
    return None


def split_states(states: set, groups: [set], trans: dict):
    if states:
        states = list(states)
        dests0 = trans[states[0]]
        abc_size = len(dests0)
        gs = list(map(lambda s: find_group(s, groups), dests0))
        s1 = set()
        s2 = set()
        s1.add(states[0])

        for s in states[1:]:
            consistent = True
            for c in range(abc_size):
                if trans[s][c] not in gs[c]:
                    consistent = False
                    break
            if consistent:
                s1.add(s)
            else:
                s2.add(s)

        if not s2:
            return s1, None
        return s1, s2
    else:
        return states, None


# def split_states(states: set, trans: dict) -> (set, set):
#
#     pass


def dfa_mini(start: int, final, trans: dict):
    states = trans.keys()
    s1 = set()
    s2 = set()
    for s in states:
        if s in final:
            s2.add(s)
        else:
            s1.add(s)
    groups = [s1, s2]

    go = True
    while go:
        g_size = len(groups)

        for s in groups:
            ss1, ss2 = split_states(s, groups, trans)
            if ss2 is not None:
                groups.remove(s)
                groups.append(ss1)
                groups.append(ss2)

        if g_size == len(groups):
            go = False

    result = dict()
    result2 = dict()
    for i in range(len(groups)):
        if start in groups[i]:
            print('start state', i)
        if list(groups[i])[0] in final:
            print('final state', i)
        result[i] = list(map(lambda s: groups.index(find_group(s, groups)), trans[list(groups[i])[0]]))
        result2[i] = list(map(lambda s: find_group(s, groups), trans[list(groups[i])[0]]))

    for k in result.keys():
        print(k, end=' ')
        for j in result[k]:
            print(j, end=' ')
        print()
    for k in result2:
        print(groups[k], '\t\t', result2[k])


if __name__ == '__main__':
    start_state, final_states, transition = parse_input('input.txt')
    dfa_mini(start_state, final_states, transition)
