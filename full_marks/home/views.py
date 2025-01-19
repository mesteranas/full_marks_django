from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _,activate
from . import forms,models

# Create your views here.
def home_(r):
    if r.method=="POST":
        data=r.POST
        userModel=auth.authenticate(username=data["username"],password=data["password"])
        if userModel:
            auth.login(r,userModel)
    return render(r,"home.html")
def Contect(r):
    return render(r,"contect.html")
def about(r):
    return render(r,"about.html")
def changeLanguage(r):
    if r.method=="POST":
        language=r.POST["language"]
        activate(language)
        return redirect("homePage")
    return render(r,"changeLanguage.html")
@ login_required
def notesCategoryView (r):
    categories=models.notesCategory.objects.all().order_by("-name")
    return render(r,"notesCategory.html",{"categories":categories})
@login_required
def newNotesCategory(r):
    if r.method=="POST":
        data=r.POST
        mdl=models.notesCategory(name=data["name"])
        mdl.save()
        return redirect("notesCategory")
    return render(r,"newCategory.html")
@login_required
def noteCategoryContent(r,categoryID:int):
    category=get_object_or_404(models.notesCategory,pk=categoryID)
    notes=models.notesContent.objects.filter(category=category).order_by("-date")
    return render(r,"noteCategoryContent.html",{"categoryName":category.name,"notes":notes,"ID":categoryID})
@login_required
def newNote (r,categoryID):
    if r.method=="POST":
        data=r.POST
        category=get_object_or_404(models.notesCategory,pk=categoryID)
        mdl=models.notesContent(name=data["name"],content=data["content"],category=category)
        mdl.save()
        return redirect("noteCategoryContent",categoryID=categoryID)
    return render(r,"newNote.html")
@login_required
def renameNoteCategory(r,categoryID:int):
    category=get_object_or_404(models.notesCategory,pk=categoryID)
    if r.method=="POST":
        data=r.POST
        category.name=data["name"]
        category.save()
        return redirect("noteCategoryContent",categoryID=categoryID)
    return render(r,"renameCategory.html",{"category":category})
@login_required
def viewNote(r,categoryID:int,noteID:int):
    note=get_object_or_404(models.notesContent,pk=noteID)
    return render(r,"viewNote.html",{"note":note})
@login_required
def editNote(r,categoryID:int,noteID:int):
    note=get_object_or_404(models.notesContent,pk=noteID)
    if r.method=="POST":
        data=r.POST
        note.name=data["name"]
        note.content=data["content"]
        note.save()
        return redirect("viewNote",categoryID=categoryID,noteID=noteID)
    return render(r,"editNote.html",{"note":note})
@login_required
def deleteNote(r,categoryID:int,noteID:int):
    if r.method=="POST":
        note=get_object_or_404(models.notesContent,pk=noteID)
        note.delete()
        return redirect("noteCategoryContent",categoryID=categoryID)
    return render(r,"deleteNote.html")
@login_required
def deleteNoteCategory(r,categoryID:int):
    if r.method=="POST":
        category=get_object_or_404(models.notesCategory,pk=categoryID)
        category.delete()
        return redirect("notesCategory")
    return render(r,"deleteCategory.html")