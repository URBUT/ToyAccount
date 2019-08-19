import argparse
import sqlite3
import getopt
import json
import sys

def conn_db():
    conn = sqlite3.connect("test.db")

    cur=conn.cursor()
    cur.execute("INSERT INTO sample_tab VALUE (?, ?, ?)")

def changeToJson(listset):
    jsonString = json.dumps(listset)
    return jsonString

def parse(value):
    json_key = ["price", "pay_option", "purpose"]

    parsed = value.split(",")
    dictOfWords = {json_key[i]  : parsed[i] for i in range(0, len(parsed))}
    print(dictOfWords)
    jsonString = changeToJson(dictOfWords)
    print (jsonString)
    print (type(jsonString))

if __name__== '__main__':
    # main(sys.argv[1:])

    parse('16000,check,coffee')