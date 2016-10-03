
from py2neo import Node,Relationship,authenticate,Graph

authenticate("localhost:7474", "neo4j", "scibase")
graph = Graph("http://localhost:7474/db/data/")




def get_affiliation_by_Domain():
	x= input('Enter Domain name')
	s="MATCH (Domain{name:'"+x+"'})<-[:Belongs_to]-(Journal)-[:Contains]->(Article)-[:Authored_by]->(Author)-[:Affiliated_to]->(n:Affiliation) RETURN n.name"
        res=graph.cypher.execute(s)
        print (res)


get_affiliation_by_Domain()
