from django.shortcuts import render
#create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    age = 65
    weight = 80
    subjects = ["Maths", "Science", "Engineering"]
    isDisabled = False
    name = "Maiyo Rono"

    data = {
        'age': age,
        'weight': weight,
        'subjects': subjects,
        'isDisabled'
        : isDisabled,
        'name': name
    }
    return render(request, 'products.html', data)
