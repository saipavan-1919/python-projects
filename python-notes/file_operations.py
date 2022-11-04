"""
    File operations:
        In python we can perform operations like opening, reading, writing, closing files.
        Open()::
            we can open a file using open function
            syntax: 
                open(<file name/path>,<mode>)
                returns a file object
            modes:
                r: open an existing file for a read operation.
                w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
                a:  open an existing file for append operation. It won’t override existing data.
                r+:  To read and write data into the file. The previous data in the file will be overridden.
                w+: To write and read data. It will override existing data.
                a+: To append and read data from the file. It won’t override existing data
        close():
            After opening a file and performing the required operation we need to close the file.
            syntax:
                <file_object>.close()
            ex:
                f = open("file","r")
                f.close()
        read():
            we can read data from file using the method read()
            syntax: 
                <file_object>.read(<size>)
                returns the data from file
        write():
            we can write into the file using write() method.
            First we need to open the file in append or writing mode.
            syntax:
                <file_object>.write("string")

                
"""

# opening a file
f = open("file.txt", "r")
# closing a file
f.close()

# other way of opening file
with open("file.txt",'r') as file:
    print(file.read())
    file.close()

# reading from a file
f = open("file.txt", "r")
print(f.read()) # to read entire file
print(f.read(10)) # to read 10 characters from file
f.close()

# writing into a file
f = open("file.txt",'w')
f.write("HI i opened the file and wrote this.")
f.close()

# opening in appending mode
with open("file.txt",'a') as file:
    file.write("now i opened the file in appending mode")
    #print(file.read())
    file.close()

# reading line by line
with open("file.txt","r") as f:
    line = f.readlines()
    for i in line:
        print(i)
