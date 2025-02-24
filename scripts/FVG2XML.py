
import json

FVG = open("resources/FVG_list", "r")

verbs = dict()
actual = None
for line in FVG:
    line = line.rstrip()
    tokens = line.split(" ")
    if len(tokens) == 1:
        actual = tokens[0]
        verbs[actual] = list()
    else:
        verbs[actual].append(tokens[-1])

with open('resources/FVG.json', 'w') as fp:
    json.dump(verbs, fp)
