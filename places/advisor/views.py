from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PlaceInfo
from django.utils import timezone
from .forms import PlaceForm
from django.contrib import messages
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

def get_districts(request):
    county = request.GET.get('county', None)
    if county is not None:
        distinct_districts = PlaceInfo.objects.filter(county=county).values_list('district', flat=True).distinct()
        return JsonResponse({'districts': list(distinct_districts)})
    else:
        return JsonResponse({})

@csrf_exempt    
def filter_list(request):
    # Assuming YourPlaceModel is the model for your places
    places = PlaceInfo.objects.all()

    # Handle form submission for filtering
    if request.method == 'POST':
        county = request.POST.get('county', '')
        district = request.POST.get('district', '')
        place_type = request.POST.get('place_type', '')
        price_category = request.POST.get('price_category', '')
        loudness = request.POST.get('loudness', '')
        largegroup = request.POST.get('largegroup', '')
        alone = request.POST.get('alone', '')
        dateable = request.POST.get('dateable', '')
        kitchen = request.POST.get('kitchen', '')
        smoke = request.POST.get('smoke', '')
        door_policy = request.POST.get('door_policy', '')
        readable = request.POST.get('readable', '')
        workable = request.POST.get('workable', '')


        # Perform filtering based on form data
        # Adjust this part based on your model fields and filter requirements
        if county:
            places = places.filter(county=county)
        if district:
            places = places.filter(district=district)
        if place_type:
            places = places.filter(place_type=place_type)
        if price_category:
            places = places.filter(price_category=price_category)
        if loudness:
            places = places.filter(loudness=loudness)
        if largegroup:
            places = places.filter(largegroup=True)
        if alone:
            places = places.filter(alone=True)
        if dateable:
            places = places.filter(dateable=True)
        if kitchen:
            places = places.filter(kitchen=True)      
        if smoke:
            places = places.filter(smoke=True)
        if door_policy:
            places = places.filter(door_policy=True)
        if readable:
            places = places.filter(readable=True)
        if workable:
            places = places.filter(workable=True)  
    context = {
        'object_list': places,
        # Add other context variables as needed
    }
    return render(request, "advisor/filter-list.html", context)


def place_detail(request, slug):
    place = get_object_or_404(PlaceInfo, slug=slug)
    print(place.city)
    print(place.county)
    print(place.name)
    print(place.slug)
    return render(request, 'advisor/place-detail.html', {'place': place})


def create_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('list_places')
        else:
            # Form is not valid, show error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")  # Redirect to the place list page
    else:
        print('form is not valid')
        form = PlaceForm()

    return render(request, 'advisor/create-place.html', {'form': form})


