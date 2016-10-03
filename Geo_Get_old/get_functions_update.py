from py2neo import Node, Relationship, Graph, authenticate
#(give your  "localhost/neo4j username/ neo4j password")
authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")

from titlecase import titlecase

def get_countries():
	
	print "Function name:Get_countries"  
	print "Gives the list of all countries\n"
	
	q1="MATCH (cntry:Country) RETURN cntry.Name"
	res=graph.cypher.execute(q1)
	print (res)
	
def get_continents():

	print "Function name:Get_continents\nGives the list of all continents\n"
	
	q1="MATCH (cntnt:Continent) RETURN cntnt.Name"
	res=graph.cypher.execute(q1)
	print (res)

def get_authors():
	
	print "Function name:Get_author"  
	print "Gives the list of all authors\n"
		
	q1="MATCH (a:Author) RETURN a.Name"
	res=graph.cypher.execute(q1)
	print (res)

def get_journals():
	
	print"Function name:Get_jounrals\nGives list of all journals\n"
	q1="MATCH (j:Journal) RETURN j.Name"
	res=graph.cypher.execute(q1)
	print (res)

def get_publishers():

	print "Function name:Get_publisher\nGives list of all publishers\n"	
	q1="MATCH (p:Publisher) RETURN p.Name"
	res=graph.cypher.execute(q1)
	print (res)
	
def get_affiliation():

	print "Function name:Get_affiliation\nGives list of all affiliation \n"
	s="MATCH (aff:Affiliation) RETURN aff.Name"
	res=graph.cypher.execute(s)
	print (res)


def get_article_by_continent(x):

	x=titlecase(x)
	print "Function name:Get_article_by_continent\nGives list of all articles according to the input continent\n"	
	#x=input("Enter contienent name:")
	print "\nContinent name:",x
	q1="MATCH (ar:Article)-[:authored_by]->(Author)-[:affiliated_to]->(Affiliation)-[:located_in]->(Country)-[:part_of]->(Continent {name:'"+x+"'}) RETURN ar.Name"
	res=graph.cypher.execute(q1)
	print (res)

def get_author_by_resident_country(x):
	x=titlecase(x)
	print "Function name:Get_author_resident_country\nGives list of all authors according to input resident country\n"
	#x=input("Enter acountry name:")
	print "\nCountry name:",x
	q1="MATCH (a:Author)-[:lives_in]->(City)-[:located_in]->(Country {name:'"+x+"'}) RETURN a.Name"
	res=graph.cypher.execute(q1)
	print (res)


def get_journal_by_country(x):
	x=titlecase(x)
	print "Function name:Get_journal_by_country\nGives list of all journals by input country\n"
	#x = input("Enter Country Name:")
	print "\nCountry name:",x
	q1 = "MATCH (j:Journal)-[:published_in]->(Country {name:'"+x+"'}) RETURN j.Name"
	result1 = graph.cypher.execute(q1)
	print(result1)


def get_article_by_country(x):
	x=titlecase(x)
	print "Function name:Get_article_by_country\nGives list of all journals by input country\n"
	#x = input("Enter Country Name")
	print "\nCountry name",x
	q2 = "MATCH (ar:Article)-[:authored_by]->(Author)-[:affiliated_to]->(Affiliation)-[:located_in]->(Country {name:'"+x+"'}) RETURN ar.Name"
	result2 = graph.cypher.execute(q2)
	print(result2)

def get_article_by_domain(x):
	x=titlecase(x)
	print "Function name:Get_articles_by_domain\nGives list of all articles by input domain\n"
	#x = input("Enter Domain")
	print "\nDomain name",x
	q3 = "MATCH (Journal)-[:belongs_to]->(Domain {name:'"+x+"'}),(Article)<-[:contains]-(Journal) RETURN ar.Name, d.Name;"
	result3 = graph.cypher.execute(q3)
	print(result3)

def get_affiliation_by_domain(x):
	x=titlecase(x)
	print "Function name:Get_affiliation_by_domain\nGives list of all affiliation by input domain\n"
	#x= input('Enter Domain name')
	print "\nDomain name:",x
	s="MATCH (Domain{name:'"+x+"'})<-[:belongs_to]-(Journal)-[:contains]->(Article)-[:authored_by]->(Author)-[:affiliated_to]->(aff:Affiliation) RETURN aff.Name"
        res=graph.cypher.execute(s)
        print (res)


def get_publisher_by_domain(x):
	x=titlecase(x)
	print "Function name:Get_publisher_by_domain\nGives list of all publisher by input domain\n"
	#x= input('Enter Domain name')
	print "\nDomain name:",x
	s="MATCH (p:Publisher)<-[:published_by]-(:Journal)-[:belongs_to]->(Domain {name:'"+x+"'}) RETURN p.Name"
	res=graph.cypher.execute(s)
	print (res)

def get_journal_by_continent(x):
	x=titlecase(x)
	print "Function name:Get_journal_by_continent\nGives list of all journals by input continent\n"
	#x=input("Enter continent name:")
	print "\nContinent name:",x
	q1="MATCH (j:Journal)-[:published_in]->(Country)-[:part_of]->(Continent {name:'"+x+"'}) RETURN j.Name"
	res=graph.cypher.execute(q1)
	print (res)

def get_country_by_continent(x):
	x=titlecase(x)
	print "Function name:Get_country_by_continent\nGives all countries of the continent given as input\n"
	#x=input("Enter contienent name:")
	print "\nContinent name:",x
	q1="MATCH (cntry:Country)-[:part_of]->(Continent {name:'"+x+"'}) RETURN cntry.Name"
	res=graph.cypher.execute(q1)
	print (res)

def get_journal_by_domain(x):
	x=titlecase(x)
	print "Function name:Get_journal_by_domain\nGives all journals of the domain given as input"
	#x=input("Enter domain name:")
	print "\nDomain name:",x
	q1="MATCH (j:Journal)-[:belongs_to]->(Domain{name:'"+x+"'}) RETURN j.Name"
	res=graph.cypher.execute(q1)
	print (res)

def get_author_by_origin_country(x):
	x=titlecase(x)
	print "Function name:Get_author_by_origincountry\nGives all authors of the country(based on origin of author) given as input\n"
	#x=input("Enter country name:")
	print "\nCountry name:",x
	q1="MATCH (a:Author)-[:native_of]->(City)-[:located_in]->(Country{name:'"+x+"'}) RETURN a.Name"
	res=graph.cypher.execute(q1)
	print (res)

def get_publisher_by_country(x):
	x=titlecase(x)
	print "Function name:Get_publisher_by_country\nGives all publishers of the country given as input\n"
	#x=input("Enter country name:")
	print "\nCountry name:",x
	q1="MATCH (p:Publisher)-[:based_in]->(Country{name:'"+x+"'}) RETURN p.Name"
	res=graph.cypher.execute(q1)
	print (res)

def get_journal_by_publisher(x):
	x=titlecase(x)
	print "Function name:Get_journal_by_publisher\nThis Gives all the journals of the publisher given as input"
	print "\nPublisher:",x
	q="MATCH (j:Journal)-[:published_by]->(Publisher{name:'"+x+"'}) RETURN j.Name"
	res=graph.cypher.execute(q)
	print (res)
	


def get_authors_by_domain(x):
	x=titlecase(x)
        print "Function name:Get_authors_by_domain\nGives all authors of a given domain name\n"
        #x= input('Enter Domain name')
	print "\nDomain:",x
        a="MATCH (a:Author)<-[:authored_by]-(Article)<-[:contains]-(Journal)-[:belongs_to]->(Domain {name:'"+x+"'}) RETURN a.Name"
        res=graph.cypher.execute(a)
        print (res)



def get_articles_by_journal(x):
	x=titlecase(x)
	print "Function name:Get_articles_by_journal\nGives all the articles of the journal given as input\n"
	print "Journal:",x
	q="MATCH (ar:Article)<-[:contains]-(Journal {name:'"+x+"'}) RETURN ar.Name"

	res=graph.cypher.execute(q)
	print (res)
	


def get_affiliations_by_country(x):
	x=titlecase(x)
        print "Function name: get_affiliations_by_country()\nGives a list of affiliations for a given country "
        #x= input('Enter country name')
	print "\nCountry:",x
        a="MATCH (cntry:Country{name:'"+x+"'})<-[:located_in]-(City)<-[:located_in]-(aff:Affiliation) RETURN aff.Name"
        res=graph.cypher.execute(a)
        print (res)



def get_authors_by_affiliation(x):
	x=titlecase(x)
	print "Function name:Get_authors_by_affiliation\nThis Gives all the authors of the affiliation given as input"
	print "\nAffiliation:",x
	q="MATCH (a:Author)-[:affiliated_to]->(Affiliation{name:'"+x+"'}) RETURN a.Name"
	res=graph.cypher.execute(q)
	print (res)


def get_journal_by_author(x):
	x=titlecase(x)
	print "Function name:Get_journal_by_author\nThis Gives all the journals of an author given as input"
	print "\nAuthor:",x
	q="MATCH (j:Journal)-[:contains]->(Article)-[:authored_by]->(Author {name:'"+x+"'}) RETURN j.Name"
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
