import gym, itertools, numpy as np, pandas as pd, random

rule = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mapped_observation = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

list_dict_rules = []
dict_rules = {}
combinations_5_neighbours = list(itertools.product([0, 1], repeat=5))
combinations_5_neighbours = ["".join(str(seq)).replace(',','').replace(' ','').replace('(','').replace(')','') for seq in combinations_5_neighbours]
size = 10

for iteration in range(0,10):
    for combination in combinations_5_neighbours:
        dict_rules[combination] = random.randint(0, 1)
    list_dict_rules.append(dict_rules)


oldline = mapped_observation
for ruleset in list_dict_rules:
    newline = [0] * len(mapped_observation)
    for x in range(0,len(mapped_observation)):
        for bit in range(len(mapped_observation)):
            combination = str(oldline[bit % 60]) + str(oldline[(bit+1) % 60]) + str(oldline[(bit+2) % 60]) + str(oldline[(bit+3) % 60]) + str(oldline[(bit+4) % 60])
            newline[(bit+2) % 60] = ruleset[combination]
        oldline = newline


    print(newline)
    print(newline.count(1))
    print("1") if newline.count(1) > (len(mapped_observation)/2) else print("0")