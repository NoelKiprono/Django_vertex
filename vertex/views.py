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
        'isDisabled' : isDisabled,
        'name': name
    }
    return render(request, 'products.html', data)


def students(request):
   
    scores = [
        {
		"names": "Ayanna Moon",
		"email": "eu.sem@icloud.com",
		"score": 63,
		"age": 22
	},
	{
		"names": "Coby Lynch",
		"email": "sollicitudin@aol.com",
		"score": 25,
		"age": 21
	},
	{
		"names": "Shana Adams",
		"email": "sagittis.lobortis@aol.edu",
		"score": 82,
		"age": 23
	},
	{
		"names": "Richard Gordon",
		"email": "mauris.rhoncus@aol.com",
		"score": 55,
		"age": 19
	},
	{
		"names": "Larissa Richmond",
		"email": "metus.eu@yahoo.net",
		"score": 27,
		"age": 20
	},
	{
		"names": "Raymond Dennis",
		"email": "sem.vitae@hotmail.ca",
		"score": 65,
		"age": 22
	},
	{
		"names": "Micah Mercer",
		"email": "nulla.facilisis.suspendisse@hotmail.edu",
		"score": 92,
		"age": 18
	},
	{
		"names": "Morgan Tyson",
		"email": "ullamcorper.duis@google.edu",
		"score": 90,
		"age": 18
	},
	{
		"names": "Indira Fox",
		"email": "molestie.dapibus@yahoo.couk",
		"score": 61,
		"age": 19
	},
	{
		"names": "Aretha Greer",
		"email": "sem@protonmail.edu",
		"score": 69,
		"age": 23
	},
	{
		"names": "Chaney Wolf",
		"email": "tortor.nunc@outlook.com",
		"score": 98,
		"age": 23
	},
	{
		"names": "John Potter",
		"email": "lobortis.nisi@google.ca",
		"score": 48,
		"age": 23
	},
	{
		"names": "Walter Stevenson",
		"email": "justo.praesent@google.edu",
		"score": 57,
		"age": 23
	},
	{
		"names": "Leonard Richard",
		"email": "dignissim.tempor@google.org",
		"score": 92,
		"age": 21
	},
	{
		"names": "Yoshio Holland",
		"email": "dui.cras@icloud.ca",
		"score": 29,
		"age": 22
	}
]
    data = {"students": scores}
    return render(request, 'students.html', data)   
    