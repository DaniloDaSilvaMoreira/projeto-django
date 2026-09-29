from django.shortcuts import render, get_object_or_404 

from django.db.models import Q, Value, F 
from django.db.models.functions import Concat
from utils.recipes.factory import make_recipe
from .models import Recipe
from django.db.models.aggregates import Count
from django.http import Http404
# Create your views here.

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')

    if not recipes:
        raise Http404('Not found')


    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title':f'{recipes.first().category.name} - Category |'
        })


def recipe(request, id):
    # Busca a receita real no banco ou retorna erro 404 se não existir
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe, # Mudado de make_recipe() para a receita do banco
        'is_detail_page': True,
    })

def theory(request, *args, **kwargs):
    recipes = Recipe.objects.get_published()
    number_of_recipes = recipes.aggregate(number=Count('id'))

    context = {
        'recipes': recipes,
        'number_of_recipes': number_of_recipes['number']
    }

    return render(request, 'recipes/pages/theory.html', context=context)
