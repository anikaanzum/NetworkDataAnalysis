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
	Tag='Total_Population'
	
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
file_name='population_county.csv'
path = os.path.join(path, file_name)
#print(path)
Tag=['Total_Population']
pop_arr,area=get_csv_info(path,Tag)

pop_arr = list(map(int, pop_arr))
#print(pop_arr)
final_pop=[]
final_area=[]
#print(len(pop_arr))
for i in range(len(pop_arr)):
	if(pop_arr[i]!=0):
		final_pop.append(pop_arr[i])
		final_area.append(area[i])
min_val=min(final_pop)
max_val=max(final_pop)
#print("min max val")
#print(min_val,max_val)
#print(len(final_pop))
norm_pop=[]
j=0
Data=[['Areaname','NormalizedPopulation']]
for i in final_pop:
	#print(i)
	z=float((i-min_val)*1.0/(max_val-min_val))
	norm_pop.append(z)
	Data.append([final_area[j],z])
	j+=1
with open('../CountyData/PopulationNormalized2009.csv', 'w') as csvFile:
    	writer = csv.writer(csvFile)
    	writer.writerows(Data)
