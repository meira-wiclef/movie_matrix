from django.shortcuts import render
from pip._internal import index


# Create your views here.
from django.shortcuts import render


def home(request):
    context = {
        # Hero section background images
        "page_images": {
            'bg_image': 'core/images/bg-image.png',
            'bg_image_mobile': 'core/images/bg-image-mobile.png',
            'footer_1': 'core/images/footer-1.png'
        },

        # Top 3 of the Week (keeping your existing ones)
        "top_week_movies": [
            {
                'title': 'The Rip',
                'year': '2026',
                'duration': '1h53m',
                'rating_code': 'R',
                'score': '6.8(79k)',
                'image': 'core/images/top-week-1.png',
                'description': 'A group of Miami cops discovers a stash of millions in cash, leading to distrust as outsiders learn about the huge seizure.'
            },
            {
                'title': 'Avatar: Fire and Ash',
                'year': '2025',
                'duration': '3h17m',
                'rating_code': 'PG',
                'score': '7.4(122k)',
                'image': 'core/images/top-week-2.png',
                'description': "Jake and Neytiri encounter a new, aggressive Na'vi tribe, the Ash People, led by the fiery Varang."
            },
            {
                'title': 'Zootopia 2',
                'year': '2025',
                'duration': '1h48m',
                'rating_code': 'PG',
                'score': '7.5(69k)',
                'image': 'core/images/top-week-3.png',
                'description': 'Brave rabbit cop Judy Hopps and her friend, fox Nick Wilde, team up again to crack a perilous new case.'
            },

        ],

        # Comedies
        "comedies_movies": [
            {
                'title': 'The Perks of Being a Wallflower',
                'year': '2012',
                'duration': '1h42m',
                'rating_code': 'PG-13',
                'score': '7.9(510k)',
                'image': 'core/images/comedies-1.png',
                'description': 'An introverted freshman is taken under the wing of two seniors who welcome him to the real world.'
            },
            {
                'title': '10 Things I Hate About You',
                'year': '1999',
                'duration': '1h37m',
                'rating_code': 'PG-13',
                'score': '7.3(360k)',
                'image': 'core/images/comedies-2.png',
                'description': 'A new student must find a guy to date the meanest girl in school so her younger sister can go out.'
            },
            {
                'title': 'How to Lose a Guy in 10 Days',
                'year': '2003',
                'duration': '1h56m',
                'rating_code': 'PG-13',
                'score': '6.5(220k)',
                'image': 'core/images/comedies-3.png',
                'description': 'An advertising executive and a magazine writer bet on whether they can successfully cause a breakup in 10 days.'
            },
        ],

        # Action
        "action_movies": [
            {
                'title': 'Red Notice',
                'year': '2021',
                'duration': '1h58m',
                'rating_code': 'PG-13',
                'score': '6.3(310k)',
                'image': 'core/images/action-1.png',
                'description': 'An Interpol agent tracks the world’s most wanted art thief by reluctantly teaming up with a rival criminal.'
            },
            {
                'title': 'Spider-Man: No Way Home',
                'year': '2021',
                'duration': '2h28m',
                'rating_code': 'PG-13',
                'score': '8.2(870k)',
                'image': 'core/images/action-2.png',
                'description': 'With Spider-Man’s identity revealed, Peter asks Doctor Strange for help, unleashing multiverse villains.'
            },
            {
                'title': 'The Fast and the Furious',
                'year': '2001',
                'duration': '1h46m',
                'rating_code': 'PG-13',
                'score': '6.8(410k)',
                'image': 'core/images/action-3.png',
                'description': 'An undercover Los Angeles police officer infiltrates a street racing gang suspected of hijacking electronics trucks.'
            },
        ],

        # Classics
        "classics_movies": [
            {
                'title': 'Little Women',
                'year': '2019',
                'duration': '2h15m',
                'rating_code': 'PG',
                'score': '7.8(210k)',
                'image': 'core/images/classics-1.png',
                'description': 'Jo March reflects back and forth on her life, telling the beloved story of the March sisters.'
            },
            {
                'title': 'Titanic',
                'year': '1997',
                'duration': '3h14m',
                'rating_code': 'PG-13',
                'score': '7.9(1.2M)',
                'image': 'core/images/classics-2.png',
                'description': 'A seventeen-year-old aristocrat falls in love with a kind, poor artist aboard the luxurious, ill-fated R.M.S. Titanic.'
            },
            {
                'title': "Breakfast at Tiffany's",
                'year': '1961',
                'duration': '1h55m',
                'rating_code': 'Approved',
                'score': '7.6(140k)',
                'image': 'core/images/classics-3.png',
                'description': 'A young New York City socialite becomes interested in a young man who has moved into her apartment building.'
            },
        ]
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

