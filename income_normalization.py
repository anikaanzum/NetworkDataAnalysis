import sys
import xlrd
import csv
import pandas
import os
import glob
import os.path


def read_csv(filename):
    data=[]
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile)
        for row in readCSV:
            data.append(row)
    #print(data)
    header=data[0]   
    #print(header) 
    return header


def get_csv_info(path,Tag):
	header=read_csv(path)
	#print(header)
	Tag='Median_Income'
	
	pop=[]
	area=[]
	for i in header:
		if(Tag==i):
			
			#print("Found")
			with open(path) as f:
				reader = csv.DictReader(f, delimiter=',')
				for row in reader:
					pop.append(row[Tag])
					area.append(row['Areaname'])
		
	return pop,area
		
my_path = os.path.abspath(os.path.dirname(__file__))
#print(my_path)
path = os.path.join(my_path, "CensusData/CountyData/")
#print(path)
extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('*.{}'.format(extension))]
#print(result)
file_name='income_county.csv'
path = os.path.join(path, file_name)
#print(path)
Tag=['Median_Income']
income_arr,area=get_csv_info(path,Tag)
#print(pop_arr)
#print(type(pop_arr[0]))
income_arr = list(map(int, income_arr))
print(income_arr)
final_income=[]
final_area=[]
for i in range(len(income_arr)):
	if(income_arr[i]!=0):
		final_income.append(income_arr[i])
		final_area.append(area[i])

min_val=min(final_income)
max_val=max(final_income)
#print("min max val")
#print(min_val,max_val)

Data=[['Areaname','NormalizedIncome']]
j=0
norm_income=[]
for i in final_income:
	#print(i)
	z=float((i-min_val)*1.0/(max_val-min_val))
	norm_income.append(z)
	Data.append([final_area[j],z])
	j+=1

with open('../CountyData/IncomeNormalized2009.csv', 'w') as csvFile:
    	writer = csv.writer(csvFile)
    	writer.writerows(Data)