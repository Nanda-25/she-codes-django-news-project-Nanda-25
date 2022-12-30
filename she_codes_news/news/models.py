from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
        )

    # author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField(blank=True)

    # def get_absolute_url(self):
    #     return reverse('news:story', kwargs={'pk': self.pk}))

# categories = (
#         ('FUN', 'Fun'),
#         ('MUSIC', 'Music'),
#         ('MOVIES', 'Movies'),
#         ('EDUCATION', 'Education'),
#         ('SCIENCE', 'Science'),
#         ('TECHNOLOGY', 'Technology'),
#         ('ANIMALS', 'Animals'),
#         ('FOOD', 'Food'),
#     )
#     category = models.CharField(max_length=200, choices = categories, default='news')