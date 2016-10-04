import json
import os.path
import csv

from py2neo import Node, Relationship, Graph, authenticate
from datetime import datetime
startTime = datetime.now()


authenticate("localhost:7474", "neo4j", "scibase")
graph = Graph("http://localhost:7474/db/data")

def continent(temp):
	with open('InstituteCountryContinent.csv') as journal_file:
				i_name = csv.reader(journal_file)
				for row in i_name:
					if (temp == row[1].lower()):
						ct = row[2].lower()
						tx = graph.begin()
						ctc = Node("Country",Name=temp)
						graph.merge(ctc)
						cntnt = Node("Continent",Name=ct)
						graph.merge(cntnt)
						graph.merge(Relationship(ctc, "IS_PRESENT_IN", cntnt))
						tx.commit()

	


# Change the value of directory to the path where data to be pushed is stored
path = []
directory = '/home/sourav/Documents/Temp_codes/Finalized_structure'
for filename in os.listdir(directory):
	if filename.endswith("JDIQ.json"):
		x = os.path.join(directory, filename)
		path.append(x)
#print path
		
count = 0
for journals in path:
	
	with open(journals) as data_file:
		json1 = json.load(data_file)
		count += 1
		#print json1.items()
		print(count)


#with open('TAP.json') as data_file:
#	json1 = json.load(data_file)   

#for better clarity add print statement to check each key and value pair
		
		for key,value in json1.items():
			print(key)
			j=Node("Journal",Acronymn=key)
			graph.merge(j)
			
			cnt=0
			for key_1,value_1 in value.items():
				if key_1 == 'ISSN':	
					#print value_1		
					j[key_1] = value_1
					j.push()				
				elif (key_1 == 'Volumes'):
					for key_2,value_2 in value_1.items():
						for key_3,value_3 in value_2.items():
								value_d=value_3['date']
								if value_d['year'] is not None:
									y = value_d['year']									
								if value_d['month'] is not None:
			 						m = value_d['month']
#Article  information

								value_4=value_3['articles']
								tx = graph.begin()
								#print value_4.items()
								for key_5,value_5 in value_4.items():						
										if value_5['title'] is not None:
											cnt+=1
											print(cnt)
											var = value_5['title']
											print(var)											
											ar=Node("Article",Title=var)
											tx.merge(ar)
											ar['Year'] = y
											print(y)
											ar['Month'] = m
											print(m)
											ar.push()
											tx.merge(Relationship(j, "CONTAINS", ar))
											print("Check 1")
									
											if value_5['doi'] is not None:
												x = value_5['doi']
												ar['DOI'] = x		
												ar.push()
#Cited Author Details							
												print("Check 2")						

											if value_5['citations'] is not None:
												for ele in value_5['citations']:
													x = ele['Name'].lower()
													a1 = Node("Cited Author",Name=x)
													print("Check 3")
													tx.merge(a1);
													tx.merge(Relationship(ar, "CITED_BY", a1))
													
													if ele['Country'] is not None:
														z = ele['Country'] 
														continent(z)
														ac = Node("Country",Name=z)
														print("Check 4")
														tx.merge(ac)
														tx.merge(Relationship(a1, "CITED_LOCATED_IN", ac))
														
#Article's Author Details 

											if value_5['authors'] is not None:
												for auth in value_5['authors']:
													affd=value_5['affiliation_data']
													if auth['name'] is not None:
															var1 = auth['name']							                  
															au=Node("Author",Name=var1,Link=auth['link'])
															print("Check 5")
															tx.merge(au)
															tx.merge(Relationship(ar, "AUTHORED_BY", au))
															

															for ele in affd:
																if ele['Name'] == auth['name']:

																	if ele['university'] is not None:

																		inst=Node("Institute",Name=ele['university'])
																		tx.merge(inst)
																		tx.merge(Relationship(au, "AFFILIATED_TO", inst))
																		print("Check 6")
																	if ele['country'] is not None:
																		c = ele['country']
																		continent (c.lower())
																		country=Node("Country",Name=c)
																		tx.merge(country)
																		tx.merge(Relationship(inst, "LOCATED_IN", country))
																		tx.merge(Relationship(au, "PART_OF", country))
																		print("Check 7")
								tx.commit()


tx=graph.begin()
#Creating Publisher's Information
with open('journal_publisher_relation (2).csv') as journal_file:
	publisher_name = csv.reader(journal_file)
	for row in publisher_name:
		#print row[4]
		if key == row[4]:
		#	print row[1]
			var = row[3].lower()
			#continent(var)
			pc= Node("Country",Name=var)
			tx.merge(pc)
			p=Node("Publisher",Name=row[1])
			tx.merge(p)					
			tx.merge(Relationship(j, "PUBLISHED_BY", p));
			tx.merge(Relationship(p, "PUBLISHER_LOCATED_IN", pc))
tx.commit()
		

#Adding Journal Parameters 									
					
with open('self citation list (1)_good.csv') as journal_file:
	journal_name = csv.reader(journal_file)
	for row in journal_name:
		if (key == row[1]):
				j['Name'] = row[0] 
				j['Self citation'] = row[2]
				j['Total citation'] = row[3]
				j['NLIQ'] = row[4]
				j['ICR'] = row[5]
				j['OCQ'] = row[6]
				j['SNIP'] = row[7]
				j.push()
				#print(key)

print(datetime.now() - startTime)	
