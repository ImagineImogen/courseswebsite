from django.urls import path
from .views import CourseListView, CourseDetailView, CourseDeleteView, CourseCreateView, CourseUpdateView

urlpatterns = [
    path('list', CourseListView.as_view(), name="course_list"),
    path('create/', CourseCreateView.as_view(), name='create_course'),
    path('<slug:slug>/delete', CourseDeleteView.as_view(), name='delete_course'),
    path('<slug:slug>/update', CourseUpdateView.as_view(), name='update_course'),
    path('<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),

]
