import csv

row1 = []
emp = {}
def employee_data():
    with open("C:\\Users\\RAW\\Desktop\\bank_data.csv", 'r') as csvfile:
        file = csv.reader(csvfile)
        name = input("enter your name = ")
        row1 = file.__next__()
        while True:
            row = file.__next__()
            if row[0] == 'done':
                print("sorry, please enter a valid name")
                break
            elif row[0].lower() == name.lower():
                #print(row)
                i=0
                for item in row:
                    emp[row1[i]]=row[i]
                    i=i+1
                print(emp)
                return emp
    return {}
