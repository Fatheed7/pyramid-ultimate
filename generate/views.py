from django.shortcuts import render
from games.models import Game, Category, PrimaryChallenge, SecondaryChallenge

def generate(request):
    """ A view to return the index page """

    if request.method == 'POST':
        selected_games = request.POST.getlist('game')
        context = {
            'selected_games': selected_games,
        }
        return render(request, 'generate/test.html', context)

    games = Game.objects.all()
    categories = Category.objects.order_by('name')

    context = {
        'games': games,
        'categories': categories,
    }

    return render(request, 'generate/generate.html', context)

def gen_test(request):
    print(request.getlist('game'))