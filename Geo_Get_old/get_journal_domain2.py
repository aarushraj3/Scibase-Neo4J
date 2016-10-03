from py2neo import Node, Relationship, Graph, authenticate
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")


def get_journal_by_domain(x):

	print "Function name:Get_journal_by_domain\nGives all journals of the domain given as input"
	#x=input("Enter domain name:")
	print "\nDomain name:",x
	q1="MATCH (n:Journal)-[:Part_of]->(Domain{name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)
	
get_journal_by_domain("Domain1")

