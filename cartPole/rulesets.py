import itertools, csv, pandas as pd
from pprint import pprint

# lst = list(itertools.product([0, 1], repeat=16))
# lst = ["".join(str(seq)).replace(',','').replace(' ','').replace('(','').replace(')','') for seq in lst]

# df = pd.DataFrame(lst)
# df = df.astype(str)
# df.to_csv('ruleset.csv', index=False)


# lst2 = list(itertools.product([0, 1], repeat=4))
# lst2 = ["".join(str(seq)).replace(',','').replace(' ','').replace('(','').replace(')','') for seq in lst2]

# df2 = pd.DataFrame(lst2)
# df2 = df2.astype(str)
# df2.to_csv('observation_space.csv', index=False)

df = pd.read_csv('observation_space.csv', dtype=str)
df2 = pd.read_csv('ruleset.csv', dtype=str)

observations = df.values.tolist()
rulesets = df2.values.tolist()

list_rulesets = []

for ruleset in rulesets:
    dict = {}
    rule = "".join(ruleset)
    for i in range(len(observations)):
        dict[observations[i][0]] = rule[i]
    list_rulesets.append(dict)