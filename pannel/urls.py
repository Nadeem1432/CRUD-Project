from django.urls import path
from . import views
urlpatterns = [
    path('', views.view, name = 'view' ),
    path('search/',views.search,name='search'),
    path('edit_student/<int:id>', views.edit_student, name = 'edit_student' ),
    path('delete_student/<int:id>', views.delete_student, name = 'delete_student' ),
    path('insert_student/', views.insert_student, name = 'insert_student' ),

]
