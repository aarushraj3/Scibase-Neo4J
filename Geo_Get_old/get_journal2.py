from py2neo import Node, Relationship, Graph, authenticate
#(give your  "localhost/neo4j username/ neo4j password")
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")




def get_journals():
	
	print"Function name:Get_jounrals\nGives list of all journals\n"
	q1="MATCH (n:Journal) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)
	

get_journals()
