from py2neo import Node,Relationship,authenticate,Graph

authenticate("localhost:7474", "neo4j", "scibase")
graph = Graph("http://localhost:7474/db/data/")





def get_publisher_by_domain():
	x= input('Enter Domain name')
	s="MATCH (n:Publisher)<-[:Published_by]-(:Journal)-[:Belongs_to]->(Domain {name:'"+x+"'}) RETURN n.name"
	
	res=graph.cypher.execute(s)
	
	print (res)




get_publisher_by_domain()

