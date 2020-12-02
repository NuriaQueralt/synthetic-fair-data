# @name: rdf2srdf.py
# @description: Script to test to generate synthetic fair data
# @version: 1.0
# @date: 11-09-2020
# @author: Núria Queralt Rosinach
# @email: n.queralt_rosinach@lumc.nl

# TODO: code to generate synthetic fair data
"""Script to test to generate synthetic fair data"""

import rdflib

# variables
ont = rdflib.Graph()
rdf_in = rdflib.Graph()

# input
# semantic model
ont_owl = 'https://github.com/FAIRDataTeam/WHO-COVID-CRF/raw/master/WHO_COVID-19_Rapid_Version_CRF_Ontology.owl'

# rdf data
who_ttl = '../in/who-crf/vodan/test_report_dsw_rajaram.ttl'

# script
# load semantic model
ont.load(ont_owl)
print("* The ontology has {} statements.".format(len(ont)))

# read who crf form rdf/ttl
rdf_in.parse(who_ttl, format="ttl")
print("* The who crf rdf has {} statements.".format(len(rdf_in)))

# RDF DATA
# parse rdf to csv
# variable dictionary to store form:questions:
# { crf1: { question: { value, unit, rule, range } }
crf2question = dict()
question2result = dict()
result = dict()

# parse
import pprint
#for stmt in rdf_in:
    #pprint.pprint(stmt)

# build a table for patient 1 :: IL-6 results

# ONTOLOGY
# parse ontology question structure
# { question: { str: onto_path } }
question2ontoPath = dict()

# find IL-6 subclass structure
c = rdflib.URIRef("http://purl.org/vodan/whocovid19crfsemdatamodel/IL-6")
# pprint.pprint(ont.preferredLabel(c, lang="en"))
# pprint.pprint(ont.objects(subject=c, predicate=rdflib.RDFS.subClassOf))
# pprint.pprint(type(ont.objects(subject=c, predicate=rdflib.RDFS.subClassOf)))
# for parent in ont.objects(subject=c, predicate=rdflib.RDFS.subClassOf):
#     pprint.pprint(parent)

# class
print("* Parsing IL-6 question.\n  Class information:  ")
types_dict = dict()
for type in ont.objects(c, rdflib.RDFS.subClassOf):
    # if parent class is an atomic class (concept or IRI)
    if isinstance(type, rdflib.URIRef):
        parent_class = type
    # if parent class is a class expression (anonymous class or complex concept or BNode)
    constructor_dict = dict()
    axiom_list = list()
    if isinstance(type, rdflib.BNode):
        # has_measurement_unit_label value pg/ml (object property individual value restriction)
        for s,p,o in ont.triples((type,None,None)):
            axiom_list.append({p:o})
        constructor_dict[s]= axiom_list
            #print(s,p,o)

    types_dict.update({type: 1})

print("\t- subclass of {} classes: {}".format(len(types_dict), types_dict.keys()))
print("\t\t subclass of atomic class: '{}'".format(parent_class))
print("\t\t subclass of axioms class:")
first_triple = 1
for anonymous_class_id in constructor_dict:
    if first_triple:
        first_triple = 0
        print("\t\t [ {}".format(anonymous_class_id))
    for axiom in range(len(constructor_dict[anonymous_class_id])):
        for predicate, value in constructor_dict[anonymous_class_id][axiom].items():
            if axiom < len(constructor_dict[anonymous_class_id])-1:
                print("\t\t   {} {} ;".format(predicate,value))
            else:
                print("\t\t   {} {} .".format(predicate,value))
        # print("\t\t   {} {} ;".format(predicate,constructor_dict[anonymous_class_id][axiom].values()))
print("\t\t ]".format(s))

labels_dict = dict()
for label in ont.objects(c, rdflib.RDFS.label):
    labels_dict.update({label: 1})

print("\t- {} labels: {}".format(len(labels_dict), labels_dict))

for preflabel in ont.objects(c, rdflib.SKOS.prefLabel):
    print("\t- preferred label: {}".format(preflabel))

# parent class
print("\n  Parent class information:")
print("  {} is subclass of:".format(parent_class))
# for parent in ont.objects(parent_class, rdflib.RDFS.subClassOf):
#     if isinstance(parent, rdflib.URIRef):
#         print("\t- {} ({})".format(parent, ont.preferredLabel(parent, lang="en")[0][1]))
#     else:
#         print("\t- {}".format(parent))
        # part_of
        # has_literal_value union
        # has_other_measurement_unit_label

# print subclasses triples or axioms (the ones which are BNodes)
print("\n Parent class axioms")
print("  'part_of' predicates:")
# for s, p, o in ont.triples((None, rdflib.OWL.onProperty, rdflib.URIRef("http://purl.obolibrary.org/obo/BFO_0000050"))):
#     print(s)

# RULES/RANGES
# { question: { rules: axioms, ranges: { dec, max, min }, units: unit_list } }
# find axioms, e.g. subclassof
# find ranges, both numeric and unit labels
# variable array to store the tabular information:
# ( crf_result x clinical parameter result )
# e.g. crf1_module2_result3 x fever,il6,thrombosis
crf_result2question = dict()


# Ranges and rules

# generate synthetic data in csv

# convert synthetic data in csv to rdf/ttl



