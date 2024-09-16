from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from courts.models import Court, CourtOrder
from members.models import Member  # Import the Member model
from .forms import CourtOrderForm  # Import the form for reserving a courtfrom members.models import Member  # Import the Member model


# Show the list of courts
def courts(request):
    mycourts = Court.objects.all().values()  # Fetch data from the Court model
    template = loader.get_template('courts_page.html')
    context = {
        'courts': mycourts,
    }
    return HttpResponse(template.render(context, request))

# Reserve a court with two members
def reserve_court(request):
    if request.method == 'POST':
        form = CourtOrderForm(request.POST)
        if form.is_valid():
            court_order = form.save(commit=False)
            court_order.start_time = timezone.now()
            court_order.save()

            # Mark the court as occupied
            court_order.court.is_occupied = True
            court_order.court.time_of_occupation = timezone.now()
            court_order.court.save()

            return redirect('court_order_list')  # Redirect to the list of court orders
    else:
        form = CourtOrderForm()

    return render(request, 'reserve_court.html', {'form': form})

# View the court orders (occupied courts and members)
def court_order_list(request):
    # Fetch all available courts and members
    courts = Court.objects.filter(is_occupied=False)  # Only show available courts
    members = Member.objects.all()

    context = {
        'courts': courts,
        'members': members,
    }
    
    return render(request, 'court_order.html', context)


# Manually reserve/unreserve courts (similar to your original view)
def reserve(request, id):
  court = Court.objects.get(id=id)
  court.is_occupied = not court.is_occupied
  court.save()
  return redirect('/courts/')

# Show details for a single court
def single_court(request, id):
  mycourts = Court.objects.get(id=id)
  template = loader.get_template('single_court.html')
  context = {
    'mycourts': mycourts,
  }
  return HttpResponse(template.render(context, request))

# Mark a court as occupied (for your existing functionality)
def occupy_court(request, court_id):
    court = Court.objects.get(id=court_id)
    court.Is_occupied = True
    court.save()
    return redirect('courts')  # Redirect back to the list of courts after occupying

# Mark a court as free
def free_court(request, court_id):
    court = Court.objects.get(id=court_id)
    court.Is_occupied = False
    court.save()
    return redirect('courts')  # Redirect back to the list of courts after freeing