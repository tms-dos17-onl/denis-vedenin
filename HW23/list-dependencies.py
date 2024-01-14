#!/usr/bin/python3
import requests
import argparse

parser = argparse.ArgumentParser(description='list-dependencies')
parser.add_argument("--package", help="package list ")
args = parser.parse_args()

NamePackage = args.package

response = requests.get("https://pypi.org/pypi/" + NamePackage + "/json")

for dep in response.json()['info']['requires_dist']:
    print(dep)
