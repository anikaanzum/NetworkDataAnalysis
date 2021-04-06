import sys
import xlrd
import csv
import pandas
import os
import glob
import os.path

def load_xls_folder():
    path = 'CensusData/EDU'
    extension = 'xls'
    os.chdir(path)
    result = [i for i in glob.glob('*.{}'.format(extension))]
    print(result)
    return result    

def load_csv_intoArray():
	my_path = os.path.abspath(os.path.dirname(__file__))
	path = os.path.join(my_path, "../EDUData/")
	extension = 'csv'
	os.chdir(path)
	result = [i for i in glob.glob('*.{}'.format(extension))]
	#print(result)
	return result    
        
    
            
    
    
def xlsTocsv_convert(filename):
    workBook = xlrd.open_workbook(filename)#reading the excel file
    sheet_names = workBook.sheet_names()
    #print("sheet names=",sheet_names)
    list_sheet = []
    lenth = len(sheet_names)
    for i in range(lenth):
        sheet =  workBook.sheet_by_name(sheet_names[i])
        list_sheet.append(sheet)
        total_col = list_sheet[i].ncols
        #print("total col=",total_col)
    #print("list sheet=",list_sheet)   
    
    
    
    for i in range(len(sheet_names)):
        j=sheet_names[i]
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../EDUData/"+filename+j+".csv")
        yourcsvFile = open(path, 'w')
        wr = csv.writer(yourcsvFile, quoting=csv.QUOTE_ALL)
        wr = csv.writer(yourcsvFile,lineterminator='\n')
        for rownum in range(list_sheet[i].nrows):
            wr.writerow(list_sheet[i].row_values(rownum))
               

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
	print(header)
	edu=[]
	area=[]
	for i in header:
		print("OK"+str(i))
		if(Tag==str(i)):
			print("Found")
			with open(path) as f:
				reader = csv.DictReader(f, delimiter=',')
				for row in reader:
					edu.append(row[Tag])
					area.append(row['Area_name'])
	return edu,area
		
	
		
def main_func():
    all_xlsfiles=load_xls_folder()
   
    for i in all_xlsfiles:
        xlsTocsv_convert(i)
    
    csvFiles=load_csv_intoArray()
    print(csvFiles)
    data=[['Areaname','Bachelors']]
    Tag='EDU690209D'
    for file1 in csvFiles:
    	my_path = os.path.abspath(os.path.dirname(__file__))
    	#print(my_path)
    	path = os.path.join(my_path, file1)
    	print(path)
    	edu,area=get_csv_info(path,Tag)
    	
    	for i in range(len(edu)):
    		data.append([area[i],edu[i]])
    
    	
    
    with open('../OutputINC/EduByCounty2009.csv', 'w') as csvFile:
    	
    	writer = csv.writer(csvFile)
    	writer.writerows(data)
    	
main_func()