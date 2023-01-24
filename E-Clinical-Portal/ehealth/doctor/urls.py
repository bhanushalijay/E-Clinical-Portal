from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.index, name="Login"),
    path('signup',views.signup,name="signup"),
    path('back',views.back,name="back"),
    path('portal',views.portal,name="portal"),
    path('check',views.check,name="check"),
    path('register',views.register,name="register"),
    path('patientcheck',views.patientcheck,name="patientcheck"),
    path('savedata',views.savedata,name="savedata"),
    path('loginn',views.loginn,name="login"),
    path('home',views.home,name="home"),
]