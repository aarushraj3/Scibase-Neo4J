import json
import os
import csv

from py2neo import Node, Relationship, Graph, authenticate

authenticate("localhost:7474", "neo4j", "scibase")
graph = Graph("http://localhost:7474/db/data")
from datetime import datetime


path = []
directory = '/home/sourav/Documents/Temp_codes/Push_Journal/Journals'
for filename in os.listdir(directory):
	if filename.endswith(".json"):
		x = os.path.join(directory, filename)
		path.append(x)
#print(path)


for journals in path:
	startTime = datetime.now()
	with open(journals) as data_file:
		json1 = json.load(data_file)


		for key,value in json1.items():
			print(key)
			print(value['Name'])
			j=Node("Journal",Acronymn=key,Name=value['Name'],NLIQ=value['NLIQ'],ICR=value['ICR'],OCQ=value['OCQ'],SNIP=value['SNIP'],ISSN=value['ISSN'])
			graph.merge(j)
			j['Self Citation'] = value['Self citation']
			j['Total Citation'] = value['Total citation']
			j.push()
			p=Node("Publisher",Name=value['Publisher'])
			#city=Node("City",City=value['Publisher City'])
			country=Node("Country",Name=value['Publisher Country'].lower())
			graph.merge(Relationship(j, "published_by", p))
			graph.merge(Relationship(p, "located_in", country))			
			
			vol=value['Volumes']
			for key_1,value_1 in vol.items():
				#print(key_1)
				for key_2,value_2 in value_1.items():
					#print(key_2)
					tx=graph.begin()
					date=value_2['date']
					month=date['month']
					year=date['year']
					articles=value_2['articles']
					for key_3,value_3 in articles.items():
						print(key_3)
						#tx=graph.begin()
						for key_4,value_4 in value_3.items():
							ar=Node("Article",Title=value_3['title'],Abstract=value_3['abstract'],DOI=value_3['doi'],Month=month,Year=year)
							tx.merge(ar)
							tx.merge(Relationship(j, "contains", ar))
							
							#print(key_4)
							authors=value_3['authors']
							citations=value_3['citations']
							for author in citations:
								ca = Node("Cited Author",Name=author['Name'].lower())
								tx.merge(ca);
								tx.merge(Relationship(ar, "cited_by", ca))
								if author['Country'] is not None:
									#print(author['Country'])
									cac = Node("Country",Name=author['Country'].lower())
									tx.merge(cac)
									tx.merge(Relationship(ca, "cited_located_in",cac))

							for author in authors:
								#print(author)
								a = Node("Author",Name=author['name'].lower(),Link=author['link'])
								tx.merge(a)
								tx.merge(Relationship(ar, "authored_by", a))

								if author['university'] is not None:
									#print(author['university'])
									inst = Node("Institution",Name=author['university'].lower())
									tx.merge(inst)
									tx.merge(Relationship(a, "affiliated_to", inst))


								if author['country'] is not None:
									#print(author['country'])
									cntry = Node("Country",Name=author['country'].lower())
									tx.merge(cntry)
									tx.merge(Relationship(inst, "located_in", cntry))
					tx.commit()
	print(datetime.now() - startTime)
	os.remove(journals)