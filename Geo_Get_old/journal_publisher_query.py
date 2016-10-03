import csv
from py2neo import Node, Relationship, Graph, authenticate

authenticate("localhost:7474","neo4j","scibase")
graph=Graph("http://localhost:7474/db/data")


def add_journal():
	labels = graph.node_labels
	for label in labels:
		try:
			graph.schema.create_uniqueness_constraint(label, 'ISSN')
		except:
			pass


	with open('Journal_list.csv') as csvfile1:
		journal_file = csv.reader(csvfile1)
		for row in journal_file:
			row_var = Node("Journal", name = row[0], ISSN = row[1])
			graph.merge(row_var)

def add_publisher_info():
	with open('journal_publisher_relation.csv') as csvfile2:
		journal_file = csv.reader(csvfile2)
		for row in journal_file:
			row_var1 = Node("Publisher", name = row[1])
			row_var2 = Node("Journal", name = row[0])
			graph.merge(row_var1)
			graph.merge(row_var2)
			rel = Relationship(row_var1, "Published_By", row_var2)
			graph.merge(rel)

add_journal()
add_publisher_info()

'''

While pushing the data make the query generic so that next time we can just push the data where publisher information is from one file and 
Journal information is from another file

Explore Merge and Unwind cypher queries

routine to add journal node to do the following:
-> create a Journal node with parameters as ISSN (with unique constraints) and name read from a csv/json file
-> create a publisher node with name (with unique constraints) as a property read from another json/csv file where journal and publisher data is available
-> create a relationship between them

'''