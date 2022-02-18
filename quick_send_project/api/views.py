import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import Address
from django.utils import timezone
import datetime
import utils
import qrcode
import io

#o is any object
#fields is an array of strings representing field names
#This function creates a new dictionary consisting of only the fields in o
def copy_fields(o, fields):
  return_object = {}
  for field in fields:
    return_object[field] = o[field]
  return return_object

#Returns true if the address is already in the database
def check_db_for_address(collection, address):
  if collection.find_one({'address': address}):
    return True
  else:
    return False

#Obtain information about the address passed in and returns the information as a JSON serializable object
def fetch_address_information(collection, address):
  url = 'https://api.blockcypher.com/v1/btc/test3/addrs/' + address
  request = requests.get(url)
  json_output = request.json()
  new_data = {
    "address": json_output['address'],
    "balance": json_output['balance'],
    "final_balance" : json_output['final_balance'],
    "final_n_tx" : json_output['final_n_tx'],
    "n_tx" : json_output['n_tx'],
    "total_received" : json_output['total_received'],
    "total_sent" : json_output['total_sent'],
    "unconfirmed_balance" : json_output['unconfirmed_balance'],
    "unconfirmed_n_tx" : json_output['unconfirmed_n_tx'],
    "last_updated" : timezone.now()
  }

  #if the address is already in the database, perform an update, otherwise insert a new record
  if check_db_for_address(collection, address):
    collection.update_one({'address':address}, {"$set":new_data})
  else:
    collection.insert_one(new_data)

  return json_output

def lookup(request, address):
  #json is the json string that will be returned by the end of this function
  json_output = None
  fields_to_copy = ['address','balance','final_balance','final_n_tx','n_tx','total_received','total_sent','unconfirmed_balance','unconfirmed_n_tx']

  collection = utils.get_default_collection()

  if check_db_for_address(collection, address):
    #retrieve information from database
    record = collection.find_one({'address': address})
    half_an_hour = datetime.timedelta(minutes=30)
    now = datetime.datetime.now()
    half_an_hour_ago = now - half_an_hour

    print(record['last_updated'])
    print(half_an_hour_ago)
    if record['last_updated'] < half_an_hour_ago:
      #Last updated over half an hour ago. Fetch information from website
      json_output = fetch_address_information(collection, address)
      print('Fetch from live')
    else:
      #Retrieve information from database
      json_output = copy_fields(record, fields_to_copy)
      print('Database hit')
  else:
    #record not found. Retreive information from ledger and insert into database
    print('Fetched from live')
    json_output = fetch_address_information(collection, address)

  return JsonResponse(json_output)

def generate_qr_code(request,address):
  data = 'http://localhost:8000/wallets/lookup/' + address
  
  # Encoding data using make() function
  img = qrcode.make(data)
  output = io.BytesIO()
  img.save(output, format='JPEG')
  return HttpResponse(output.getbuffer(), content_type="image/jpeg")