# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

f = open('words.txt', 'r')
words = f.read().replace('"','').split(',')

ords = []

for word in words:
    val = 0
    for ch in word:
        val += ord(ch)-64
    ords.append(val)

tris = []
i = 1
sum = 0
while sum < max(ords):
    sum += i
    tris.append(sum)
    i += 1
    
cnt = 0
for i in ords:
    if i in tris:
        cnt += 1
print(cnt)