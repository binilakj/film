from django.urls import path
from . import views
app_name='filmapp'



urlpatterns = [
   path('',views.movie,name='movie'),
   path('cinema/<int:movies>/',views.detail,name='detail'),
   path('add/',views.add_cinema,name='add_cinema'),
   path('update/<int:id>/',views.update,name='update'),
   path('delete/<int:id>/', views.delete, name='delete')
]