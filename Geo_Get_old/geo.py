import json
from py2neo import Node, Relationship, Graph, authenticate
import random, string
#(give your  "localhost/neo4j username/ neo4j password")
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")

with open('geophysicaldata.json') as data_file:
    geodata = json.load(data_file)
name1=''
name2=''

def help1(par):
	global name1
	name1=par

def help2(par):
	global name2
	name2=par




def printd(d):
	continents = ["Asia","Oceania","Europe","","Africa","Americas"]
	for cntnt_k, cntnt_v in d.items():
		if isinstance(cntnt_v, dict):
			if cntnt_k in continents:
				cntnt= cntnt_k
				cntnt1=cntnt
				cntnt = graph.merge_one("Continent", "Name",cntnt1 )
				help1(cntnt)
				printd(cntnt_v)
			if cntnt_k not in continents:
				cntry= cntnt_k
				cntry1=cntry
				cntry = graph.merge_one("Country", "Name",cntry1 )
				graph.create_unique(Relationship(cntry, "part_of", name1))
				help2(cntry)				
				printd(cntnt_v)
		elif isinstance(cntnt_v, list):
			tx=graph.cypher.begin()			
			for val in cntnt_v:
				cty= val
				cty1=cty
				cty = tx.graph.merge_one("City", "Name",cty1 )
				tx.graph.create_unique(Relationship(cty, "located_in", name2))
			tx.commit()


printd(geodata)

