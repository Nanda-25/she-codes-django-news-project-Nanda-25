from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(),name='newStory'),
    path('story/<int:pk>/delete', views.DeleteStoryView.as_view(), name='deleteStory'),
    path('story/<int:pk/edit', views.EditStoryView.as_view(), name='editStory'),
    path('author-search/', views.Authors.as_view(), name='authorSearch')

]

#django never you give the same number for a storie.