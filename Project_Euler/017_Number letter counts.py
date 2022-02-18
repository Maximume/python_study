# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

dict = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3,
    11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6,
    30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 100:7, 1000:11
    }

res = 0

for i in range(1,1000 + 1):
    if len(str(i)) == 1:
        res += dict.get(i)

    elif len(str(i)) == 2:
        if dict.get(i, 0) == 0:
            res += dict.get(int(str(i)[0]) * 10) + dict.get(int(str(i)[-1]))
        else:
            res += dict.get(i)

    elif len(str(i)) == 3:
        if i%100 == 0:
            digits3 = dict.get(int(str(i)[0])) + dict.get(100)
        else:
            digits3 = dict.get(int(str(i)[0])) + dict.get(100) + 3

        if dict.get(int(str(i)[1:]), 0) == 0:
            res += dict.get(int(str(i)[1]) * 10) + dict.get(int(str(i)[-1])) + digits3
        else:
            res += dict.get(int(str(i)[1:])) + digits3

    else:
        res += dict.get(i)

print(res)