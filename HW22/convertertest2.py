#!/usr/bin/python3
import xmltodict
from yaml import SafeLoader
import yaml
import json
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument(
    '--infile', type=argparse.FileType('r'), default=sys.stdin)

parser.add_argument('--outformat', choices=['xml', 'yaml', 'json'])

parser.add_argument('--informat', choices=['xml', 'yaml', 'json'])

args = parser.parse_args()

# Запись файла в строку

file_content = args.infile.read()

print("Текущий файл:\n")

print(file_content)

# Функции конвертации


def json_to_xml(file_content):

    python_dict = json.loads(file_content)

    xml_string = xmltodict.unparse(python_dict, pretty=True)

    line = xml_string.split('\n')[1:]

    result = '\n'.join(line)

    print(f"Строка в XML: \n\n{result}")


def xml_to_json(file_content):

    python_dict = xmltodict.parse(file_content)

    json_string = json.dumps(python_dict, indent=4)

    print(f"\nСтрока в JSON: \n\n{json_string}")


def xml_to_yaml(file_content):

    python_dict = xmltodict.parse(file_content)

    yaml_string = yaml.dump(python_dict)

    print(f"\nСтрока в YAML: \n\n{yaml_string}")


def yaml_to_xml(file_content):

    python_dict = yaml.load(file_content, Loader=SafeLoader)

    xml_string = xmltodict.unparse(python_dict, pretty=True)

    line = xml_string.split('\n')[1:]

    result = '\n'.join(line)

    print(f"\nСтрока в XML: \n\n{result}")


def yaml_to_json(file_content):

    python_dict = yaml.load(file_content, Loader=SafeLoader)

    json_string = json.dumps(python_dict, indent=4)

    print(f"\nСтрока в JSON: \n\n{json_string}")


def json_to_yaml(file_content):

    python_dict = json.loads(file_content)

    yml_string = yaml.dump(python_dict)

    print(f"\nСтрока в YAML: \n\n{yml_string}")


if args.informat == 'json' and args.outformat == 'xml':
    json_to_xml(file_content)
elif args.informat == 'xml' and args.outformat == 'json':
    xml_to_json(file_content)
elif args.informat == 'xml' and args.outformat == 'yaml':
    xml_to_yaml(file_content)
elif args.informat == 'yaml' and args.outformat == 'xml':
    yaml_to_xml(file_content)
elif args.informat == 'yaml' and args.outformat == 'json':
    yaml_to_json(file_content)
elif args.informat == 'json' and args.outformat == 'yaml':
    json_to_yaml(file_content)
else:
    print("Ошибка выбора!")
