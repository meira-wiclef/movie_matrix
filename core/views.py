from django.shortcuts import render
from pip._internal import index


# Create your views here.
def home(request):
    context = {
        "page_images" : {
            'bg_image': 'core/images/bg-image.png',
            'bg_image_mobile': 'core/images/bg-image-mobile.png',
            'top_week_1': 'core/images/top-week-1.png',
            'top_week_2': 'core/images/top-week-2.png',
            'top_week_3': 'core/images/top-week-3.png',
            'comedies_1': 'core/images/comedies-1.png',
            'comedies_2': 'core/images/comedies-2.png',
            'comedies_3': 'core/images/comedies-3.png',
            'comedies_4': 'core/images/comedies-4.png',
            'comedies_5': 'core/images/comedies-5.png',
            'comedies_6': 'core/images/comedies-6.png',
            'action_1': 'core/images/action-1.png',
            'action_2': 'core/images/action-2.png',
            'action_3': 'core/images/action-3.png',
            'action_4': 'core/images/action-4.png',
            'action_5': 'core/images/action-5.png',
            'action_6': 'core/images/action-6.png',
            'classics_1': 'core/images/classics-1.png',
            'classics_2': 'core/images/classics-2.png',
            'classics_3': 'core/images/classics-3.png',
            'classics_4': 'core/images/classics-4.png',
            'classics_5': 'core/images/classics-5.png',
            'classics_6': 'core/images/classics-6.png',
            'footer_1': 'core/images/footer-1.png',
        }
    }
    return render(request, 'core/index.html', context)

def movie(request):
    context = {
        'page_images' : {
            'bg_movie_2': 'core/images/bg-movie-2.jpg',
            'movie_1': 'core/images/movie-1.jpg',
            'movie_2': 'core/images/movie-2.webp',
            'logan': 'core/images/logan.jpg',
            'kate': 'core/images/kate.jpg',
            'nina': 'core/images/nina.jpg',
            'paul': 'core/images/paul.JPG',
            'ezra': 'core/images/ezra.jpg',
            'emma': 'core/images/emma.jpg',
            'comedies_2': 'core/images/comedies-2.png',
            'comedies_3': 'core/images/comedies-3.png',
            'footer_1': 'core/images/footer-1.png',
        }
    }
    return render(request, 'core/movie.html', context)

def about(request):
    context = {
        'page_images' : {
            'footer_1': 'core/images/footer-1.png',
        }
    }
    return render(request, 'core/aboutus.html', context)

def contact(request):
    context = {
        'page_images': {
            'footer_1': 'core/images/footer-1.png',
        }
    }
    return render(request, 'core/contactus.html', context)

