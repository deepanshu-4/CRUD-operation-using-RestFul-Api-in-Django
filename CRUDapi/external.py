import requests
import json
def create():
	ur="http://127.0.0.1:8000/add/"
	data={
		'name':'D',
		'rno':1,
		'city':'Haryana'
	}
	json_data=json.dumps(data)
	r=requests.post(url=ur,data=json_data)
	data=r.json()
	print(data)

def read(id=None):
	ur="http://127.0.0.1:8000/read/"
	data={}
	if id is not None:
		data={'id':id}
	json_data=json.dumps(data)	
	r=requests.get(url=ur,data=json_data)
	print(r.json())

	
while(True):

	x=int(input("Enter choice\n 1. create 2.read 3.read with id "))
	if(x==1):
		create()
	elif(x==2):
		read()
	elif(x==3):
		id=int(input("Enter id "))
		read(id)	
	else:
		break;	