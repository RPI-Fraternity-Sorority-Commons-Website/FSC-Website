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
admin.autodiscover()
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from IFC import views

urlpatterns = [
    # hook in admin site urls
    path("admin/", admin.site.urls),


    # IFC app URLs
    path("", views.simpleView("IFC/homepage.html"), name="home"),
    path("documents/", views.simpleView("IFC/documents.html"), name="documents"),
    path("calendar/", views.simpleView("IFC/calendar.html"), name="calendar"),
    path("leadership/", views.simpleView("IFC/leadership.html"), name="leadership"),
    path("recruitment/", views.simpleView("IFC/recruitment.html"), name="recruitment"),
    path("fall/", views.simpleView("IFC/fall.html"), name="fall"),
    path("spring/", views.simpleView("IFC/spring.html"), name="spring"),

    path("chapters/", views.ourChapters, name="chapters"),
    path('chapters/<str:chapter_name>/', views.chapter_detail, name="chapter_detail"),
    path("chapters/<str:chapter_name>/edit/", views.edit_chapter, name="edit_chapter"),

    path('selectChapter', views.select_chapter, name="select_chapter"),

    path('login/', views.user_login, name="user_login"),
    path('signup/', views.user_signup, name="user_signup"),
    path('logout/', views.user_logout, name="user_logout"),
    path('profile/', views.profileView.as_view(), name="view_profile"),
    path('upload/', views.upload_content, name='upload_content'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
