import sys
import xlrd
import csv
import pandas
import os
import glob
import os.path

def remove_state_pop():
	my_path = os.path.abspath(os.path.dirname(__file__))

	path = os.path.join(my_path, "CensusData/OutputINC/")

	extension = 'csv'

	file_name='PopulationByCounty2009.csv'
	path = os.path.join(path, file_name)
	print(path)
	data=read_csv(path)
	print(data)

	with open('CensusData/CountyData/population_county.csv', 'w') as csvFile:
    		writer = csv.writer(csvFile)
    		writer.writerows(data)

def remove_state_income():
	my_path = os.path.abspath(os.path.dirname(__file__))

	path = os.path.join(my_path, "CensusData/OutputINC/")

	extension = 'csv'

	file_name='IncomeByCounty2009.csv'
	path = os.path.join(path, file_name)
	print(path)
	data=read_csv(path)
	print(data)

	with open('CensusData/CountyData/income_county.csv', 'w') as csvFile:
    		writer = csv.writer(csvFile)
    		writer.writerows(data)


def remove_state_edu():
	my_path = os.path.abspath(os.path.dirname(__file__))

	path = os.path.join(my_path, "CensusData/OutputINC/")

	extension = 'csv'

	file_name='EduByCounty2009.csv'
	path = os.path.join(path, file_name)
	print(path)
	data=read_csv(path)
	print(data)

	with open('CensusData/CountyData/edu_county.csv', 'w') as csvFile:
    		writer = csv.writer(csvFile)
    		writer.writerows(data)





def read_csv(filename):
    data=[]
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile)
        for row in readCSV:
        		area=row[0]
        		coma=','
        		if(coma in area or area=='Areaname'):
        			data.append(row)
    #print(data)
    #header=data[0]   
    #print(header) 
    return data

remove_state_pop()		
remove_state_income()		
remove_state_edu()		