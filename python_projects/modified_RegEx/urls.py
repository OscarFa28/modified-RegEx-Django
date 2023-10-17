from django.urls import path

from modified_RegEx import views

app_name = 'modified_RegEx'

urlpatterns = [
    path('',views.index, name="index"),
    path('regEx_process/',views.regEx_process, name="regEx_process"),
]