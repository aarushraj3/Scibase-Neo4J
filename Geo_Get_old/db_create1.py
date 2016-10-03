import string
import random
from titlecase import titlecase
from py2neo import Node, Relationship, Graph, authenticate
#(give your  "localhost/neo4j username/ neo4j password")
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")


def author_generator(size=6, chars=string.ascii_uppercase):
	return titlecase(''.join(random.choice(chars) for _ in range(size))) + " " + titlecase(''.join(random.choice(chars) for _ in range(size))) 

def Article_DOI(size=2, chars=string.digits):
	return ''.join(random.choice(chars) for _ in range(size)) + "." + ''.join(random.choice(chars) for _ in range(size)) + "." + ''.join(random.choice(chars) for _ in range(4))

def journal_issn(size=4, chars=string.digits):
	return ''.join(random.choice(chars) for _ in range(size)) + "-" + ''.join(random.choice(chars) for _ in range(size)) 

def journal_generator(size=8, chars=string.ascii_uppercase):
	return titlecase(''.join(random.choice(chars) for _ in range(size)))


def Publisher_Generator(size=8, chars=string.ascii_uppercase):
	return titlecase(''.join(random.choice(chars) for _ in range(size)))

def Domain_Generator(size=7, chars=string.ascii_uppercase):
	return titlecase(''.join(random.choice(chars) for _ in range(size)))	

def Article_Generator(size=5, chars=string.ascii_uppercase):
	return titlecase(''.join(random.choice(chars) for _ in range(size)))

def Affiliation_Generator(size=10, chars=string.ascii_uppercase):
	return titlecase(''.join(random.choice(chars) for _ in range(size)))


for i in range(2):
	print "Enter author name:"	
	a=author_generator()
	a1=a
	a = graph.merge_one("Author", "name",a1 )
	



	ct= input ("Enter Continent name:")
	ct1=ct
	ct = graph.merge_one("Continent", "name",ct1 ) 




	cy= input ("Enter Country name:")
	cy1=cy
	cy = graph.merge_one("Country", "name",cy1 )
	
	co= input ("Enter Origin Country name:")
	co1=co
	co = graph.merge_one("Country", "name",co1 )


	
	print "Enter Article:"
	ar1=Article_Generator()
	ar = graph.merge_one("Article", "name",ar1 )
	print "Enter article DOI:"
	ar2=Article_DOI()
	ar.properties["DOI"]=ar2


	print "Enter Journal name:"
	j1=journal_generator()
	print "Enter Journal ISSN:"
	j2=journal_issn()
	j = graph.merge_one("Journal", "name",j1 ) 
	j.properties["ISSN"]=j2




	print "Enter Domain name:"
	d1=Domain_Generator()
	d = graph.merge_one("Domain", "name",d1 )




	print "Enter Publisher name:"
	p1= Publisher_Generator()
	p = graph.merge_one("Publisher", "name",p1 )

	cp= input ("Enter Country of Publisher:")
	cp1=cp
	cp = graph.merge_one("Country", "name",cp1 )

	cp2= input ("Enter Country of Journal:")
	cp3=cp2
	cp2 = graph.merge_one("Country", "name",cp3 )
	



	print ("Enter Affiliation(Institute) name:")
	af1=Affiliation_Generator()
	af = graph.merge_one("Affiliation", "name",af1 ) 
	cf= input ("Enter Country of Institute:")
	cf1=cf
	cf = graph.merge_one("Country", "name",cf1 )
	cf2= input ("Enter Continent of Institute:")
	cf3=cf2
	cf2 = graph.merge_one("Continent", "name",cf3 )






	graph.create_unique(Relationship(a, "Lives_in", cy))
	graph.create_unique(Relationship(cy, "Part_of", ct))

	graph.create_unique(Relationship(a, "Affiliated_to", af))
	graph.create_unique(Relationship(af, "Located_in", cf))

	graph.create_unique(Relationship(ar, "Authored_by", a))
	graph.create_unique(Relationship(j, "Contains", ar))

	graph.create_unique(Relationship(j, "Published_by", p))
	graph.create_unique(Relationship(j, "Belongs_to", d))

	graph.create_unique(Relationship(cf, "Part_of", cf2))
	graph.create_unique(Relationship(a, "Computed", d))

	graph.create_unique(Relationship(af, "Computed", d))
	graph.create_unique(Relationship(cf, "Computed", d))
	
	graph.create_unique(Relationship(cf2, "Computed", d))	
	graph.create_unique(Relationship(j, "Computed", d))

	graph.create_unique(Relationship(ar, "Computed", d))
	graph.create_unique(Relationship(j, "Published_in", cp2))

	graph.create_unique(Relationship(p, "Based_in", cp))
	graph.create_unique(Relationship(a, "Native_of", co))



#MERGE (u1:User {name: "u1"})-[:FRIEND]-(u2:User {name:"u2"})
