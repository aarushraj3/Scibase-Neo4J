from py2neo import Node, Relationship, Graph, authenticate
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")


def get_a_by_continent():
	x=input("Enter contienent name:")
	q1="MATCH (n:Article)-[:Authored_by]->(Author)-[:Affiliated_to]->(Affiliation)-[:Located_in]->(Country)-[:Part_of]->(Continent {name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)
	

get_a_by_continent()


