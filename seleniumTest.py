import csv
import ast
main = []
mainList = []
with open('seleniumExtractNew25.csv',"rb") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        main.append(row['Photos'])

    for i in main:
        mainList.append(ast.literal_eval(i))
    
    for j in mainList:
        for k in j:
            print k
