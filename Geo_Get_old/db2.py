from py2neo import Graph, Node, authenticate,Relationship,cypher

authenticate("localhost:7474", "neo4j", "scibase")

graph = Graph("http://localhost:7474/db/data/")

#countries 5 total
Country1= Node("Country", name= "Country1")
graph.create(Country1)

Country2= Node("Country", name= "Country2")
graph.create(Country2)

Country3= Node("Country", name= "Country3")
graph.create(Country3)

Country4= Node("Country", name= "Country4")
graph.create(Country4)

Country5= Node("Country", name= "Country5")
graph.create(Country5)

#continents 7
Asia = Node("Continent", name="Asia")
graph.create(Asia)

Africa = Node("Continent", name="Africa")
graph.create(Africa)

North_America = Node("Continent", name="North America")
graph.create(North_America)

South_America= Node("Continent", name="South America")
graph.create(South_America)

Europe = Node("Continent", name="Europe")
graph.create(Europe)

Antartica = Node("Continent", name="Antartica")
graph.create(Antartica)

Australia = Node("Continent", name="Australia")
graph.create(Australia)

#author 4
Author1 = Node("Author", name="Author1")
graph.create(Author1)

Author2 = Node("Author", name="Author2")
graph.create(Author2)

Author3 = Node("Author", name="Author3")
graph.create(Author3)

Author4 = Node("Author", name="Author4")
graph.create(Author4)


#publisher 3
Publisher1 = Node("Publisher", name="Publisher1")
graph.create(Publisher1)

Publisher2 = Node("Publisher", name="Publisher2")
graph.create(Publisher2)

Publisher3 = Node("Publisher", name="Publisher3")
graph.create(Publisher3)

#domain 3
Domain1 = Node("Domain", name="Domain1")
graph.create(Domain1)

Domain2 = Node("Domain", name="Domain2")
graph.create(Domain2)

Domain3 = Node("Domain", name="Domain3")
graph.create(Domain3)

#institute 3
Institute1 = Node("Institute", name="Institute1")
graph.create(Institute1)

Institute2 = Node("Institute", name="Institute2")
graph.create(Institute2)

Institute3 = Node("Institute", name="Institute3")
graph.create(Institute3)

#article 3
Article1 = Node("Article", name="Article1",DOI="10.1000/182")
graph.create(Article1)

Article2 = Node("Article", name="Article2",DOI="10.1000/187")
graph.create(Article2)

Article3 = Node("Article", name="Article3",DOI="10.1001/182")
graph.create(Article3)

#journal 3
Journal1 = Node("Journal", name="Journal1",ISSN="1234-098X")
graph.create(Journal1)


Journal2 = Node("Journal", name="Journal2",ISSN="1200-9087")
graph.create(Journal2)

Journal3 = Node("Journal", name="Journal3",ISSN="1341-1234")
graph.create(Journal3)

#relationships

#author
graph.create_unique(Relationship(Author1, "Lives_in", Country1))#resident country
graph.create_unique(Relationship(Author1, "Origin_from", Country2))#origin country

graph.create_unique(Relationship(Author2, "Lives_in", Country3))#resident country
graph.create_unique(Relationship(Author2, "Origin_from", Country4))#origin country

graph.create_unique(Relationship(Author3, "Lives_in", Country5))#resident country
graph.create_unique(Relationship(Author3, "Origin_from", Country1))#origin country

graph.create_unique(Relationship(Author4, "Lives_in", Country2))#resident country
graph.create_unique(Relationship(Author4, "Origin_from", Country3))#origin country

#publisher
graph.create_unique(Relationship(Publisher1, "Based_in", Country1))#publisher based in country
graph.create_unique(Relationship(Publisher2, "Based_in", Country2))
graph.create_unique(Relationship(Publisher3, "Based_in", Country3))

#article
graph.create_unique(Relationship(Article1, "Authored_by", Author1))#author of every article
graph.create_unique(Relationship(Article2, "Authored_by", Author2))
graph.create_unique(Relationship(Article3, "Authored_by", Author3))

graph.create_unique(Relationship(Article1, "Computed", Domain1))#article belongs to which domain
graph.create_unique(Relationship(Article2, "Computed", Domain2))
graph.create_unique(Relationship(Article3, "Computed", Domain3))

#journal
graph.create_unique(Relationship(Journal1, "Contains", Article1))#article is part of which journal
graph.create_unique(Relationship(Journal2, "Contains", Article2))
graph.create_unique(Relationship(Journal3, "Contains", Article3))

graph.create_unique(Relationship(Journal1, "Published_by", Publisher1))#journal published by which publisher
graph.create_unique(Relationship(Journal2, "Published_by", Publisher2))
graph.create_unique(Relationship(Journal3, "Published_by", Publisher3))

graph.create_unique(Relationship(Journal1, "Belongs_to", Domain1))#journal belongs to  which domain
graph.create_unique(Relationship(Journal2, "Belongs_to", Domain2))
graph.create_unique(Relationship(Journal3, "Belongs_to", Domain3))

graph.create_unique(Relationship(Journal1, "Computed", Domain1))#journal domain computed relation
graph.create_unique(Relationship(Journal2, "Computed", Domain2))
graph.create_unique(Relationship(Journal3, "Computed", Domain3))

graph.create_unique(Relationship(Journal1, "Published_in", Country3))#journal published in which country
graph.create_unique(Relationship(Journal2, "Published_in", Country4))
graph.create_unique(Relationship(Journal3, "Published_in", Country5))

#institution
graph.create_unique(Relationship(Institute1, "Located_in", Country1))#institute located in which country
graph.create_unique(Relationship(Institute2, "Located_in", Country2))
graph.create_unique(Relationship(Institute3, "Located_in", Country3))

#country
graph.create_unique(Relationship(Country1, "Part_of", Asia))#country is a part of which continent
graph.create_unique(Relationship(Country2, "Part_of", Europe))
graph.create_unique(Relationship(Country3, "Part_of", North_America))
graph.create_unique(Relationship(Country4, "Part_of", South_America))
graph.create_unique(Relationship(Country5, "Part_of", Africa))

