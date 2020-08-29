from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Course


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'


class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course_delete.html'
    success_url = reverse_lazy('course_list')


class CourseCreateView(CreateView):
    model = Course
    template_name = 'course_create.html'
    success_url = reverse_lazy('course_list')
    fields = ['title', 'description', 'slug']


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'course_update.html'
    success_url = reverse_lazy('course_list')
    fields = ['title', 'description']