import json
import boto3
import os


def numTriangular(n):
	i = 1
	tri = 0
	while i <= n:
		tri = tri + i 
		i+=1
	return tri 

def handlertriangular(event, context):
    try:
        d = json.loads(event)
        val = int(d['val'])     
        return numTriangular(val)
    except Exception as e:
        print(e)
        return -1      