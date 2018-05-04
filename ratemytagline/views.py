from django.shortcuts import render
from django.http import Http404
from . models import tagLine

def index(request):
    if request.POST:
        tagLine(tagline = request.POST.get("tagline",""),username = request.POST.get("name","")).save()
    taglinesList = tagLine.objects.all()
    context = {'taglines':taglinesList}
    return render(request,'ratemytagline/index.html',context)

def detail(request,id):
    try:
        tagline = tagLine.objects.get(pk = id)
    except:
        raise Http404("Tagline does not exist")
    if request.POST:
        tagline.numberOfVotes += 1
        tagline.save()
    return render(request,'ratemytagline/details.html',{'tagline':tagline})
