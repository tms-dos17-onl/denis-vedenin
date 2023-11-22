#!/usr/bin/python3

import argparse
import json
import xmltodict
import yaml
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='converter')
    parser.add_argument("--infile", help="file name",
                        type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument(
        "--informat", choices=['json', 'xml', 'yaml'], help="format import file")
    parser.add_argument(
        "--outformat", choices=['json', 'xml', 'yaml'], help="format output file")
    args = parser.parse_args()

    if args.informat == "xml":
        file_in = xmltodict.parse(args.infile.read())
        # print(xml_forma)
    elif args.informat == "json":
        file_in = json.load(args.infile)
        # print(json_forma)
    elif args.informat == "yaml":
        file_in = yaml.load(args.infile, Loader=yaml.SafeLoader)
        # print(yaml_forma)

    if args.outformat == "xml":
        file_out = xmltodict.unparse(file_in, pretty=True)
        print(file_out)
    elif args.outformat == "json":
        file_out = json.dumps(file_in, indent=4)
        print(file_out)
    elif args.outformat == "yaml":
        file_out = yaml.dump(file_in)
        print(file_out)
