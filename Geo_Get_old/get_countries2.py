from py2neo import Node, Relationship, Graph, authenticate
#(give your  "localhost/neo4j username/ neo4j password")
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")





def get_countries():
	
	print "Function_name:Get_countries"  
	print "Gives the list of all countries\n"
	
	q1="MATCH (n:Country) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)
	

get_countries()
