from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="Login"),
    path('signup',views.signup,name="signup"),
    path('portal',views.portal,name="portal"),
    path('register',views.register,name="register"),
    path('check',views.check,name="check"),
    path('back',views.back,name="back"),
    path('savedata',views.savedata,name="savedata"),
    path('loginn',views.loginn,name="login"),
    path('home',views.home,name="home"),
    path('bookappointment',views.bookappointment,name="bookappointment"),
    path('bookin',views.bookin,name="bookin")

]