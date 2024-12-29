#!/usr/bin/env python3

import requests

import json

SUBSCRIPTION_KEY = "1C6gWseVhYHDy4Lfv8914bnLTgjVSK4hFOY2hbl5rorZPvY8fsGeJQQJ99ALACYeBjFXJ3w3AAAFACOGx4uM"

vision_service_address = "https://pythonimgeanalyzer.cognitiveservices.azure.com/"

address = vision_service_address + "analyze"

parameters  = {'visualFeatures':'Description,Color',
               'language':'en'}

image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, "rb").read()

headers    = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

response = requests.post(address, headers=headers, params=parameters, data=image_data)

response.raise_for_status()

results = response.json()
print(json.dumps(results))