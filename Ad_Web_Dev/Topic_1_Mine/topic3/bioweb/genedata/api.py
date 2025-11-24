from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

@csrf_exempt
def gene_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        gene = Gene.objects.get(pk=pk)
    except Gene.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = GeneSerializer(gene)
        return JsonResponse(serializer.data)