# counting the number of every character of a given text file

f = open("file2.txt")
s = f.read()
print(s)
viewed_chars = []
count_chars = []
for i in s:
    count = 0
    if i in viewed_chars:
        continue
    viewed_chars.append(i)
    for j in s:
        if j==i:
            count += 1
    count_chars.append(count)

print(viewed_chars,count_chars)
f.close()
