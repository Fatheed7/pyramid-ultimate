from django.shortcuts import render
from games.models import Game, Category, PrimaryChallenge, SecondaryChallenge
from django.contrib.auth.decorators import login_required

@login_required
def generate(request):
    """ A view to return the index page """

    games = Game.objects.order_by('name')
    categories = Category.objects.order_by('name')
    primary = PrimaryChallenge.objects.order_by('name')
    secondary = SecondaryChallenge.objects.order_by('name')

    if 'genForm' in request.POST:
        if request.method == 'POST':
            selected_games = request.POST.getlist('game')
            request.session['selected_games'] = selected_games

            context = {
                'selected_games': selected_games,
                'games': games,
            }
            return render(request, 'generate/confirm.html', context)
    elif 'confirmForm' in request.POST:
        if request.method == 'POST':
            return generate_challenges(request, games, primary, secondary)
    context = {
        'games': games,
        'categories': categories,
    }

    return render(request, 'generate/generate.html', context)

@login_required
def create_run(request):
    primary = PrimaryChallenge.objects.order_by('name')
    secondary = SecondaryChallenge.objects.order_by('name')
    context = {
        'primary': primary,
        'secondary': secondary,
    }

    return render(request, 'generate/create.html', context)

@login_required
def generate_challenges(request, games, primary, secondary):
    selected_games = request.session.get('selected_games')
    game_list = games.filter(name__in=selected_games)
    challenge_list = []
    for game in game_list:
        print("Game: " + game.name + " - ID: " + str(game.id))
        confirm_primary = primary.filter(game=game.id)
        confirm_secondary = secondary.filter(game=game.id)
        random_primary = confirm_primary.order_by('?')[:1]
        random_secondary = confirm_secondary.order_by('?')[:1]
        challenge_object = {
            'game': game.name,
            'primary': random_primary[0].name,
            'secondary': random_secondary[0].name,
        }
        challenge_list.append(challenge_object)
    context = {
        'challenge_list': challenge_list,
        'primary': primary,
        'secondary': secondary,
    }
    return render(request, 'generate/create.html', context)
