# this file is used to process the csv file and get the data from the logs for burst hung

import csv

import os

import re

import subprocess

def open_csv_file(csv_file):

    f = open(csv_file, 'r')

    reader = csv.reader(f)

    return reader

def write_csv_file(csv_file,data):

    with open(csv_file,'w') as f:

        csv_writer = csv.writer(f)

        csv_writer.writerows(data)

def find_test_seed(logs_path, serial_log):

    serial_log_path = logs_path + "/" + serial_log

    #print(serial_log_path)

    #print(os.path.exists(serial_log_path))

    if os.path.exists(serial_log_path):

        cmd = "grep 'burst hung' " + serial_log_path

        try:

            s=subprocess.check_output(cmd, shell=True)

            #print(s.decode("utf-8"))

            if "matches" in s.decode("utf-8"):

                cmd = "tail -3 " + serial_log_path

                p = subprocess.check_output(cmd, shell=True)

                #print(p.decode("utf-8"))

                status = "burst hung"

                data = p.decode("utf-8")

                return (status, data)

        except:

            #print("no string found")

            status = "no failure"

            data = ""

            return (status, data)

def logs_parser(final_csv, row, logs_path, test_seed_index):

    files = os.listdir(logs_path)

    #print(files)

    if len(files)==2:

        for log in files:

            if "serial" in log:

                serial_log = log

        status, data = find_test_seed(logs_path, serial_log)

        if status == "burst hung":

            test_seed = re.findall("Test [0-9a-z]* seed [0-9a-z]*",data)

            #print(test_seed)

            if len(test_seed) == 1:

                row[test_seed_index] = test_seed[0]

        final_csv.append(row)

            #row[test_seed_index + 1] = status

def main():

    csv_file = "output.csv"

    reader = open_csv_file(csv_file)

    heading = next(reader)

    #print(heading)

    final_csv = []

    final_csv.append(heading)

    #print(final_csv)

    logs_index = 0

    test_seed_index = 0

    for i in range(len(heading)):

        if heading[i] == "logs_path":

            logs_index = i

        if heading[i] == "test_seed":

            test_seed_index = i

    #print(logs_index, test_seed_index)

    for row in reader:

        logs_parser(final_csv,row,row[logs_index], test_seed_index)

    #print(final_csv)

    write_csv_file("result.csv",final_csv)

if __name__ == "__main__":

    main()
