from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
import os
import json
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse, FileResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .forms import ChapterForm, SignUpForm
from django.contrib import messages
from django.conf import settings
from .forms import ChapterForm
from .models import Chapter


# class-based view abstreaction for views that simply render a template
def simpleView(template):
    return TemplateView.as_view(template_name=template)


# Requesting Webpages:
def ourChapters(request):
    chapters = Chapter.objects.all()
    return render(request, 'IFC/ourChapters.html', {'chapters': chapters})


def select_chapter(request):
    chapters = Chapter.objects.all()
    return render(request, 'IFC/select_chapter.html', {'chapters': chapters})


# @login_required
def chapter_detail(request, chapter_name):
    chapter_name = chapter_name.replace('-', ' ')
    chapter = get_object_or_404(Chapter, name=chapter_name)
    return render(request, 'IFC/Chapter_base.html', {'chapter': chapter})


# @login_required
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

        return render(request, 'IFC/chapterInfoEdit.html', {'form': form, 'chapter': chapter})
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
            return render(request, 'IFC/login.html', {'error': 'Invalid username or password'})
    return render(request, 'IFC/login.html')


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'IFC/signup.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')


class profileView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'IFC/profile.html'
    success_url = '/'

    def get_object(self):
        return self.request.user

def handleAcrFile(file, acr_std_id):
    path = os.path.join('media/accreditation', str(acr_std_id))

    fs = FileSystemStorage()
    fs.save(os.path.join(path, file.name), file)

def accreditation_upload(request):
    if request.method == 'POST':
        acr_section = request.POST.get('acr_section')
        file = request.FILES['file']
        
        handleAcrFile(file, acr_section)
        return redirect('/accreditation')

    else:
        acr_data_path = os.path.join(settings.BASE_DIR, 'IFC\\static\\IFC\\json\\accreditation.json')
        file = open(acr_data_path, 'r')
        acr_data = json.load(file)

        return render(request,"IFC/accreditation.html", {"acr_data": acr_data["1"]})
#    return render(request,"IFC/upload_file.html", {'acr_data': acr_data})

def accreditation_file_list(request):
    section = request.GET.get('sec', 'none')
    root_path = '/media/accreditation/'+str(section)+'/'
    os_path = str(settings.BASE_DIR) + root_path

    files = []
    #print("Path="+path)
    try:
        files = os.listdir(os_path)
    except FileNotFoundError:
        files = []

    print("Files b4:" + str(files))
    files = [x for x in files if x != "deleted"]
    print("Files after:" + str(files))

    return render(request, 'IFC/filelist.html', {'files':files, 'section':str(section)})

def accreditation_file_get(request):
    sec = str(request.GET.get('sec', 'none'))
    fname = str(request.GET.get('f', 'none'))
    root_path = '/media/accreditation/'+str(sec)+'/'
    os_path = str(settings.BASE_DIR) + root_path

    #get directory contents again for security check
    files = []
    try:
        files = os.listdir(os_path)
    except FileNotFoundError:
        files = []
    
    #security check
    if (fname in files):
        return FileResponse(open(os_path + fname, 'rb'), as_attachment=True, filename=fname)
    else:
        return redirect('/accreditation/list?sec=' + sec)

def accreditation_file_rm(request):
    sec = str(request.GET.get('sec', 'none'))
    fname = str(request.GET.get('f', 'none'))
    path = str(settings.BASE_DIR) + '/media/accreditation/' + sec + '/'
    #os.rename(path + fname, path + 'deleted/' + fname)
    os.remove(path + fname)
    return redirect('/accreditation/list?sec=' + sec)