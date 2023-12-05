from django.urls import include,path
from hub.views import *

urlpatterns = [
    
    path("signup/", signup_view.as_view(), name="Signup"),
    path("login/", login_view.as_view(), name="Login"),
    # path("logout/", logout_View.as_view(), name="Logout"),
    path("event/", event_view.as_view(), name="Event"),
    path("club/", club_view.as_view(), name="Club"),
    path("feedback/", feed_view.as_view(), name="Feedback"),
    path("user/", user_view.as_view(), name="User"),
    path("userclub/", club_user_view.as_view(), name="Club View")
]