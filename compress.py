import re

def compress(string):
    string = string.lower()
    clusters = []
    for i in range(0, len(string)):
        for k in range(i + 2, len(string) + 1):
            section = string[i:k]
            clusters.append((string.count(section) * (k - i) - k + i, section))


    clusters = sorted(clusters)
    clusters.reverse()
    out = []
    for i in clusters:
        if (i not in out) and (i[0] > 2):
            out.append(i)

    return out


def get_dict(string, depth):
    alphabet = "☀☂☃☄★☆☇☈☉☊☋☌☍'☎☏☐☑☒☓☖"
    greedy_string = string.lower()
    out = []
    for i in range(0, depth):
        next = compress(greedy_string)[0]
        out.append(next)
        replacent = next[1]
        greedy_string = greedy_string.replace(replacent, alphabet[i])
    return out


lyrics = '''
The_Man_by_Aloe_Blacc_Well_you_can_tell_everybody_Yeah_you_can_tell_everybody_Go_ahead_and_tell_everybody_I'm_the_man,_I'm_the_man,_I'm_the_man_Well_you_can_tell_everybody_Yeah_you_can_tell_everybody_Go_ahead_and_tell_everybody_I'm_the_man,_I'm_the_man,_I'm_the_man_Yes_I_am,_yes_I_am,_yes_I_am_I'm_the_man,_I'm_the_man,_I'm_the_man
'''
print(get_dict(lyrics, 3))
