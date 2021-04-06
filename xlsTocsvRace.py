import sys
import xlrd
import csv
import pandas
import os
import glob
import os.path

def load_xls_folder():
    path = 'CensusData/Race'
    extension = 'xls'
    os.chdir(path)
    result = [i for i in glob.glob('*.{}'.format(extension))]
    print(result)
    return result    

def load_csv_intoArray():
	my_path = os.path.abspath(os.path.dirname(__file__))
	path = os.path.join(my_path, "../RaceData/")
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
        path = os.path.join(my_path, "../RaceData/"+filename+j+".csv")
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
	#print(header)
	#Tag='POP150210D'
	print(Tag)
	print(path)
	FileList=[]
	cnt=0
	data=[]
	Area=[]
	male_pop=[]
	for i in header:
		if(path=='/home/anika/Desktop/IndependentStudy/NetworkDataAnalysis/CensusData/RaceData/Sheet3.csv'):
			print(i)
			print(Tag)
		if(str(Tag)==str(i)):
			print("Found")
			with open(path) as f:
				reader = csv.DictReader(f, delimiter=',')
				for row in reader:
					Area.append(row['Areaname'])
					male_pop.append(row[Tag])
		cnt+=1
	return Area,male_pop
		
def main_func():
    all_xlsfiles=load_xls_folder()
    #print(all_xlsfiles)
    for i in all_xlsfiles:
        xlsTocsv_convert(i)
    
    AreaW=[]
    AreaB=[]
    WhiteInfo=[]
    blackInfo=[]
    csvFiles=load_csv_intoArray()
    for file1 in csvFiles:
    	my_path = os.path.abspath(os.path.dirname(__file__))
    	#print(my_path)
    	path = os.path.join(my_path, file1)
    	Tag=['RHI125209D', 'RHI225209D']
    	area1,white=get_csv_info(path,Tag[0])
    	area2,black=get_csv_info(path,Tag[1])
    	print(area1)
    	print(black)
    	if(len(white)>0):
    		AreaW=area1[:]
    		WhiteInfo=white[:]
    	if(len(black)>0):
    		AreaB=area2[:]
    		blackInfo=black[:]
    data=[]
    i=0
    print(AreaW)
    print(WhiteInfo)
    print(AreaB)
    print(blackInfo)
    while(i<len(AreaW)):
    	j=0
    	while(j<len(AreaB)):
    		if(AreaW[i]==AreaB[j]):
    			data.append([AreaW[i],WhiteInfo[i],blackInfo[j]])
    			break
    		j+=1
    	i+=1
    #print(data)
    with open('../OutputINC/RaceByCounty2009.csv', 'w') as csvFile:
    	writer = csv.writer(csvFile)
    	writer.writerows(data)
main_func()