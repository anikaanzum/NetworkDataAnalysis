import sys
import xlrd
import csv
import pandas
import os
import glob
import os.path

def load_xls_folder():
    path = 'CensusData/INC'
    extension = 'xls'
    os.chdir(path)
    result = [i for i in glob.glob('*.{}'.format(extension))]
    print(result)
    return result    

def load_csv_intoArray():
	my_path = os.path.abspath(os.path.dirname(__file__))
	path = os.path.join(my_path, "../IncomeData/")
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
        path = os.path.join(my_path, "../IncomeData/"+j+".csv")
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


def CSV_for_filtering(path):
	header=read_csv(path)
	print(header)
	Tag='IPE010209D'
	FileList=[]
	cnt=0
	for i in header:
		if(Tag==i):
			data=[]
			Area=[]
			IPE=[]
			#print("Found")
			with open(path) as f:
				reader = csv.DictReader(f, delimiter=',')
				for row in reader:
					Area.append(row['Areaname'])
					IPE.append(row[Tag])
			Data=[]
			for i in range(len(Area)):
				Data.append([Area[i],IPE[i]])
			with open('../OutputINC/IncomeByCounty2009.csv', 'w') as csvFile:
				writer = csv.writer(csvFile)
				writer.writerows(Data)
		cnt+=1

		
		
		

def main_func():
    all_xlsfiles=load_xls_folder()
    #print(all_xlsfiles)
    for i in all_xlsfiles:
        xlsTocsv_convert(i)
    
    
    csvFiles=load_csv_intoArray()
    for file1 in csvFiles:
    	my_path = os.path.abspath(os.path.dirname(__file__))
    	#print(my_path)
    	path = os.path.join(my_path, file1)
    	CSV_for_filtering(path)
    
    
main_func()