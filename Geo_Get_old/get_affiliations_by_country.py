from py2neo import Node, Relationship, Graph, authenticate
authenticate("localhost:7474","neo4j","Scibase")
graph=Graph("http://localhost:7474/db/data")


def get_affiliations_by_country():
        print "Function name: get_affiliations_by_country()\nGives a list of affiliations for a given country "
        x= input('Enter country name')
        a="MATCH (n:Country{name:'"+x+"'}) <-[:Belongs_to]-(Journal)-[:Contains]->(Article)-[:Authored_by]->(Author)-[:Affiliated_to]->(n:Affiliation) RETURN n.name"
        res=graph.cypher.execute(a)
        print (res)

get_affiliations_by_country()


