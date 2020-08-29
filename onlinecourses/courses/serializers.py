from rest_framework import serializers
from .models import  Course

class CourseSerializer (serializers.ModelSerializer):

    #lessons = LessonSerializer(many=True, required=False)
    class Meta:
        model = Course
        fields = ( 'title', 'description', 'slug') 