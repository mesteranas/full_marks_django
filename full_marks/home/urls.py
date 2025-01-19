from django.urls import path
from . import views
urlpatterns=[
    path("",views.home_,name="homePage"),
    path("contect/",views.Contect,name="contect"),
    path("about/",views.about,name="about"),
    path("changeLanguage",views.changeLanguage,name="changeLanguage"),
    path("notes",views.notesCategoryView,name="notesCategory"),
    path("notes/new",views.newNotesCategory,name="newNotesCategory"),
    path("notes/<int:categoryID>",views.noteCategoryContent,name="noteCategoryContent"),
    path("notes/<int:categoryID>/new",views.newNote,name="newNote"),
    path("notes/<int:categoryID>/rename",views.renameNoteCategory,name="renameNoteCategory"),
    path("notes/<int:categoryID>/<int:noteID>",views.viewNote,name="viewNote"),
    path("notes/<int:categoryID>/<int:noteID>/edit",views.editNote,name="editNote"),
    path("notes/<int:categoryID>/<int:noteID>/delete",views.deleteNote,name="deleteNote"),
    path("notes/<int:categoryID>/delete",views.deleteNoteCategory,name="deleteNoteCategory"),
]