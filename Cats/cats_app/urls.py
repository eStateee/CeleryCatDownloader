from django.urls import path
from cats_app.views import cat_view
urlpatterns = [
    path('', cat_view, name='cats')
]
