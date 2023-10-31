from django.contrib import admin
from django.urls import path

from app.views import *

urlpatterns = [
    path("", homepage),
    path("<str:team>/", team_viewer),
    path("admin/", admin.site.urls),
]
