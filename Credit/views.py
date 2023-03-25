from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Credit.models import Demande,agent_de_verification
from Credit.serializers import DemandeSerializer,agent_de_verificationSerializer
# Create your views here.

@csrf_exempt
def demandeApi(request,id=0):
    if request.method=='GET':
        demande=Demande.objects.all()
        demande_serializer=DemandeSerializer(demande,many=True)
        return JsonResponse(demande_serializer.data, safe=False )
    
    elif request.method=='POST':
        demande_data=JSONParser().parse(request) 
        demande_serializer=DemandeSerializer(data=demande_data)
        if demande_serializer.is_valid():
            demande_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method=='PUT':
        demande_data=JSONParser().parse(request)
        demande=Demande.objects.get(DemandeId=demande_data['DemandeId'])
        demande_serializer=DemandeSerializer(demande,data=demande_data)
        if demande_serializer.is_valid():
            demande_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update", saf=False)
    
    elif request.method=='DELETE':
        demande=Demande.objects.get(DemandeId=id)
        demande.delete()
        return JsonResponse("Deleted Successfully!", safe=False)

@csrf_exempt
def agent_de_verificationApi(request, id=0):
    if request.method == 'GET':
        Agent_de_verification = agent_de_verification.objects.all()
        agent_de_verification_serializer = agent_de_verificationSerializer(
            Agent_de_verification, many=True)
        return JsonResponse(agent_de_verification_serializer.data, safe=False)
    elif request.method == 'POST':
        agent_de_verification_data = JSONParser().parse(request)
        agent_de_verification_serializer = agent_de_verificationSerializer(
            data=agent_de_verification_data)
        if agent_de_verification_serializer.is_valid():
            agent_de_verification_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        agent_de_verification_data = JSONParser().parse(request)
        Agent_de_verification = agent_de_verification.objects.get(
            idAgent_de_verification=agent_de_verification_data['idAgent_de_verification'])
        agent_de_verification_serializer = agent_de_verificationSerializer(
            Agent_de_verification, data=agent_de_verification_data)
        if agent_de_verification_serializer.is_valid():
            agent_de_verification_serializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('Failed to Update')
    elif request.method == 'DELETE':
        Agent_de_verification = agent_de_verification.objects.get(
            idAgent_de_verification=id)
        Agent_de_verification.delete()
        return JsonResponse('Deleted Successfully', safe=False)
