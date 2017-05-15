import sys
from edit_distance import edit_distance


def distance(group, s):
    'Calulate the average distance between seq S and seqs in GROUP'
    if not group:
        return 0
    distances = list(edit_distance(s, seq)[0] if seq[0:2] == s[0:2] else 9999
                     for seq in group)  # 前两个字母不同的单词不在一起
    return sum(distances) / len(distances)


def grouping(groups, s, accuracy=2):
    'grouping seq S into one of group in GROUPS'
    if not groups:
        groups.append([])
    distances = list(distance(group, s) for group in groups)
    min_distance = min(distances)
    min_pos = distances.index(min_distance)
    # print('min_distance=', min_distance, "min_pos=", min_pos)
    if min_distance <= accuracy:
        groups[min_pos].append(s)
    else:
        groups.append([s])
    return groups


if __name__ == '__main__':
    # 1,2个字母组成的单词就不要参活了....
    words = (word.strip() for word in sys.stdin if len(word) > 2)
    words = sorted(words)
    groups = list()
    for word in words:
        grouping(groups, word)
    groups = sorted(groups, key=len)
    for group in groups:
        print(group, end='\n\n')
