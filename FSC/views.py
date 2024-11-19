from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .forms import ChapterForm, SignUpForm
from .models import Chapter
from django.contrib import messages
from .models import Upload
from .forms import UploadForm

# class-based view abstreaction for views that simply render a template
def simpleView(template_name):
    def view_func(request):
        if template_name == "FSC/feed.html":
            # If it's the feed, include posts
            posts = Upload.objects.all().order_by('-created_at')
            return render(request, template_name, {'posts': posts})
        return render(request, template_name)
    return view_func

def home(request):
    posts = Upload.objects.all().order_by('-created_at')
    return render(request, 'FSC/feed.html', {'posts': posts})

# Requesting Webpages:
def ourChapters(request):
    ifc_chapters = sorted(Chapter.objects.filter(council="ifc"), key=lambda ch: ch.name)
    panhel_chapters = sorted(Chapter.objects.filter(council="panhel"), key=lambda ch: ch.name)
    msfc_chapters = sorted(Chapter.objects.filter(council="msfc"), key=lambda ch: ch.name)
    pfs_chapters = sorted(Chapter.objects.filter(council="pfs"), key=lambda ch: ch.name)
    return render(request, 'FSC/ourChapters.html', {'ifc_chapters': ifc_chapters, "panhel_chapters": panhel_chapters, "msfc_chapters": msfc_chapters, 'pfs_chapters': pfs_chapters})


def select_chapter(request):
    chapters = Chapter.objects.all()
    return render(request, 'FSC/select_chapter.html', {'chapters': chapters})


# @login_required
def chapter_detail(request, chapter_name):
    chapter_name = chapter_name.replace('-', ' ')
    chapter = get_object_or_404(Chapter, name=chapter_name)
    return render(request, 'FSC/Chapter_base.html', {'chapter': chapter})


@login_required
def edit_chapter(request, chapter_name):

    # Get the chapter by ID (or use some other logic to assign chapters to users)
    chapter_name = chapter_name.replace('-', ' ')
    chapter = get_object_or_404(Chapter, name=chapter_name)

    if request.user.is_authenticated and request.user.affiliation == chapter_name:

        # Ensure the user is authorized to edit this chapter (this depends on your user model/permissions setup)
        # You might need to compare request.user with the user related to the chapter

        if request.method == 'POST':
            form = ChapterForm(request.POST, request.FILES, instance=chapter)
            if form.is_valid():
                form.save()
                return redirect("/chapters/" + chapter.name + "/")
        else:
            form = ChapterForm(instance=chapter)

        return render(request, 'FSC/chapterInfoEdit.html', {'form': form, 'chapter': chapter})
    else:
        return redirect("/chapters/" + chapter.name + "/")


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'FSC/login.html', {'error': 'Invalid username or password'})
    return render(request, 'FSC/login.html')


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'FSC/signup.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')


class profileView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'FSC/profile.html'
    success_url = '/'

    def get_object(self):
        return self.request.user

@login_required
def upload_content(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.save()
            messages.success(request, 'Content uploaded successfully!')
            return redirect('home')
    else:
        form = UploadForm()
    
    return render(request, 'FSC/upload.html', {'form': form})