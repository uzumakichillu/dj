from django.conf.urls import url,include
from basicapp import views

app_name = 'basicapp'

urlpatterns=[
    url(r'^register/',views.register,name='register'),
    url(r'^userlogin/',views.userlogin,name='login')
]
