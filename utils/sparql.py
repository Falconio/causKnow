from SPARQLWrapper import SPARQLWrapper, JSON

# general scheme for SPARQL queries

sparql = SPARQLWrapper("http://localhost:3030/causknow/sparql")


class sparqlQuery:
    def __init__(self, sparqlquery):
        sparql.setQuery(sparqlquery)
        sparql.setReturnFormat(JSON)
        self.results = sparql.query().convert()

    def sparqlResults(self):
        try:
            results = self.results
            return results
        except:
            return "ERROR: Something wrong with the query"
