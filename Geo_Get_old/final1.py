from py2neo import Node, Relationship, Graph, authenticate
#(give your  "localhost/neo4j username/ neo4j password")
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")





	

def get_countries():
	
	print "Function_name:Get_countries"  
	print "Gives the list of all countries\n"
	
	q1="MATCH (n:Country) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)
	
def get_continents():

	print "Function name:Get_continents\nGives the list of all continents\n"
	
	q1="MATCH (n:Continent) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)

def get_authors():
	
	print "Function_name:Get_author"  
	print "Gives the list of all authors\n"
		
	q1="MATCH (n:Author) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)

def get_journals():
	
	print"Function name:Get_jounrals\nGives list of all journals\n"
	q1="MATCH (n:Journal) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)

def get_publishers():

	print "Function name:Get_publisher\nGives list of all publishers\n"	
	q1="MATCH (n:Publisher) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)
	
def get_affiliation():

	print "Function name:Get_affiliation\nGives list of all affiliation \n"
	s="MATCH (n:Affiliation) RETURN n.name"
	res=graph.cypher.execute(s)
	print (res)


def get_article_by_continent(x):

	print "Function name:Get_article_by_continent\nGives list of all articles according to the input continent\n"	
	#x=input("Enter contienent name:")
	print "\nContinent name:",x
	q1="MATCH (n:Article)-[:Authored_by]->(Author)-[:Affiliated_to]->(Affiliation)-[:Located_in]->(Country)-[:Part_of]->(Continent {name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)

def get_author_by_resident_country(x):

	print "Function name:Get_author_resident_country\nGives list of all authors according to input resident country\n"
	#x=input("Enter country name:")
	print "\nCountry name:",x
	q1="MATCH (n:Author)-[:Lives_in]->(Country {name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)


def get_journal_by_country(x):

	print "Function name:Get_journal_by_country\nGives list of all journals by input country\n"
	#x = input("Enter Country Name:")
	print "\nCountry name:",x
	q1 = "MATCH (n:Journal)-[:Published_in]->(Country {name:'"+x+"'}) RETURN n.name"
	result1 = graph.cypher.execute(q1)
	print(result1)


def get_article_by_country(x):

	print "Function name:Get_article_by_country\nGives list of all journals by input country\n"
	#x = input("Enter Country Name")
	print "\nCountry name",x
	q2 = "MATCH (n:Article)-[:Authored_by]->(Author)-[:Affiliated_to]->(Affiliation)-[:Located_in]->(Country {name:'"+x+"'}) RETURN n.name"
	result2 = graph.cypher.execute(q2)
	print(result2)

def get_article_by_domain(x):

	print "Function name:Get_articles_by_domain\nGives list of all articles by input domain\n"
	#x = input("Enter Domain")
	print "\nDomain name",x
	q3 = "MATCH (Journal)-[:Belongs_to]->(domain {name:'"+x+"'}),(article)<-[:Contains]-(Journal) RETURN article.name, domain.name;"
	result3 = graph.cypher.execute(q3)
	print(result3)

def get_affiliation_by_domain(x):

	print "Function name:Get_affiliation_by_domain\nGives list of all affiliation by input domain\n"
	#x= input('Enter Domain name')
	print "\nDomain name:",x
	s="MATCH (Domain{name:'"+x+"'})<-[:Belongs_to]-(Journal)-[:Contains]->(Article)-[:Authored_by]->(Author)-[:Affiliated_to]->(n:Affiliation) RETURN n.name"
        res=graph.cypher.execute(s)
        print (res)


def get_publisher_by_domain(x):
	
	print "Function name:Get_publisher_by_domain\nGives list of all publisher by input domain\n"
	#x= input('Enter Domain name')
	print "\nDomain name:",x
	s="MATCH (n:Publisher)<-[:Published_by]-(:Journal)-[:Belongs_to]->(Domain {name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(s)
	print (res)

def get_journal_by_continent(x):

	print "Function name:Get_journal_by_continent\nGives list of all journals by input continent\n"
	#x=input("Enter continent name:")
	print "\nContinent name:",x
	q1="MATCH (n:Journal)-[:Published_in]->(Country)-[:Part_of]->(Continent {name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)

def get_country_by_continent(x):

	print "Function name:Get_country_by_continent\nGives all countries of the continent given as input\n"
	#x=input("Enter contienent name:")
	print "\nContinent name:",x
	q1="MATCH (n:Country)-[:Part_of]->(Continent {name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)

def get_journal_by_domain(x):

	print "Function name:Get_journal_by_domain\nGives all journals of the domain given as input"
	#x=input("Enter domain name:")
	print "\nDomain name:",x
	q1="MATCH (n:Journal)-[:Belongs_to]->(Domain{name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)

def get_author_by_origin_country(x):

	print "Function name:Get_author_by_origincountry\nGives all authors of the country(based on origin of author) given as input\n"
	#x=input("Enter country name:")
	print "\nCountry name:",x
	q1="MATCH (n:Author)-[:Native_of]->(Country{name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)

def get_publisher_by_country(x):

	print "Function name:Get_publisher_by_country\nGives all publishers of the country given as input\n"
	#x=input("Enter country name:")
	print "\nCountry name:",x
	q1="MATCH (n:Publisher)-[:Based_in]->(Country{name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q1)
	print (res)

def get_journal_by_publisher(x):

	print "Function name:Get_journal_by_publisher\nThis Gives all the journals of the publisher given as input"
	print "\nPublisher:",x
	q="MATCH (n:Journal)-[:Published_by]->(Publisher{name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q)
	print (res)
	


def get_authors_by_domain(x):
        print "Function name:Get_authors_by_domain\nGives all authors of a given domain name\n"
        #x= input('Enter Domain name')
	print "\nDomain:",x
        a="MATCH (n:Author)<-[:Authored_by]-(Article)<-[:Contains]-(Journal)-[:Belongs_to]->(Domain {name:'"+x+"'}) RETURN n.name"
        res=graph.cypher.execute(a)
        print (res)



def get_articles_by_journal(x):

	print "Function name:Get_articles_by_journal\nGives all the articles of the journal given as input\n"
	print "Journal:",x
	q="MATCH (n:Article)<-[:Contains]-(Journal{name:'"+x+"'}) RETURN n.name"

	res=graph.cypher.execute(q)
	print (res)
	


def get_affiliations_by_country(x):
        print "Function name: get_affiliations_by_country()\nGives a list of affiliations for a given country "
        #x= input('Enter country name')
	print "\nCountry:",x
        a="MATCH (c:Country{name:'"+x+"'})<-[:Located_in]-(n:Affiliation) RETURN n.name"
        res=graph.cypher.execute(a)
        print (res)



def get_authors_by_affiliation(x):

	print "Function name:Get_authors_by_affiliation\nThis Gives all the authors of the affiliation given as input"
	print "\nAffiliation:",x
	q="MATCH (n:Author)-[:Affiliated_to]->(Affiliation{name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q)
	print (res)


def get_journal_by_author(x):

	print "Function name:Get_journal_by_author\nThis Gives all the journals of an author given as input"
	print "\nAuthor:",x
	q="MATCH (n:Journal)-[:Contains]->(Article)-[:Authored_by]->(Author {name:'"+x+"'}) RETURN n.name"
	res=graph.cypher.execute(q)
	print (res)
	


get_continents()
get_countries()
get_authors()

get_journals()
get_publishers()
get_affiliation()

get_country_by_continent("australia")
get_author_by_resident_country("ind")
get_author_by_origin_country("ind")

get_journal_by_continent("asia")
get_journal_by_country("ind")
get_journal_by_domain("d2")

get_article_by_continent("europe")
get_article_by_country("ind")
get_article_by_domain("d1")

get_affiliation_by_domain("d1")
get_publisher_by_country("USA")
get_publisher_by_domain("d1")

get_journal_by_publisher("ieee")
get_authors_by_domain("d2")
get_articles_by_journal("j2")

get_affiliations_by_country("eng")
get_authors_by_affiliation("pes")
get_journal_by_author("a2")
