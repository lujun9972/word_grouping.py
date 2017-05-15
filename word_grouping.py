import sys
from edit_distance import edit_distance


def distance(group, s):
    'Calulate the average distance between seq S and seqs in GROUP'
    if not group:
        return 0
    distances = list(edit_distance(s, seq)[0] for seq in group)
    return sum(distances) / len(distances)


def grouping(groups, s, expected=2):
    'grouping seq S into one of group in GROUPS'
    if not groups:
        groups.append([])
    for group in groups:
        d = distance(group, s)
        if d <= expected:
            group.append(s)
            break
    else:
        groups.append([s])
    return groups


if __name__ == '__main__':
    words = sys.stdin.readlines()
    words = sorted(words)
    groups = list()
    for word in words:
        grouping(groups, word)
    groups = sorted(groups, key=len)
    for group in groups:
        print(group, end='\n\n')
