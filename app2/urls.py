"""pj2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.urls import path
from . import views

app_name = 'app2'

# Class-based-Viewの場合
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # ex: /app2/
    path('movie/<int:pk>/',        views.MovieDetailView.as_view(),      name='movie_detail'), # /app2/movie/2/
    path('register/director/',     views.RegisterDirectorView.as_view(), name='add_director'), # /app2/register/director/
    path('register/movie/',        views.RegisterMovieView.as_view(),    name='add_movie'),    # /app2/register/movie/
    path('write/log/',             views.WriteLogView.as_view(),         name='add_log'),      # /app2/write/log/
    path('write/thismovie/<int:movie_id>/log/', views.WriteLog,          name='add_thelog'),   # /app2/write/thismovie/2/log/
    path('update/log/<int:pk>/',   views.UpdateLogView.as_view(),        name='update_log'),   # /app2/update/log/2/
    path('delete/log/<int:pk>/',   views.DeleteLogView.as_view(),        name='delete_log'),   # /app2/delete/log/2/
    path('delete/movie/<int:pk>/', views.DeleteMovieView.as_view(),      name='delete_movie'), # /app2/delete/movie/2/
]

"""
# Function-View
urlpatterns = [
    path('', views.index, name='index'), # ex: /app2/
    path('movie/<int:pk>/',    views.movieDetail,      name='movie_detail'), # /app2/movie/2/
    path('register/director/', views.registerDirector, name='add_director'), # /app2/register/director/
    path('register/movie/',    views.registerMovie,    name='add_movie'),    # /app2/register/movie/
    path('write/log/',         views.writeLog,         name='add_log'),      # /app2/write/log/
    path('update/log/<int:pk>/',   views.updateLog,    name='update_log'),   # /app2/update/log/2/
    path('delete/log/<int:pk>/',   views.deleteLog,    name='delete_log'),   # /app2/delete/log/2/
    path('delete/movie/<int:pk>/', views.deleteMovie,  name='delete_movie'), # /app2/delete/movie/2/
]
"""