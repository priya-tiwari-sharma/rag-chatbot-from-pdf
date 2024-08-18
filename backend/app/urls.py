from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.FileUploadView.as_view(), name="upload"),
    path("ask/", views.AskQueryView.as_view(), name="ask"),
    path("check_key/", views.OpenAIKeyView.as_view(), name="key"),
]