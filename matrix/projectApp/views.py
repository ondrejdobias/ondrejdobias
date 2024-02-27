from django.shortcuts import render
from django.http import HttpResponse
import random


def models_list(request):
    random_n = random.randint(0, 1000)
    if random_n < 30:
        random_n +=1000

    return HttpResponse(f"Random číslo generátor: {random_n}")

def post_list(request):
    random_n = random.randint(0, 1000)
    if random_n < 69:
        random_n += 666

    return render(request, 'ProjectApp/post_list.html', {"vara":random_n})
