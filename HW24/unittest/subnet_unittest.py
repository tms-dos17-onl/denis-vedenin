#!/usr/bin/python3

import unittest
import argparse  # argparse— Анализатор параметров командной строки, аргументов и подкоманд

import ipaddress  # from ipaddress import IPv4Address, IPv4Network

ip = input("Введи ip: ")
cidr_mask = input("Введи маску: ")


def calculate_subnet(ip, cidr_mask):
    network = ipaddress.IPv4Network(ip + cidr_mask, strict=False)
    subnet_address = str(network.network_address)
    subnet_mask = str(network.netmask)
    first_host = str(network.network_address + 1)
    last_host = str(network.broadcast_address - 1)
    broadcast_address = str(network.broadcast_address)
    subnet_class = get_subnet_class(network)

    return subnet_address, subnet_mask, first_host, last_host, broadcast_address, subnet_class

# Создаем функцию для нахождения класса сети


def get_subnet_class(network):
    first_octet = int(network.network_address.exploded.split('.')[0])

    if 1 <= first_octet <= 128:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    elif 224 <= first_octet <= 239:
        return 'D'
    elif 240 <= first_octet <= 255:
        return 'E'


# parser = argparse.ArgumentParser(description='Subnet Calculator')
# # Позиционные аргументы
# parser.add_argument('--ip', type=str, help='IP address')
# parser.add_argument('--cidr_mask', default='Not values', help='CIDR mask')
# args = parser.parse_args()

# ip = ipaddress.IPv4Address(args.ip)
# cidr_mask = args.cidr_mask

subnet_address, subnet_mask, first_host, last_host, broadcast_address, subnet_class = calculate_subnet(
    str(ip), cidr_mask)

print("Адрес подсети:: " + subnet_address)
print("Маска подсети: " + subnet_mask)
print("IP адрес первого хоста: " + first_host)
print("IP адрес последнего хоста: " + last_host)
print("Широковещательный адрес: " + broadcast_address)
print("Класс подсети: " + subnet_class)


class SubnetTest(unittest.TestCase):

    def test_ip(self):
        self.assertTrue(ip, "ok")
    print("Тест показал ip равен: ", ip)

    def test_cidr_mask(self):
        self.assertIsNotNone(cidr_mask, "ok")
    print("Тест показал ip равен: ", cidr_mask)


if __name__ == '__main__':
    SubnetTest()
