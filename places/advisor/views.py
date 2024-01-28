from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import PlaceInfo
from django.utils import timezone
# Create your views here.
def home_page(request, *args, **kwargs):
    
	if not request.user.is_authenticated:
		return redirect("login-user")
    
	context = {}

	return render(request, "advisor/advisorhome.html", context)

@login_required(login_url='auth/login/')
def list_places(request):
    qs = PlaceInfo.objects.all()
	# Get distinct counties and districts
    distinct_counties = PlaceInfo.objects.values_list('county', flat=True).distinct()
    distinct_districts = PlaceInfo.objects.values_list('district', flat=True).distinct()

    context={
        "object_list":qs,
		"distinct_counties":distinct_counties,
		"distinct_districts":distinct_districts,
    }
    
    return render(request, "advisor/advisorhome.html", context=context)
