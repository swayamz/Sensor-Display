from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import FarmData
from .models import FarmDataJSON
from django.core.serializers import json
from django.core import serializers
# Create your views here.

def home(request):
    getLatestTime = FarmData.objects.values_list('time', flat=True).latest('id')
    #myData = FarmData.objects.all().filter(time='19 Jul 2019 11:19:26')
   ##myData_time = list(map(str, list(FarmData.objects.values_list('time', flat=True).filter(time='19 Jul 2019 11:19:26'))))
   # myData_group = list(map(str, list(FarmData.objects.values_list('x', flat=True).filter(time='19 Jul 2019 11:19:26'))))
   # myData_variable = list(FarmData.objects.values_list('y', flat=True).filter(time='19 Jul 2019 11:19:26'))
    #myData_value = list(FarmData.objects.values_list('value', flat=True).filter(time='19 Jul 2019 11:19:26'))

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
    return render(request, 'home.html', {'latestTime' : getLatestTime})

def getJSONdata(request):
    getLatestTime = FarmData.objects.values_list('time', flat=True).latest('id')
    myData = FarmData.objects.all().filter(time=getLatestTime)
    print(serializers.serialize('json', myData))
    return JsonResponse(serializers.serialize('json', myData), safe=False)

