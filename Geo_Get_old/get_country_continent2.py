from py2neo import Node, Relationship, Graph, authenticate
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")



def get_country_by_continent(x):

	print "Function name:Get_country_by_continent\nGives all countries of the continent given as input\n"
	#x=input("Enter contienent name:")
	print "\nContinent name:",x
	q1="MATCH (n:Country)-[:Part_of]->(Continent {name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)
	
get_country_by_continent("Asia")

