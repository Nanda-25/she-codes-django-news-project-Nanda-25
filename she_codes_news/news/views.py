from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from .models import NewsStory
from .forms import StoryForm
from users.models import CustomUser

#classe face field - similar to the functions from the tutorial
class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context
        
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeleteStoryView(DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')

class EditStoryView(UpdateView):
    model = NewsStory
    template_name = 'news/editStory.html'
    fields = ['title', 'pub_date', 'image_url', 'category', 'content']
    success_url = reverse_lazy('news:index')

class Authors(generic.ListView):
    template_name = 'news/authorSearch.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return CustomUser.objects.all()

    def get_context_data(self, **kwargs):
        query = self.request.GET.get("author")
        context = super().get_context_data(**kwargs)
        context['author_list'] = CustomUser.objects.all().order_by('username')
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        context['author_stories'] = NewsStory.objects.filter(author__username=query).order_by('-pub_date')
        return context