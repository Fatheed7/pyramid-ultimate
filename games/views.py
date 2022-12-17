from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Game, Category
from django.db.models import F, Q
from django.db.models.functions import Lower

# Create your views here.

def all_games(request):

    games = Game.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                games = games.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'rating':
                sortkey = 'rating__rating'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    games = games.order_by(
                        F(sortkey).desc(nulls_last=True))
                else:
                    games = games.order_by(sortkey)
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            games = games.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('games'))

            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query) |
                       Q(ingredients__name__icontains=query))
            games = games.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'games': games,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'games/games.html', context)

def game_detail(request, game_id):
    """ A view to show individual product details """

    game = get_object_or_404(Game, pk=game_id)

    context = {
            'game': game,
        }

    return render(request, 'games/game_detail.html', context)