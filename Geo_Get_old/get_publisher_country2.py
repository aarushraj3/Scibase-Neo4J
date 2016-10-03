from py2neo import Node, Relationship, Graph, authenticate
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")



def get_publisher_by_country(x):

	print "Function name:Get_publisher_by_country\nGives all publishers of the country given as input\n"
	#x=input("Enter country name:")
	print "\nCountry name:",x
	q1="MATCH (n:Publisher)-[:Based_in]->(Country{name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)
	
get_publisher_by_country("Country1")

