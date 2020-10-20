from django.contrib import admin
from .models import Article
from .models import Professor

admin.site.register(Article)
admin.site.register(Professor)