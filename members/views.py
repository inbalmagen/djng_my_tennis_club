from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from members.models import Member
from django.shortcuts import redirect

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def trainers(request):
    return render(request, 'trainers_page.html')



def main(request):
    return render(request, 'home_page.html')

