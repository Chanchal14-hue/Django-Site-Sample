from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Chanchal Admin"
admin.site.site_title = "Chanchal Admin Portal"
admin.site.index_title = "Welcome to Chanchal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
