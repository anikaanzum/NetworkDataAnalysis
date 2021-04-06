import csv
data=[]
filename='INC01.csv'
with open(filename) as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        data.append(row)
        
print(data)    
print(data[0])
header=data[0]
new_header=[]
delete_index=[]
print("len of header=",len(header))
for i in range(len(header)):
    if(header[i].find("F")==-1 and header[i].find("N1")==-1 and header[i].find("N2")==-1):
        new_header.append(header[i])
    else:    
        delete_index.append(i)        
print(new_header)     
print(len(new_header)) 
print(delete_index)
''
j=len(delete_index)-1
while(j>=0):
    k=delete_index[j]
    for i in range(len(data)):
        data[i].pop(k)
    j=j-1


with open('edited_'+filename, 'w') as csvFile:
    writer = csv.writer(csvFile,lineterminator='\n')
    writer.writerows(data)
       