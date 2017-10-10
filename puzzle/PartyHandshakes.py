from itertools import permutations, combinations

couples = [
    ('Noel', 'Holly'),
    ('Alex', 'Brenda'),
    ('Charles', 'Diana'),
    ('Edward', 'Felix'),
    ('George', 'India')
]

everyone = []
for c in couples:
    everyone.append(c[0])
    everyone.append(c[1])

possible_unknown_pair = []
for t in combinations(everyone, 2):
    can_add = True
    for c in couples:
        if (c[0] == t[0] and c[1] == t[1]) or (c[0] == t[1] and c[1] == t[0]):
            can_add = False

    if can_add:
        possible_unknown_pair.append(t)

for p in possible_unknown_pair:
    print(p)
#print(len(possible_unknown_pair))

x = 0
for c1 in combinations(possible_unknown_pair, 8):
    x += 1
print(x)



