from django .urls import path

app_name='shoping'

from .views import Fashion_list


urlpatterns=[

path('',Fashion_list.as_view(),name='Fashion_list')

]