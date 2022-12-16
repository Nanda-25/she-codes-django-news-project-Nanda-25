from django.urls import path
from .views import CreateAccountView, ProfileView, EditAccountView, AuthorsView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/', ProfileView.as_view(), name='profileView'),
    path('create-account/edit', EditAccountView.as_view(), name='editAccount'),
    path('view-authors', AuthorsView.as_view(), name='authors'),
]