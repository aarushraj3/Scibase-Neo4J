from py2neo import Node, Relationship, Graph, authenticate
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")



def get_author_by_origincountry(x):

	print "Function name:Get_author_by_origincountry\nGives all authors of the country(based on origin of author) given as input\n"
	#x=input("Enter country name:")
	print "\nCountry name:",x
	q1="MATCH (n:Author)-[:Origin_from]->(Country{name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)
	
get_author_by_origincountry("Country1")

