from py2neo import Node, Relationship, Graph, authenticate
#(give your  "localhost/neo4j username/ neo4j password")
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")

def get_authors():
	
	print "Function_name:Get_author"  
	print "Gives the list of all authors\n"
		
	q1="MATCH (n:Author) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)
	

get_authors()
