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
		
	return area,pop
		
my_path = os.path.abspath(os.path.dirname(__file__))

path = os.path.join(my_path, "CensusData/CountyData/")

extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('*.{}'.format(extension))]

file_name='PopulationNormalized2009.csv'
path = os.path.join(path, file_name)

Tag='NormalizedPopulation'
pop_area,pop_arr=get_csv_info(path,Tag)

path = os.path.join(my_path, "CensusData/CountyData/")
file_name='IncomeNormalized2009.csv'
path = os.path.join(path, file_name)

Tag='NormalizedIncome'
income_area,income_arr=get_csv_info(path,Tag)

path = os.path.join(my_path, "CensusData/CountyData/")
file_name='EducationNormalized2009.csv'
path = os.path.join(path, file_name)

Tag='NormalizedEducation'
edu_area,edu_arr=get_csv_info(path,Tag)


data=[['area','pop_norm','income_norm','edu_norm']]

for i in range(len(pop_area)):
	incomeTemp=-1
	eduTemp=-1
	for j in range(len(income_area)):
		if(income_area[j]==pop_area[i]):
			incomeTemp=income_arr[j]
			break
	for j in range(len(edu_area)):
		if(edu_area[j]==pop_area[i]):
			eduTemp=edu_arr[j]
			break
	if(incomeTemp!=-1 and eduTemp!=-1):
		data.append([pop_area[i],pop_arr[i],incomeTemp,eduTemp])
		
	



with open('../CountyData/NormalizedData.csv', 'w') as csvFile:
    	writer = csv.writer(csvFile)
    	writer.writerows(data)




