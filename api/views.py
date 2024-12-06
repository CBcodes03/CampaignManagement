from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Agent, Campaign, CampaignResult
from .serializers import AgentSerializer, CampaignSerializer, CampaignResultSerializer
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to Campaign Management API"})
# Agent pagination
class AgentPagination(PageNumberPagination):
    page_size = 5  # Number of agents per page
    page_size_query_param = 'page_size'  # Allow users to specify page size
    max_page_size = 100  # Max limit for page size

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    pagination_class = AgentPagination  # Use custom pagination


# Campaign pagination
class CampaignPagination(PageNumberPagination):
    page_size = 5  # Number of campaigns per page
    page_size_query_param = 'page_size'  # Allow users to specify page size
    max_page_size = 100  # Max limit for page size

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    pagination_class = CampaignPagination  # Use custom pagination


class CampaignResultViewSet(viewsets.ModelViewSet):
    queryset = CampaignResult.objects.all()
    serializer_class = CampaignResultSerializer
