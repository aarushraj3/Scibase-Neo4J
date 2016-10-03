from py2neo import Node, Relationship, Graph, authenticate
authenticate("localhost:7474","neo4j","suraj1012")
graph=Graph("http://localhost:7474/db/data")


def get_authors_by_affiliation(x):

	print "Function name:Get_authors_by_affiliation\nThis Gives all the authors of the affiliation given as input"
	print "\nAffiliation:\n",x
	q="MATCH (n:Author)-[:Affiliated_to]->(Affiliation{name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q)
	print (res)
	
get_authors_by_affiliation("pqr")

