import json
import os.path
import csv

from py2neo import Node, Relationship, Graph, authenticate

authenticate("localhost:7474", "neo4j", "scibase")
graph = Graph("http://localhost:7474/db/data")

def continent(temp):	
		with open('InstituteCountryContinent.csv') as journal_file:
			i_name = csv.reader(journal_file)
			for row in i_name:
				if (temp == row[1].lower()):
					ct = row[2].lower()
					tx = graph.begin()
					ctc=Node("Country",Name=temp)
					tx.merge(ctc)
					cntnt = Node("Continent",Name=ct)
					
					
					tx.merge(cntnt)
					#tx.merge(pr)
					rel=Relationship(ctc, "IS_PRESENT_IN", cntnt)
					tx.merge(Relationship(ctc, "IS_PRESENT_IN", cntnt))
					tx.commit()
					cntnt['Size']=1234
					cntnt.push()
continent("united states")