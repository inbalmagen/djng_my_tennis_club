from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render

from courts.models import Court

# Create your views here.
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