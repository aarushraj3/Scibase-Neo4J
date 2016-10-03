from py2neo import Graph, Node, Relationship, authenticate

authenticate("localhost:7474","neo4j","my-p4ssword")
# link of the database garph (scibase of cource :P) 
graph=Graph("http://localhost:7474/db/data")


# get Journals by country
def get_Journal_by_country(graph):
	x = input("Enter Country Name:")
	q1 = "MATCH (n:Journal)-[:Published_in]->(Country {name:'"+x+"'}) RETURN n.name"
	result1 = graph.cypher.execute(q1)
	return result1

# get articles by country
def get_article_by_country(graph):
	x = input("Enter Country Name")
	q2 = "MATCH (Journal)-[:CONTAINS]->(article), (Journal)<-[:Published_in]-(country {name:'"+x+"'}) RETURN article.name, country.name;"
	result2 = graph.cypher.execute(q2)
	return result2

# get articles by domain
def get_artices_by_domain(graph):
	x = input("Enter Domain")
	q3 = "MATCH (Journal)-[:BELONGS_TO]->(domain {name:'"+x+"'}),(article)<-[:CONTAINS]-(Journal) RETURN article.name, domain.name;"
	result3 = graph.cypher.execute(q3)
	return result3


r1 = get_Journal_by_country(graph)
print(r1)
r2 = get_article_by_country(graph)
print(r2)
r3 = get_artices_by_domain(graph)
print(r3)
