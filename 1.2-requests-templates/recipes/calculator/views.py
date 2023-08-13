from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'curry': {
        'специи, г': 30,
        'перец, шт': 2,
        'лук, шт': 2,
        'курица, г': 400,
    },
}


def recipes(request, meal):
    number_of_people = int(request.GET.get('servings', 1))
    for key in DATA.keys():
        for key1 in DATA[key]:
            DATA[key][key1] = DATA[key][key1] * number_of_people
    if meal == 'buter':
        context = {
            'recipe': DATA['buter'],
        }
    elif meal == 'omlet':
        context = {
            'recipe': DATA['omlet'],
        }
    elif meal == 'pasta':
        context = {
            'recipe': DATA['pasta'],
        }
    elif meal == 'curry':
        context = {
            'recipe': DATA['curry'],
        }
    return render(request, 'calculator/index.html', context)

# нужно сделать обнуление при изменении цифры, но как это сделать?
