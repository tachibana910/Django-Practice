from django.forms import ModelForm
from .models import Movie, Director, Log


class DirectorForm(ModelForm):
    class Meta:
        model  = Director
        fields = ('name',)

class MovieForm(ModelForm):
    class Meta:
        model  = Movie
        fields = ('title', 'watch_date', 'director')

class LogForm(ModelForm):
    class Meta:
        model  = Log
        fields = ('text', 'movie')