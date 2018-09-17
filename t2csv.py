#! /usr/bin/python

import os
import csv

dirpath = '/Users/ashutoshahmadalexandar/Desktop/DIC/Lab3/Spark2/UnknownData2'
output = 'unknown2.csv'
with open(output, 'w') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(['Category', 'Article'])

    files = os.listdir(dirpath)

    for filename in files:
        with open(dirpath + '/' + filename) as afile:
        	file2 = filename.split('_')[0]
        	csvout.writerow([file2, afile.read()])
        	afile.close()

    outfile.close()
