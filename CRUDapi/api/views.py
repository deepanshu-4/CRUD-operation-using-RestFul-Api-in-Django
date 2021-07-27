from .models import Student
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseNotFound
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io
@csrf_exempt
def add(request):
	if(request.method=='POST'):
		json_data=request.body
		stream=io.BytesIO(json_data)
		parsed_data=JSONParser().parse(stream)
		serializer=StudentSerializer(data=parsed_data)
		if serializer.is_valid():
			serializer.save()
			res={'msg':'data created'}
			json_data=JSONRenderer().render(res)
			return HttpResponse(json_data,content_type='application/json')
		json_data=JSONRenderer().render(serializer.errors)
		return HttpResponse(json_data,content_type='application/json')
	return HttpResponseNotFound("<h1>BAD request 404</h1>")		


def read(request):
	try:

		json_data=request.body
		stream=io.BytesIO(json_data)
		pythondata=JSONParser().parse(stream)
		print(pythondata)
		id=pythondata.get('id',None)
		if id is not None:
			stu=Student.objects.get(id=id)
			serializer=StudentSerializer(stu)
			json_data=JSONRenderer().render(serializer.data)
			return HttpResponse(json_data,content_type='application/json')
		stu=Student.objects.all()
		serializer=StudentSerializer(stu,many=True)
		json_data=JSONRenderer().render(serializer.data)
		return HttpResponse(json_data,content_type='application/json')	
	except:
		return HttpResponseNotFound("<h1>BAD request 404</h1>")

