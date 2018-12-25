from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

# from django.http import HttpResponse

from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from .utils.rdfLoader import FusekiRdfLoader
from .utils.sparql import sparqlQuery

class Home(TemplateView):
    template_name = 'causknow/home.html'

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        FusekiClass = FusekiRdfLoader(name)
        context['fusekiResponse'] = FusekiClass.httpResponse()
        context['url'] = fs.url(name)
        
    return render(request, 'causknow/upload.html', context)

def SPARQLQuery(request):
    context = {}
    if request.method == 'POST':
        UserSparqlQuery = request.POST.get('usersparqlquery', None)
        SparqlUtils = sparqlQuery(UserSparqlQuery)
        context['sparqlResults'] = SparqlUtils.sparqlResults()  

        return render(request, 'causknow/results.html', context)
    else:
        return render(request, 'causknow/sparql.html')    


