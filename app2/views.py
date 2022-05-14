from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Director, Log
from .form import DirectorForm, MovieForm, LogForm

"""
from django import template
from django.template import context
from django.urls import reverse
"""


# Create your views here.


# Class-based-View

"""
IndexView クラス（ListView）
    ・queryset か model が必須（model だけを指定した場合は全てのレコードが抽出されてテンプレートに渡される）
    ・context_object_name : 指定した名前で参照
    ・template_name : 使用するテンプレート
"""
class IndexView(generic.ListView):
    template_name       = 'app2/index.html'   # ③ index.htmlに情報を渡す
    context_object_name = 'movie_list'        # ② 集めた情報の名前を'movie_list'にして
    queryset            = Movie.objects.all() # ① modelから情報を取り出して


"""
MovieDetailView クラス（DetailView）
    ・queryset か model が必須
    ・queryset を指定した場合はクエリセットからレコードを一意に絞り込む
"""
class MovieDetailView(generic.DetailView):
    model         = Movie              # 情報を持ってくるmodelを指定して
    template_name = 'app2/detail.html' # 情報(Movie)をdetail.htmlに渡す


"""
RegisterDirectorView クラス（CreateView）
"""
class RegisterDirectorView(generic.CreateView):
    model         = Director
    form_class    = DirectorForm
    template_name = 'app2/register.html'
    """・"reverse_lazy"はClassベースビュー版のredirectという解釈でOK.
       ・ここではURLに変数を渡す必要がないので、静的URLに遷移するときのみ使える"success_url"を使用する
    """
    success_url = reverse_lazy("app2:add_movie") 
    

"""
RegisterMovieView
"""
class RegisterMovieView(generic.CreateView):
    model         = Movie
    form_class    = MovieForm
    template_name = 'app2/register.html'
    """
    ・ここではリダイレクトするURLは映画ごとに異なる(動的な)ため、pkを渡す必要がある
    ・そのため"get_success_url"を用いてリダイレクトする
    """
    def get_success_url(self):
        return reverse_lazy("app2:movie_detail", kwargs={'pk': self.object.pk })
    

"""
WriteLogView
"""
class WriteLogView(generic.CreateView):
    model         = Log
    form_class    = LogForm
    template_name = 'app2/register.html'

    def get_success_url(self):
        # return reverse('app2:movie_detail', kwargs={'pk': self.object.movie.pk}) # qiitaで書かれていた形(reverse)
        return reverse_lazy("app2:movie_detail", kwargs={'pk': self.object.movie.pk })    # 他のサイトでよく使われてた形(reverse_lazy)


"""
WriteLog
"""
def WriteLog(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id) # この"movie_id"はテンプレートから送信されたデータ
    form  = LogForm(initial = {'movie': movie})

    if request.method == "POST":
        form = LogForm(request.POST)
        
        if form.is_valid():
            l = form.save(commit=False)
            l.save()
            return redirect('app2:movie_detail', pk=l.movie.pk)
    else:
        context = { 'form': form }
        return render(request, 'app2/register.html', context)


"""
UpdateLogView
"""
class UpdateLogView(generic.UpdateView):
    model         = Log
    form_class    = LogForm
    template_name = "app2/register.html"
    
    def get_success_url(self):
        return reverse_lazy('app2:movie_detail', kwargs={'pk': self.object.movie.pk }) # 更新が完了したら詳細ページに移動


"""
DeleteMovieView
"""
class DeleteMovieView(generic.DeleteView):
    model = Movie

    def get_success_url(self):
        return reverse_lazy('app2:index') # 削除が完了したら一覧ページに移動


"""
DeleteLogView
"""
class DeleteLogView(generic.DeleteView):
    model = Log

    def get_success_url(self):
        return reverse_lazy('app2:movie_detail', kwargs={'pk': self.object.movie.pk }) # 削除が完了したら詳細ページに移動





"""
# Function-View

# index
def index(request):
    movie_list = Movie.objects.all()
    return render(request, 'app2/index.html', {'movie_list':movie_list})


# moviedetail
def movieDetail(request, pk):
    m = Movie.objects.get(pk=pk) # Movieに入っているpkがリクエストと一致しているデータをgetしてmとする
    return render(request, 'app2/detail.html', {'movie':m})


# registerDirector
def registerDirector(request):
    if request.method == "POST":
        form = DirectorForm(request.POST)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('app2:add_movie')
    else:
        form = DirectorForm()
        return render(request, 'app2/register.html', {'form':form})


# registerMovie
def registerMovie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            return redirect('app2:movie_detail', pk=m.pk)
    else:
        form = MovieForm()
        return render(request, 'app2/register.html', {'form':form})


# writeLog
def writeLog(request):
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            l = form.save(commit=False)
            l.save()
            return redirect('app2:movie_detail', pk=l.movie.pk)
    else:
        form = LogForm()
        return render(request, 'app2/register.html', {'form':form})

    
# updateLog
def updateLog(request, pk):
    obj = get_object_or_404(Log, id=pk)
    if request.method == "POST":
        form = LogForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('app2:movie_detail', pk=obj.movie.pk)
    else:
        form = LogForm(instance=obj)
        return render(request, 'app2/register.html', {'form': form})


# deleteMovie
def deletemovie(request, pk):
    obj = get_object_or_404(Movie, id=pk)
    if request.mothod == "POST":
        obj.delete()
        return redirect('app2:index')
    context = {'obj':obj}
    return render(request, "app2/delete.html", context)


# deleteLog
def deleteLog(request, pk):
    obj = get_object_or_404(Log, id=pk)
    movie_id = obj.movie.pk
    if request.mothod == "POST":
        obj.delete()
        return redirect('app2:movie_detail', pk=movie_id)
    context = {'obj':obj}
    return render(request, "app2/delete.html", context)

"""