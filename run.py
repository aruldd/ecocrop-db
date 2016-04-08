import requests,csv
from bs4 import BeautifulSoup
header=[2,4,6,8,9,11,13,26,29,34,37,42,45,50,53,58,61,66,69,77,79,81,83,85,87,89,97,99,102,103,104,105,106]
data=[0,3,5,7,10,12,27,28,30,31,32,33,35,36,38,39,40,41,43,44,46,47,48,49,51,52,54,55,56,57,59,60,62,63,64,65,67,68,70,71,72,73,78,80,82,84,86,88,90,91,92,98,100,101,107,108,109,110,111,112]

def chk(no):
	print(no)
	url = r"http://ecocrop.fao.org/ecocrop/srv/en/dataSheet?id="+str(no)
	soup = BeautifulSoup(requests.post(url).text,"lxml")
	txt = [x.string for x in soup.find_all(['h2','td','th'])]
	txt = [txt[i] for i in data]
	txt.insert(0, no)
	return txt
final_data = []
ids = []
error = []
with open('index.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        ids.append(int(row[0]))

for iD in ids:	
	try:
		final_data.append(chk(iD))
		print("done..")
	except:
		error.append(iD)
		print("error")
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(final_data)	
try:
	with open('error.csv', 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(error)
except:
	pass
