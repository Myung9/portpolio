from django.contrib import admin
from .models import Blog

# Register your models here.

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blog':blogs})

admin.site.register(Blog)