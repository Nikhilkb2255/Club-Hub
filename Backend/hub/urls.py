from django.urls import include,path
from hub.views import *

urlpatterns = [
    
    path("signup/", SIGNUP.as_view(), name="Signup"),
    path("login/", LOGIN.as_view(), name="Login"),
    path("event/", EVENT.as_view(), name="Event"),
    path("club/", CLUB.as_view(), name="Club"),
    path("feedback/", FEEDBACK.as_view(), name="Feedback"),
    path("join/", JOIN_CLUB.as_view(), name="User"),
    path("userclub/", CLUB_USER.as_view(), name="Club View")
]