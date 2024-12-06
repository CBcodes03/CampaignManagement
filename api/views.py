from rest_framework import viewsets 
from .models import Agent, Campaign, CampaignResult
from .serializers import AgentSerializer, CampaignSerializer, CampaignResultSerializer
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to Campaign Management API"})

#creating viewsets for each api this will save us time as we wont have to write view for each operarion
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()#all here means the data api interacts with
    serializer_class = AgentSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class CampaignResultViewSet(viewsets.ModelViewSet):
    queryset = CampaignResult.objects.all()
    serializer_class = CampaignResultSerializer
