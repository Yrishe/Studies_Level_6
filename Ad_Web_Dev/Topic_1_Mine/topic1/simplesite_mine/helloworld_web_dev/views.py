from django.shortcuts import render
from django.http import HttpResponse
# access models and import all databases
from .models import *


# Week 1
# fulfill request and return response
def index(request):
    response_string = Hello.objects.all()[0]
    return render(request, 'helloworld_web_dev/index.html', {'data': response_string})

# Week 2
def simple_view(request):
    # get all Address objects from the database
    addresses = Address.objects.all()
    # get the first address and its resident's name
    first_address = addresses[0] if addresses else None
    # return the person's name linked to the first address
    resident_name = str(first_address.resident)
    # create an HTML response string
    # html = "<html><head></head><body>Name : " + resident_name +"<br />Address: "+first_address.street_name+"</body></html>"
    return render(request, 'helloworld_web_dev/simple_view.html', {'address': first_address, 'name': resident_name})

