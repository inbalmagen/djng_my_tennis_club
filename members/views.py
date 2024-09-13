from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from members.models import Member
from .models import Court
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

def courts(request):
    mycourts = Court.objects.all().values()  # Fetch data from the Court model
    template = loader.get_template('courts_page.html')
    context = {
        'mycourts': mycourts,
    }
    return HttpResponse(template.render(context, request))

def single_court(request, id):
  mycourts = Court.objects.get(id=id)
  template = loader.get_template('single_court.html')
  context = {
    'mycourts': mycourts,
  }
  return HttpResponse(template.render(context, request))

def occupy_court(request, court_id):
    court = Court.objects.get(id=court_id)
    court.Is_occupied = True
    court.save()
    return redirect('courts')  # Redirect back to the list of courts after occupying

def free_court(request, court_id):
    court = Court.objects.get(id=court_id)
    court.Is_occupied = False
    court.save()
    return redirect('courts')  # Redirect back to the list of courts after freeing

def main(request):
    return render(request, 'home_page.html')

