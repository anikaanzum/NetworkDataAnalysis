import sys
import xlrd
import csv
import pandas
import os
import glob
import os.path
import subprocess
import json
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
	

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
	#Tag='Median_Income'
	
	pop=[]
	area=[]
	for i in header:
		if(Tag==i):
			
			#print("Found")
			with open(path) as f:
				reader = csv.DictReader(f, delimiter=',')
				for row in reader:
					pop.append(row[Tag])
					#area.append(row['Areaname'])
		
	return pop


my_path = os.path.abspath(os.path.dirname(__file__))

path = os.path.join(my_path, "CensusData/CountyData/")

extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('*.{}'.format(extension))]

file_name='NormalizedData.csv'
path = os.path.join(path, file_name)

Tag='pop_norm'
pop=get_csv_info(path,Tag)

Tag='income_norm'
income=get_csv_info(path,Tag)
#print(len(income_arr))

Tag='edu_norm'
edu=get_csv_info(path,Tag)
#print(len(edu_arr))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x=pop[:]
y=income[:]
z=edu[:]
x = map(float,x)
y = map(float,y)
z = map(float,z)
ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('Population')
ax.set_ylabel('Income')
ax.set_zlabel('Education')

plt.show()
