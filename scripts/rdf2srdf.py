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

# parse rdf to csv
# variable dictionary to store form:questions:
# { crf1: { question: { value, unit, rule, range } }
crf2question = dict()
question2result = dict()
results_list = list()

# parse
import pprint
for stmt in rdf_in:
    pprint.pprint(stmt)

# parse ontology question structure
# { question: onto_path }
question2ontoPath = dict()

# variable array to store the tabular information:
# ( crf_result x clinical parameter result )
# e.g. crf1_module2_result3 x fever,il6,thrombosis
crf_result2question = dict()


# Ranges and rules

# generate synthetic data in csv

# convert synthetic data in csv to rdf/ttl



