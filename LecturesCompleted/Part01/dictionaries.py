# Sözlükler nedir? key-value

myDict = {'eren': 'darıcı', 'IEEE': 'ESTU', 'Hello': 'Merhaba'}
print(myDict)

# .get(key)
valueEren = myDict.get('eren')
print(valueEren)

# .keys()
myKeys = myDict.keys()
print(myKeys)

# .values()
myValues = myDict.keys()
print(myValues)

# .items()
myItems = myDict.items()
print(myItems)

# Değişim
myDict['IEEE'] = 'STAR'
print(myDict)

# .pop() - .clear()
myDict.pop('IEEE')
print(myDict)

myDict.clear()
print(myDict)
