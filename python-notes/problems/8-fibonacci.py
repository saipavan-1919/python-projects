# fibonacci series
# 0 1 1 2 3 5 8
# Every element is a sum of its two previous elements

fi_li = [0,1]
n=10
i=2
while len(fi_li)<10:
    fi_li.append(fi_li[i-1] + fi_li[i-2])
    i+=1

print(fi_li)
