from django.http import HttpResponse

# Create your views here.

def index(request):
     return HttpResponse("You're are viewing Index page of DECISION MAKER")