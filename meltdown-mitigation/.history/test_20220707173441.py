dice = [5, 1, 2, 1, 5]
freqDic = {}

for index, key in enumerate(dice):
    index = int(index)
    key = int(key)

    if key in freqDic:
        freqDic[key] = int(freqDic[key])+1
        continue

    freqDic[key] = 1
two, three = False, False
print(two, three)
# print(list(freqDic))
