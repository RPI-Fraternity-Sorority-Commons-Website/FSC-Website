"""IFC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from IFC import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # IFC app URLs
    path("", views.homepage, name="home"),
    path("documents/", views.documents, name="documents"),
    path("calendar/", views.calendar, name="calendar"),
    path("leadership/", views.leadership, name="leadership"),
    path("recruitment/", views.recruitment, name="recruitment"),
    path("fall/", views.fall, name="fall"),
    path("spring/", views.spring, name="spring"),
    path("event-schedule/", views.eventSchedule, name="event-schedule"),

    path("chapters/", views.ourChapters, name="chapters"),
    path('chapters/<slug:chapter_name>/', views.chapter_detail, name="chapter_detail"),
    path("chapters/<slug:chapter_name>/edit/", views.edit_chapter, name="edit_chapter"),

    path('selectChapter', views.select_chapter, name="select_chapter"),
    path('chapterInfoEdit', views.chapterInfoEdit, name="chapterInfoEdit")
]
