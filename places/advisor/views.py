from django.shortcuts import render, redirect

# Create your views here.
def home_page(request, *args, **kwargs):
    
	if not request.user.is_authenticated:
		return redirect("login-user")
    
	context = {}

	return render(request, "advisor/advisorhome.html", context)