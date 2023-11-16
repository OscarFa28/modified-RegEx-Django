from django.urls import path

from modified_RegEx import views

app_name = 'modified_RegEx'

urlpatterns = [
    path('',views.index, name="index"),
    path('regEx_process/',views.regEx_process, name="regEx_process"),
    path('file_compressor/',views.file_compressor, name="file_compressor"),
]