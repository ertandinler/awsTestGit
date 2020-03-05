from django.shortcuts import render, HttpResponse

def home_view(request):
    if request.user.is_authenticated:       #bideoda  request.user.is_authenticated() methot gibi kullanılmış. böye hata verdi. is not callable
        context = {
            'isim': 'Barış',
        }
    else:
        context = {
            'isim': 'Misafir',
        }
    return render(request, 'home.html', context)
