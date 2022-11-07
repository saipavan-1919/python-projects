"""
    Binary to decimal nummber conversion
"""

bin = "1010"
bin = bin[::-1]
dec = 0
i=0
while i<len(bin):
    if bin[i]=='1':
        dec = dec + (2**i)
    i=i+1

print(dec)

