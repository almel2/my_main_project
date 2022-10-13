from django.shortcuts import render


def index(request):
    return render(request, 'warehouse_api/index.html', {})
