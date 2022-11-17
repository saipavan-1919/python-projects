# convert date from yyyy-mm-dd format to dd-mm-yyyy format

date = "2000-08-05"
date = date.split("-")
print(date)
y=date[0]
m=date[1]
d=date[2]
date=f"{d}-{m}-{y}"
print(date)
