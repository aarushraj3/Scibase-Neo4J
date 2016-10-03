from py2neo import Node, Relationship, Graph, authenticate
#(give your  "localhost/neo4j username/ neo4j password")
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")





def get_continents():

	print "Function name:Get_continents\nGives the list of all continents\n"
	
	q1="MATCH (n:Continent) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)
	

get_continents()
