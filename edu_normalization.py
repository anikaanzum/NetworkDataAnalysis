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
	Tag='Bachelors'
	
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
file_name='edu_county.csv'
path = os.path.join(path, file_name)
#print(path)
Tag=['Bachelors']
edu_arr,area=get_csv_info(path,Tag)
#print(type(edu_arr[3]))
#print(edu_arr)

edu_arr = list(map(float, edu_arr))
#print(edu_arr)

final_edu=[]
final_area=[]
for i in range(len(edu_arr)):
	if(edu_arr[i]!=0):
		final_edu.append(edu_arr[i])
		final_area.append(area[i])
#print(final_edu)
min_val=min(final_edu)
max_val=max(final_edu)
#print("min max val")
#print(min_val,max_val)
j=0
Data=[['Areaname','NormalizedEducation']]
norm_edu=[]
for i in final_edu:
	#print(i)
	z=float((i-min_val)*1.0/(max_val-min_val))
	norm_edu.append(z)
	Data.append([final_area[j],z])
	j+=1
with open('../CountyData/EducationNormalized2009.csv', 'w') as csvFile:
    	writer = csv.writer(csvFile)
    	writer.writerows(Data)

