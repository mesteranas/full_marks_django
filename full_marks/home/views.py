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
@login_required
def questionsManigerSubjects(r):
    subjects=models.examSubject.objects.all().order_by("-name")
    return render(r,"questionsManager/subject.html",{"subjects":subjects})
@login_required
def questionsManagerNewSubject(r):
    if r.method=="POST":
        data=r.POST
        mdl=models.examSubject(name=data["name"])
        mdl.save()
        return redirect("questionsManigerSubjects")
    return render(r,"questionsManager/newSubject.html")
@login_required
def questionsManagerCategory(r,subjectID:int):
    subject=get_object_or_404(models.examSubject,pk=subjectID)
    categories=models.subjectCategory.objects.filter(subject=subject).order_by("-name")
    return render(r,"questionsManager/categories.html",{"subject":subject,"categories":categories})
@login_required
def questionsManagerNewCategory(r,subjectID):
    subject=get_object_or_404(models.examSubject,pk=subjectID)
    if r.method=="POST":
        data=r.POST
        mdl=models.subjectCategory(name=data["name"],text=data["text"],subject=subject)
        mdl.save()
        return redirect("questionsManagerCategory",subjectID=subjectID)
    return render(r,"questionsManager/newCategory.html")
@login_required
def questionsManagerRenameSubject(r,subjectID:int):
    subject=get_object_or_404(models.examSubject,pk=subjectID)
    if r.method=="POST":
        data=r.POST
        subject.name=data["name"]
        subject.save()
        return redirect("questionsManagerCategory",subjectID=subjectID)
    return render(r,"questionsManager/renameSubject.html",{"subject":subject})
@login_required
def questionsManagerDeleteSubject(r,subjectID:int):
    if r.method=="POST":
        mdl=get_object_or_404(models.examSubject,pk=subjectID)
        mdl.delete()
        return redirect("questionsManigerSubjects")
    return render(r,"questionsManager/deleteSubject.html")
@login_required
def questionsManagerQuestions(r,subjectID:int,categoryID:int):
    category=get_object_or_404(models.subjectCategory,pk=categoryID)
    questions=models.question.objects.filter(category=category).order_by("-title")
    return render(r,"questionsManager/questions.html",{"category":category,"questions":questions})
@login_required
def questionsManagerNewQuestion(r,subjectID:int,categoryID:int):
    if r.method=="POST":
        data=r.POST
        category=get_object_or_404(models.subjectCategory,pk=categoryID)
        mdl=models.question(title=data["title"],correctAnswer=data["correctAnswer"],otherAnswers=data["otherAnswers"],category=category)
        mdl.save()
        return redirect("questionsManagerQuestions",subjectID=subjectID,categoryID=categoryID)
    return render(r,"questionsManager/newQuestion.html")
@login_required
def questionsManagerEditOrDeleteQuestion(r,subjectID:int,categoryID:int,questionID:int):
    question=get_object_or_404(models.question,pk=questionID)
    if r.method=="POST":
        data=r.POST
        if data["type"]=="edit":
            question.title=data["title"]
            question.correctAnswer=data["correctAnswer"]
            question.otherAnswers=data["otherAnswers"]
            question.save()
        elif data["type"]=="delete":
            question.delete()
        return redirect("questionsManagerQuestions",subjectID=subjectID,categoryID=categoryID)
    return render(r,"questionsManager/editQuestion.html",{"question":question})
@login_required
def questionsManagerDeleteCategory(r,subjectID:int,categoryID:int):
    if r.method=="POST":
        category=get_object_or_404(models.subjectCategory,pk=categoryID)
        category.delete()
        return redirect("questionsManagerCategory",subjectID=subjectID)
    return render(r,"questionsManager/deleteCategory.html")
@login_required
def questionsManagerEditCategory(r,subjectID:int,categoryID:int):
    category=get_object_or_404(models.subjectCategory,pk=categoryID)
    if r.method=="POST":
        data=r.POST
        category.name=data["name"]
        category.text=data["text"]
        category.save()
        return redirect("questionsManagerQuestions",subjectID=subjectID,categoryID=categoryID)
    return render(r,"questionsManager/editCategory.html",{"category":category})
