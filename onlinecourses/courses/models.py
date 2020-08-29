import uuid
from django.db import models
from django.core.validators import validate_image_file_extension
from django.contrib.auth.models import User
from core.utils import generate_uuid_token


def upload_image_dir(instance, filename):
    return f'media/uploads/courses/{filename.lower()}'


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField(default="No description yet")
    slug = models.SlugField()
    image = models.ImageField(upload_to=upload_image_dir, blank=True, validators=[validate_image_file_extension])


    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class CourseEnrollment(models.Model):
    """
    Model to track course enrollments.
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class CourseModule(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=128)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=128)
    module = models.ManyToManyField(CourseModule, related_name='sections')

    def __str__(self):
        return self.name

class Unit(models.Model):
    """
    Course section unit to make it reusable
    """
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    content = models.TextField()
