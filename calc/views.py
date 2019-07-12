from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import FarmData
from .models import FarmDataJSON
from django.core.serializers import json
from django.core import serializers
# Create your views here.

def home(request):
    myData = FarmData.objects.all()
    myDataLIST = list(FarmData.objects.all())
    myData_time = list(map(str, list(FarmData.objects.values_list('time', flat=True))))
    myData_group = list(map(str, list(FarmData.objects.values_list('group', flat=True))))
    myData_variable = list(FarmData.objects.values_list('variable', flat=True))
    myData_value = list(FarmData.objects.values_list('value', flat=True))

    #json_serializer = json.Serializer()
    #json_serialized = json_serializer.serialize(myData)

    #print(json_serialized)
    #myJSON = JsonResponse(myDataLIST, safe=False)
    #myData = FarmDataJSON.objects.all()
    #myData_value = list(FarmDataJSON.objects.values_list('json', flat=True))
    #matrix = []
    #for i in range(len(myData_group)):
    #    matrix.append([myData_group[i], myData_variable[i], myData_value[i]])

    #print(matrix)
    # print(table)
    # print(myData_time, myData_group, myData_value, myData_variable)
    #return render(request, 'home.html', {'myData_group': myData_group, 'myData_value': myData_value, 'myData_variable': myData_variable, 'matix' : matrix})
    return render(request, 'home.html')

def getJSONdata(request):
    myData = FarmData.objects.all()
    print(serializers.serialize('json', myData))
    return JsonResponse(serializers.serialize('json', myData), safe=False)