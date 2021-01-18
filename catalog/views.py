from django.shortcuts import render
from django.views import generic
from catalog.models import Food


def index(request):

    num_foods = Food.objects.all().count()

    context = {
        'num_foods': num_foods,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class FoodListView(generic.ListView):
    paginate_by = 100
    model = Food

class FoodDetailView(generic.DetailView):
    model = Food

def about(request):
    num_foods = Food.objects.all().count()

    context = {
        'num_foods': num_foods,
    }
    
    return render(request, 'about.html', context=context)
