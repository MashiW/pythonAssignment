#!/user/bin/python
__author__ = 'hsenid'

input_file = "output.csv"
output_file = open("processed.csv", "w+")

f = open(input_file, "r")
count = 1


for x in f:

    line = x.rstrip()
    line = line.split(",")
    lst = list(map(int, line))
    info =(str(count)+" "+ str(sum(lst))+", "+ str(max(lst))+", "+ str(min(lst)))
    count = count + 1
    output_file.write(info+"\n")