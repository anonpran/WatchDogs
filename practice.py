#python pgm demonstrating writing to csv
import csv

fields = ['Name','Branch','Year','CGPA']

rows = [['Nikhil','COE','2','9.0'],
        ['Sanchit','COE','2','9.1']]

filename = "university.csv"

#writing to csv file
with open(filename,'w') as csvfile:
    #creating a csv writier object
    csvwriter = csv.writer(csvfile)

    #writing the fields
    csvwriter.writerows(rows)
    