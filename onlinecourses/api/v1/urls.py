from django.urls import path, re_path
from . views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'profiles', ProfileAPIView)
urlpatterns = router.urls

urlpatterns += [
    # re_path('profile/(?P<pk>\d+)?', ProfileAPIView.as_view(), name="profile"),
    path('login', LoginAPIView.as_view(), name="login"),
    path('logout', LogoutAPIView.as_view(), name="logout"),
    path('courses', CoursesListView.as_view(), name="courseslist"),


]