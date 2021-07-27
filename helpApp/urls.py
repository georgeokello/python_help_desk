# imports
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('solution',views.solution, name='solution'),
    path('details/<int:pk>', views.details, name='details'),
    path('delete_problem/<int:pk>', views.delete_problem, name='delete_problem'),
    path('edit_problem/<int:pk>', views.edit_problem, name='edit_problem'),
    path('delete_solution/<int:pk>', views.delete_solution, name='delete_solution'),
    path('edit_solution/<int:pk>', views.edit_solution, name='edit_solution'),
    path('signup', views.signup, name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout')
]