#!/usr/bin/python3

import argparse
import json
import dicttoxml
import xmltodict
import yaml

parser = argparse.ArgumentParser(description='converter')
parser.add_argument("--infile", help="file name")
parser.add_argument("--informat", help="format import file")
parser.add_argument("--outformat", help="format output file")
args = parser.parse_args()

if args.informat == "xml":
    python_dict = xml_to_python_dict(reading_file)
elif args.informat == "json":
    python_dict = json_to_python_dict(reading_file)
elif args.informat == "yaml":
    python_dict = yaml_to_python_dict(reading_file)


if args.outformat == "xml":
    xml_string = python_dict_to_xml(python_dict)
    print(xml_string)
elif args.outformat == "json":
    json_string = python_dict_to_json(python_dict)
    print(json_string)
elif args.outformat == "yaml":
    yaml_string = python_dict_to_yaml(python_dict)
    print(yaml_string)
