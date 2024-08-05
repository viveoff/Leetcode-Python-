Used HashMap, iterated list with numbers, difference = target - number, check if number is in hashMap,
if not: store number in hashMap, if result is in HashMap ⇒ return [index[num], index [result]

nums = [2,7,11,15]
target = 9

For i = 0, n = 2:
- Calculate dif = 9 - 2 = 7
- Check if 7 is in hashMap (NO)
- Store '2' in hashMap with index '0': hashMap = {2: 0}

For i = 1, n = 7
- Calculate dif = 9 - 7 = 2
- Check if 2 in hashMap (YES, it is at index '0')
- Retrun [hashMap[2, i] which is [0, 1]]