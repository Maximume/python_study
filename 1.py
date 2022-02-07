f = open('maze\\maze_map.txt', 'a')

line = f.readlines()
f.close()
line[0] = line[0].split()

print(f)
print(line)

f.close()