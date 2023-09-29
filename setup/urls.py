
from django.contrib import admin
from django.urls import path

from app.views import product, subgroup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', product),
    path('subgroup/', subgroup),

]
