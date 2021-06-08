import csv
import sys
import pprint
import re
dna_seq= ''
db_str = []
my_d = {}

if len(sys.argv) < 3:
    print("usage error")
    sys.exit()

with open(sys.argv[2], 'r') as seq_file:
    dna_seq = seq_file.read()

with open(sys.argv[1], 'r') as db_file:
    reader = csv.reader(db_file)
    for row in reader:
        dna_sequences = row
        dna_sequences.pop(0)
        break
        # key = row.pop("name")
        # my_d[key] = row.values()
for item in dna_sequences:
    my_d[item] = 1
    # for i,row in enumerate(reader):
    #     for key, val in row.items():
    #         print(key, val)
    #         my_d[key] = val
# print(my_d)

for key in my_d:
    l = len(key)
    tempMax = 0
    temp = 0
    for i in range(len(dna_seq)):
        # after having counted a sequence it skips at the end of it to avoid counting again
        while temp > 0:
            temp -= 1
            continue

        # if the segment of dna corresponds to the key and there is a repetition of it we start counting
        if dna_seq[i: i + l] == key:
            while dna_seq[i - l: i] == dna_seq[i: i + l]:
                temp += 1
                i += l

            # it compares the value to the previous longest sequence and if it is longer it overrides it
            if temp > tempMax:
                tempMax = temp

    my_d[key] += tempMax

with open(sys.argv[1], 'r') as db_file:
    reader = csv.DictReader(db_file)
    for person in reader:
        match = 0
        for dna in my_d:
            # print(dna)
            if my_d[dna] == int(person[dna]):
                match += 1
        if match == len(my_d):
            print(person['name'])
            sys.exit()
    print("No match")
