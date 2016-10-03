from py2neo import Node, Relationship, Graph, authenticate
import string
import random
from titlecase import titlecase
import json

with open('geophysicaldata.json') as data_file:
    geodata = json.load(data_file)

#(give your  "localhost/neo4j userName/ neo4j password")
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")


def Author_Generator(size=6, chars=string.ascii_uppercase):
	return titlecase(''.join(random.choice(chars) for _ in range(size))) + " " + titlecase(''.join(random.choice(chars) for _ in range(size))) 
#for i in range(0,5):
#	Author_Generator()


def Journal_Generator(size=8, chars=string.ascii_uppercase):
	return titlecase(''.join(random.choice(chars) for _ in range(size)))
#for i in range(0,5):
#	Journal_Generator()


def Publisher_Generator(size=8, chars=string.ascii_uppercase):
	return titlecase(''.join(random.choice(chars) for _ in range(size)))	
#for i in range(0,5):
#	Publisher_Generator()


def Article_Generator(size=5, chars=string.ascii_uppercase):
	return titlecase(''.join(random.choice(chars) for _ in range(size)))	
#for i in range(0,5):
#	Article_Generator()


def Domain_Generator(size=7, chars=string.ascii_uppercase):
	return titlecase(''.join(random.choice(chars) for _ in range(size)))	
#for i in range(0,5):
#	Domain_Generator()


def Affiliation_Generator(size=10, chars=string.ascii_uppercase):
	return titlecase(''.join(random.choice(chars) for _ in range(size)))	
#for i in range(0,5):
#	Affiliation_Generator()

def Article_DOI(size=2, chars=string.digits):
	return ''.join(random.choice(chars) for _ in range(size)) + "." + ''.join(random.choice(chars) for _ in range(size)) + "." + ''.join(random.choice(chars) for _ in range(4))

def journal_issn(size=4, chars=string.digits):
	return ''.join(random.choice(chars) for _ in range(size)) + "-" + ''.join(random.choice(chars) for _ in range(size)) 






cities = []
country = []

def printd(d):
	continents = ["Asia","Oceania","Europe","","Africa","Americas"]
	for cntnt_k, cntnt_v in d.items():
		if isinstance(cntnt_v, dict):
			if cntnt_k in continents:
				printd(cntnt_v)
			if cntnt_k not in continents:
				country.append(cntnt_k)
				printd(cntnt_v)
		elif isinstance(cntnt_v, list):
			for val in cntnt_v:
				cities.append(val)

	r1 = random.randint(0,len(cities)-1)
	r2 = random.randint(0,len(country)-1)
	return (cities[r1],country[r2])



for i in range(3):
	

	cty,x = printd(geodata)
	cty1 = cty
	cty = graph.merge_one("City", "Name",cty1 )


	x,cntry = printd(geodata)
	cntry1 = cntry
	cntry = graph.merge_one("Country", "Name",cntry1 )


	ctyo,x = printd(geodata)
	ctyo1 = ctyo
	ctyo = graph.merge_one("City", "Name",ctyo1 )



	a = Author_Generator()
	a1=a
	a = graph.merge_one("Author", "Name",a1 )
	


	ar= Article_Generator()
	ar2 = Article_DOI()
	ar1=ar
	ar = graph.merge_one("Article", "Name",ar1 )
	ar.properties["DOI"]=ar2
	ar.push()

	j= Journal_Generator() 
	j1=j


	j2= journal_issn()
	j = graph.merge_one("Journal", "Name",j1 ) 
	j.properties["ISSN"]=j2
	j.push()



	x,cntryp = printd(geodata)
	cntryp1 = cntryp
	cntryp = graph.merge_one("Country", "Name",cntryp1 )


	x,cntryj = printd(geodata)
	cntryj1 = cntryj
	cntryj = graph.merge_one("Country", "Name",cntryj1 )



	d= Domain_Generator()
	d1=d
	d = graph.merge_one("Domain", "Name",d1 )



	p= Publisher_Generator()
	p1=p
	p = graph.merge_one("Publisher", "Name",p1 )

	af= Affiliation_Generator()
	af1=af
	af = graph.merge_one("Affiliation", "Name",af1 ) 

	graph.create_unique(Relationship(a, "lives_in", cty))
	graph.create_unique(Relationship(a, "affiliated_to", af))
	graph.create_unique(Relationship(af, "located_in", cty))
	graph.create_unique(Relationship(ar, "authored_by", a))
	graph.create_unique(Relationship(j, "contains", ar))
	graph.create_unique(Relationship(j, "published_by", p))
	graph.create_unique(Relationship(j, "published_in", cntryj))
	graph.create_unique(Relationship(j, "belongs_to", d))
	graph.create_unique(Relationship(a, "native_of", ctyo))
	graph.create_unique(Relationship(p, "based_in", cntryp))
