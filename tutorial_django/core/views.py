from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bom dia boa tarde e boa noite</h1>")