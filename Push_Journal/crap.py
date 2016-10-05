import json
import os.path
import csv

#from py2neo import Node, Relationship, Graph, authenticate

#authenticate("localhost:7474", "neo4j", "scibase")
#graph = Graph("http://localhost:7474/db/data")
#from datetime import datetime


path = []
directory = '/home/sourav/Documents/Temp_codes/Push_Journal/Journals'
for filename in os.listdir(directory):
	if filename.endswith(".json"):
		x = os.path.join(directory, filename)
		path.append(x)
#print(path)


for journals in path:
	
	with open(journals) as data_file:
		json1 = json.load(data_file)


		for key,value in json1.items():
			print(key)
			with open('journal_publisher_relation (2).csv') as journal_file:
				publisher_name = csv.reader(journal_file)
				for row in publisher_name:
					#print row[4]
					if key == row[4]:
						value['Publisher']=row[1]
						value['Publisher City']=row[2]
						value['Publisher Country']=row[3]

			for key_1,value_1 in value.items():
				if key_1 != 'Volumes':
					print(key_1,value_1)
















			'''vol=value['Volumes']
			for key_1,value_1 in vol.items():
				#print(key_1)
				for key_2,value_2 in value_1.items():
					#print(key_2)
					articles=value_2['articles']
					for key_3,value_3 in articles.items():
						print(key_3)'''

























	'''print(journals)
	with open(journals,'w') as data_file:
		json.dump(json1,data_file)#uncomment to dump the changes to the json file'''










'''with open('ScholasticIndices.csv') as journal_file:
	journal_name = csv.reader(journal_file)
	for row in journal_name:
		if (key == row[1]):
				value['Name'] = row[0] 
				value['Self citation'] = row[2]
				value['Total citation'] = row[3]
				value['NLIQ'] = row[4]
				value['ICR'] = row[5]
				value['OCQ'] = row[6]
				value['SNIP'] = row[7]
for key_1,value_1 in value.items():
	if key_1 != 'Volumes':
		print(key_1,value_1)'''





'''						affd=value_3['affiliation_data']
						for auth in  value_3['authors']:
							for ele in affd:
								if auth['name'] == ele['Name']:
									if 'city' in ele.keys():
										auth['city'] = ele['city']
									else:
										auth['city']=None
									auth['country'] = ele['country']
									auth['university'] = ele['university']
							if not affd:
								print("Empty")
								auth['city']=None
								auth['country'] = None
								auth['university'] = None
							#print(auth)'''