import csv
import subprocess
filename='/home/anika/Desktop/IndependentStudy/NetworkDataAnalysis/sample.csv'
data=[]
with open(filename) as csvfile:
   readCSV = csv.reader(csvfile)
   for row in readCSV:
      data.append(row)
   print(data)
print(len(data))
for i in range(len(data)):
	if(i >0):
		lat=data[i][0]
		longi=data[i][1]
		print(lat,longi)
		s = subprocess.check_output("python3 county_latlong.py "+str(lat)+" "+str(longi),shell=True)
		#s = subprocess.check_output("python3 county_latlong.py ",lat,longi)
		
		print(s)