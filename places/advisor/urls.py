from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from accounts import views as account_view
from advisor import views as advisor

urlpatterns = [
    #path("", advisor.home_page, name="advisor"),
    path("", advisor.list_places, name="list_places"),
    path('address_autocomplete/', advisor.address_autocomplete, name='address_autocomplete'),
    path("get-districts/", advisor.get_districts, name="get-districts"),
    path("filter-list/", advisor.filter_list, name="filter-list"),
    path('create-place/', advisor.create_place, name='create-place'),
	path('<slug:slug>/', advisor.place_detail, name='place_detail'),
	# login-section
	path("auth/login/", LoginView.as_view
		(template_name="advisor/loginpage.html"), name="login-user"),
	path("auth/logout/", LogoutView.as_view(), name="logout-user"),
	path("accounts/signup/", account_view.SignUpView.as_view(), name="signup"),
]
