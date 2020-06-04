# !/usr/bin/python
# -*-coding:utf-8 -*-

import os
# read in key and certificate

# sk: server.key
# sc: server.crt
# ck: client.key
# cc: client.crt
def load(word):
    if word == "sk":
        with open('secrets/server.key', 'rb') as f:
            private_key = f.read()
            return private_key
    elif word == "sc":
        with open('secrets/server.crt', 'rb') as f:
            certificate_chain = f.read()
            return certificate_chain
    if word == "ck":
        with open('secrets/client.key', 'rb') as f:
            private_key = f.read()
            return private_key
    elif word == "cc":
        with open('secrets/client.crt', 'rb') as f:
            certificate_chain = f.read()
            return certificate_chain
