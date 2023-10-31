#!/usr/bin/python3

import argparse
import json
import dicttoxml
import xmltodict
# parser = argparse.ArgumentParser(description='converter')
# parser.add_argument("--infile", help="file name")
# parser.add_argument("--informat", help="format import file")
# parser.add_argument("--outformat", help="format output file")
# args = parser.parse_args()
# f = open("person.xml", "r")
# print(f.read())
# f.close

# with open('person.xml', 'r', encoding='utf-8') as file:
#     f = file.read()
# print(f)

# with open('person.xml', 'r') as myfile:
#     obj = xmltodict.parse(myfile.read())
# print(json.dumps(obj))

import yaml
xml_string = """<Person>
    <FirstName>Ivan</FirstName>
    <LastName>Ivanov</LastName>
    <Jobs>
        <Job>
            <Title>Manager</Title>
        </Job>
        <Job>
            <Title>Consultant</Title>
        </Job>
    </Jobs>
</Person>"""
print("The XML string is:")
# print(xml_string)
# python_dict=xmltodict.parse(xml_string)
# yaml_string=yaml.dump(python_dict)
# print("The YAML string is:")
# print(yaml_string)

# python_dict = xmltodict.parse(xml_string)
# file = open("person.yaml", "w")
# yaml.dump(python_dict, file)
# file.close()
xml_file = open("person.xml", "r")
xml_string = xml_file.read()
python_dict = xmltodict.parse(xml_string)
yaml_string = yaml.dump(python_dict)
print("The YAML string is:")
print(yaml_string)
