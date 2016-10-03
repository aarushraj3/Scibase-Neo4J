from py2neo import Node, Relationship, Graph, authenticate
#(give your  "localhost/neo4j username/ neo4j password")
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")



def get_publishers():

	print "Function name:Get_publisher\nGives list of all publishers\n"	
	q1="MATCH (n:Publisher) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)
	

get_publishers()
