"""
    This file takes the json file name as the argument and if the file is not presant then it will create the file.
    It takes the command line arguments as file name, attribute and its value to be changed

    Options:
        -fn  : json file name
        -rai : replace all instance of the word in the entire file (action=store_true)
              for this -a string to be replaces with -v string
        -cav : change the attribute vlaue in file (action=store_true)
        -ria : repalce the word in attribute value in json file (action=store_true)  replace in attribute
        these are sub-options
        When we give above options we should mention the below things mustly.
        -a : mention attribute name
        -v : attribute value
"""
import os
import argparse
import json

parser = argparse.ArgumentParser(description="takind arguments")
parser.add_argument("-fn",help="json file name")
parser.add_argument("-rai",action="store_true",help="replace all instances of the word in entire json file")
parser.add_argument("-cav",action="store_true",help="change the value of the attrbute in the json file")
parser.add_argument("-ria",action="store_true",help="replace the word in the attribute value in json file")
parser.add_argument("-a",help="attribute")
parser.add_argument("-v",help="attribute value to be replaced")
args = parser.parse_args()

def copy_json_files(src, dest):
    # open both files
    with open(src,'r') as firstfile, open(dest,'w') as secondfile:
        # read content from first file
        for line in firstfile:
            # write content to second file
            secondfile.write(line)
    print("copied reference file into the created file")


def replace_all_instance(fpath, attr, val):
    # this api will replace the all instances of the attr in the json file with val.
    print("inside the replace_all_instance api")
    print("fpath, attr, val = ",fpath, attr, val)
    with open(fpath, 'r') as f:
        data = json.load(f)
        print(data[attr]) # data in the json file


def change_attr_value(fpath, attr, val):
    with open(fpath, 'r') as f:
        data = json.load(f)
        print(data)
    for k,v in data.items():
        if str(type(data[k])) == "<class 'dict'>":
            func(data[k],key, val)
        elif str(type(data[k])) == "<class 'list'>":
            for i in data[k]:
                if str(type(i)) == "<class 'dict'>":
                    func(i,key, val)
        elif k==key:
            data[key] = val
            print("\nafter changing the value of key = ",data[key])
    return data


def main():
    cwd = os.getcwd()
    print("cwd = ",cwd.split("burst-scripts")[0])
    cwd = cwd.split("burst-scripts")[0]
    fpath = cwd + "burst-scripts/script_gen/databases/" + args.fn
    rfpath = "/home/saipavan/sai/repo/burst-scripts/script_gen/databases/reference.json"
    print("complete file path = ",fpath)
    try:
        # try to open the file
        f = open(fpath, 'r')
        if not f.read():
            copy_json_files(rfpath, fpath)
        print("file opened successfully")
        f.close()
    except:
        # if file not found then create the file
        f = open(fpath,'w')
        f.close()
        print("file created successfully")
        copy_json_files(rfpath, fpath)

    if args.rai and args.a and args.v:
        print("r find")
        replace_all_instance(fpath, args.a, args.v)
    elif args.cav and args.a and args.v:
        print("cav find")
        data = change_attr_value(fpath, args.a, args.v)
    elif args.ria and args.a and args.v:
        print("ria find")
    else:
        print("please provide valid options")
        exit(0)

    json_obj = json.dumps(data, indent=4)
    with open(fpath, 'w') as outfile:
        outfile.write(json_object)

if __name__=="__main__":
    main()
else:
    print(exiting)
