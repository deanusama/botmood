from django.urls import path
from courses import views

urlpatterns = [
    path('', views.courses, name='courses-list'),
    path('<slug:slug>/', views.course_detail, name='detail-page'),

    path('instructor', views.instructor, name='instructor'),
    path('instructor/<int:id>/', views.instructor_detail, name='instructor-detail'),

]
