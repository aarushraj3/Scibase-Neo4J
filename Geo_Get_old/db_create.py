from py2neo import Node, Relationship, Graph, authenticate
#(give your  "localhost/neo4j username/ neo4j password")
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")



for i in range(3):
	a= input("Enter author name:")
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


	
	ar= input("Enter article name:")
	ar2=input("Enter article DOI:")
	ar1=ar
	ar = graph.merge_one("Article", "name",ar1 )
	ar.properties["DOI"]=ar2


	

	j= input ("Enter Journal name:")
	j1=j
	j2=input ("Enter Journal ISSN:")
	j = graph.merge_one("Journal", "name",j1 ) 
	j.properties["ISSN"]=j2




	d= input ("Enter Domain name:")
	d1=d
	d = graph.merge_one("Domain", "name",d1 )




	p= input("Enter Publisher name:")
	p1=p
	p = graph.merge_one("Publisher", "name",p1 )

	cp= input ("Enter Country of Publisher:")
	cp1=cp
	cp = graph.merge_one("Country", "name",cp1 )

	cp2= input ("Enter Country of Journal:")
	cp3=cp2
	cp2 = graph.merge_one("Country", "name",cp3 )
	



	af= input ("Enter Affiliation(Institute) name:")
	af1=af
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
