from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cinema
from . forms import Cinemaform
# Create your views here.
def movie(request):
    cinema=Cinema.objects.all()
    context={
        'movies':cinema
    }
    return render(request,"index.html",context)


def detail(request, movies):
    a = Cinema.objects.get(id=movies)
    return render(request, "detail.html", {'cinema': a})


def add_cinema(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        des = request.POST.get('des', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        b = Cinema(name=name, des=des, year=year, img=img)
        b.save()
    return render(request, 'add.html')


def update(request, id):
    cinema = Cinema.objects.get(id=id)
    form = Cinemaform(request.POST or None, request.FILES, instance=cinema)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'cinema': cinema})


def delete(request, id):
    if request.method == "POST":
        cinema = Cinema.objects.get(id=id)
        cinema.delete()
        return redirect('/')
    return render(request, 'delete.html')
