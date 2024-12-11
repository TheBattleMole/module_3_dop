
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

print((data_structure))
all_ = []
def dostaem(name):
    global all_
    for i in name:
        if isinstance(i, int):
            all_.append(i)
        if isinstance(i, str):
            all_.append(len(i))
        if isinstance(i, list):
            dostaem(i)
        if isinstance(i, tuple):
            dostaem(i)
        if isinstance(i, dict):
            for j in i.items():
                dostaem(j)
            


dostaem(data_structure)
print(all_)