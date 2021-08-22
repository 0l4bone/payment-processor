from requests.api import head
from square.client import Client
from square.configuration import Configuration
import os
import sys

import boto3
from faker import Faker
from huepy import *
from time import sleep
import sys
import hashlib
from django.db import connection

import sqlite3
from sqlite3 import Error
import requests

# This code is open and you can edit All you need 

password = "osbkkjqemNQl1q"
hostname = "127.0.0.1"

client = Client(
    access_token="hVBlQMN1XtphPosbkkjqemNQl1qbWsEP3xTHwTuT",
)

customerApi = client.customers 

result = customerApi.list()

commands = []

def exec():
    if result.success():
        fake = Faker()
        print(result.body)
        #Store file each customer
        password = hashlib.md5(str.encode(fake.password())).hexdigest()
        commands[0] = "echo {}".format(result.body['customerName'])
        commands[1] = ">> {}".format("customers.d4a")
        commands[2] = " && "
        commands[3] = "chmod 777 {}".format("customers.d4a")
        command = commands[0]+commands[1]+commands[2]+commands[3]
        exec(command)
        return password
    elif result.error():
        print(result.errors)

def transformData():
    #TODO
    return True

def getCustomers(data):
    internalToken = "EP3xTHwTuTjqemNQlosbkkjqemNQl1q1qbWshVBlQMN1XtphPosEP3x"

    access={
        "token": internalToken,
        "user": "superadmin",
        "role": "administrator"
    }
    headers = {
        "Content-Type": "application/json"
    }
    customers = requests.post('https://' + hostname + '/api/scans', json=access, headers=headers,verify=False)

    for customer in customers:
        transformData(customer['name'], customer['card'])

def createNewCustomer(customer):
    curs = connection.cursor()
    name = customer['name']
    card = customer['card']
    id = customer['id']
    curs.execute("insert into customers ('name','card','id') values ('%s','%s',%s)" %(name, card, id))

exec()

