from django.urls import path
from .controllers import HelloWorld

urlpatterns = [
    path("hello/", HelloWorld.as_view(), name="hello_world"),
]
