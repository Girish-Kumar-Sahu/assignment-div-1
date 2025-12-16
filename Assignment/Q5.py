words = dict()
s = input('enter the sentance: ')
for i in range(len(s)):
    words[s[i]] = words.get(s[i], 0) + 1
print(words)