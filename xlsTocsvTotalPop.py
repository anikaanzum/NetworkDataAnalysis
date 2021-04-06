import sys
import xlrd
import csv
import pandas
import os
import glob
import os.path

def load_xls_folder():
    path = 'CensusData/population'
    extension = 'xls'
    os.chdir(path)
    result = [i for i in glob.glob('*.{}'.format(extension))]
    print(result)
    return result    

def load_csv_intoArray():
	my_path = os.path.abspath(os.path.dirname(__file__))
	path = os.path.join(my_path, "../PopulationData/")
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
        path = os.path.join(my_path, "../PopulationData/"+j+".csv")
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
	#Tag='POP150210D'
	FileList=[]
	cnt=0
	data=[]
	Area=[]
	male_pop=[]
	for i in header:
		if(Tag==i):
			
			#print("Found")
			with open(path) as f:
				reader = csv.DictReader(f, delimiter=',')
				for row in reader:
					Area.append(row['Area_name'])
					male_pop.append(row[Tag])
		cnt+=1
	return Area,male_pop
		
		

		
		
		

def main_func():
    all_xlsfiles=load_xls_folder()
    #print(all_xlsfiles)
    for i in all_xlsfiles:
        xlsTocsv_convert(i)
    
    AreaM=[]
    AreaF=[]
    MaleInfo=[]
    FemaleInfo=[]
    csvFiles=load_csv_intoArray()
    for file1 in csvFiles:
    	my_path = os.path.abspath(os.path.dirname(__file__))
    	#print(my_path)
    	path = os.path.join(my_path, file1)
    	Tag=['POP150210D', 'POP160210D']
    	area1,male=get_csv_info(path,Tag[0])
    	area2,Female=get_csv_info(path,Tag[1])
    	if(len(male)>0):
    		AreaM=area1[:]
    		MaleInfo=male[:]
    	if(len(Female)>0):
    		AreaF=area2[:]
    		FemaleInfo=Female[:]
    data=[]
    i=0
    while(i<len(AreaM)):
    	j=0
    	while(j<len(AreaF)):
    		if(AreaM[i]==AreaF[j]):
    			data.append([AreaM[i],MaleInfo[i],FemaleInfo[j],float(MaleInfo[i])+float(FemaleInfo[j])])
    			break
    		j+=1
    	i+=1
    #print(data)
    with open('../OutputINC/PopulationByCounty2009.csv', 'w') as csvFile:
    	writer = csv.writer(csvFile)
    	writer.writerows(data)
main_func()