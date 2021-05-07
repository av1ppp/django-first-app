from django.http import HttpResponse


def index(request):
  return HttpResponse("<h2>Главная</h2>")

def about(request):
  return HttpResponse("<h2>О Сайте</h2>")

def contact(request):
  return HttpResponse("<h2>Контакты</h2>")

def products(request, productId = 0):
  output = f"<h2>Product № {str(productId)}</h2>"
  return HttpResponse(output)

def users(request, id, name):
  output = f"<h2>user</h2><h3>id: {str(id)} name: {name}</h3>"
  return HttpResponse(output)

def books(request, name):
  return HttpResponse(f"<h2>Книга</h2><h3> {name}</h3>")
