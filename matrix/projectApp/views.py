from django.shortcuts import render
from django.http import HttpResponse
import random


def models_list(request):
    random_n = random.randint(1, 100)
    if random_n < 69:
        random_n +=666
    else: random_n -=1


    return HttpResponse(f"Testing of views {random_n}")
