from string import Template

from django.shortcuts import render
from django.http import HttpResponse
from utils import get_default_collection
from django.template import loader
#from blockcypher import get_address_overview
#from pycurl import Curl
#import pycurl
#from io import BytesIO
import requests

def send(request):
	template = loader.get_template('send/send.html')
	context = {}

	return HttpResponse(template.render(context,request))

def lookup(request, address=''):
	template = loader.get_template('send/lookup.html')

	address_information = ''
	#if address != '':
	#	address_information = requests.get('http://localhost:8000/api/lookup/' + address)

	#print(address_information)
	context = {'address': address, 'address_information': address_information}

	return HttpResponse(template.render(context,request))

def index(request):
	template = loader.get_template('send/index.html')
	collection = get_default_collection()
	addresses = collection.find({})
	context = {'addresses':addresses}

	return HttpResponse(template.render(context,request))
	#	amount_in_satoshis = r.json()['final_balance']
	#amount = get_address_overview('tb1qqkz98e04vakzrprqlehqr46hmx9a98jh586al6')
	#print(amount)
	#	contents = '''
	#<!DOCTYPE HTML>
	#<html>
	#<head></head>
	#<body>
	#Wallet amount: $AMOUNT<br>
	#<label for='send_amount'>send amount<input id='send_amount'></label>
	#</body>
	#</html>
	#	'''
	#template = Template(contents)
	#output_string = template.substitute(AMOUNT=amount_in_satoshis)

