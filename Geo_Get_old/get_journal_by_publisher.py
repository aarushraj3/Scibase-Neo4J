from py2neo import Node, Relationship, Graph, authenticate
authenticate("localhost:7474","neo4j","suraj1012")
graph=Graph("http://localhost:7474/db/data")


def get_journal_by_publisher(x):

	print "Function name:Get_journal_by_publisher\nThis Gives all the journals of the publisher given as input"
	print "\nPublisher:\n",x
	q="MATCH (n:Journal)-[:Published_by]->(Publisher{name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q)
	print (res)
	
get_journal_by_publisher("mno")

