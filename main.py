import subprocess
process = subprocess.Popen(['python', 'xlsTocsv.py'], stdout=subprocess.PIPE)
out, err = process.communicate()
process = subprocess.Popen(['python', 'csvtoDB.py'], stdout=subprocess.PIPE)
out, err = process.communicate()

print(out)