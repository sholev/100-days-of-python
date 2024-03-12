piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
piano_tuples = ('do', 're', 'mi', 'fa', 'so', 'la', 'si')

# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(piano_keys)

# ['c', 'd', 'e']
print(piano_keys[2:5])

# ['c', 'd', 'e', 'f', 'g']
print(piano_keys[2:])

# ['a', 'b', 'c', 'd', 'e']
print(piano_keys[:5])

# ['c', 'e']
print(piano_keys[2:5:2])

# ['a', 'c', 'e', 'g']
print(piano_keys[::2])

# ['g', 'f', 'e', 'd', 'c', 'b', 'a']
print(piano_keys[::-1])

# ('mi', 'fa', 'so')
print(piano_tuples[2:5])
