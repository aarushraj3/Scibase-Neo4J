from py2neo import Node, Relationship, Graph, authenticate
authenticate("localhost:7474","neo4j","suraj1012")
graph=Graph("http://localhost:7474/db/data")


def get_articles_by_journal(x):

	print "Function name:Get_articles_by_journal\nGives all the articles of the journal given as input\n"
	print "Journal:",x
	q="MATCH (n:Article)<-[:Contains]-(Journal{name:'"+x+"'}) RETURN n.name"

	res=graph.cypher.execute(q)
	print (res)
	
get_articles_by_journal("ghi")

