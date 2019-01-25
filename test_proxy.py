#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests

message = "Je suis au café."
d = dict(message=message)

print(type(message))
print(message)
print(type(d))
print(d)
print(type(d['message']))
print(d['message'])
s = json.dumps(d)
print(type(s))
print(s)
d = json.loads(s)
print(d)
print(type(d['message']))
print(d['message'])
