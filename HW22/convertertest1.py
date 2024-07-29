#!/usr/bin/python3

import argparse
import json
import xmltodict
import yaml

parser = argparse.ArgumentParser(description='converter')
parser.add_argument("--infile", help="file name")
parser.add_argument("--informat", help="format import file")
parser.add_argument("--outformat", help="format output file")
args = parser.parse_args()

with open(args.infile, 'r') as file:
    xml_file = file.read()
# print(xml_file)
data = xmltodict.parse(xml_file)

# using json.dumps to convert dictionary to JSON
json_file = json.dumps(data, indent=4)
# print(json_file)

# using yaml.dump to convert dictionary to YAML
yaml_file = yaml.dump(data)
# print(data)

if args.informat == "xml":
    xml_forma = xml_file
    # print(xml_forma)
elif args.informat == "json":
    json_forma = json_file
    # print(json_forma)
elif args.informat == "yaml":
    yaml_forma = yaml_file
    # print(yaml_forma)

if args.outformat == "xml":
    forma = xml_file
    print(forma)
elif args.outformat == "json":
    forma = json_file
    print(forma)
elif args.outformat == "yaml":
    forma = yaml_file
    print(forma)
