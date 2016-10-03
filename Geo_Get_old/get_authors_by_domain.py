from py2neo import Node, Relationship, Graph, authenticate
authenticate("localhost:7474","neo4j","Scibase")
graph=Graph("http://localhost:7474/db/data")




def get_authors_by_domain():
        print "Function name:Get_authors_by_domain\nGives all authors of a given domain name\n"
        x= input('Enter Domain name')
        a="MATCH (n:Author)-[:Belongs_to]->(Domain {name:'"+x+"'}) RETURN n.name"
        res=graph.cypher.execute(a)
        print (res)

get_authors_by_domain()

