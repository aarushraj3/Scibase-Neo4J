from py2neo import Node, Relationship, Graph, authenticate
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")


def get_aut_by_res_country():
	x=input("Enter country name:")
	q1="MATCH (n:Author)-[:Lives_in]->(Country {name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)



get_aut_by_res_country()
