from django.views.generic import View
import random
import string
from traning.models import Game, Ages
from django.http import JsonResponse
from django.shortcuts import render, redirect

class GameAlphabetView(View):
    template_name = 'traning/games/alphabet.html'

    def get(self, request, *args, **kwargs):
        letters = list(string.ascii_uppercase)
        correct_letter = random.choice(letters)
        random_letters = random.sample(letters, 3)
        options = random_letters + [correct_letter]
        random.shuffle(options)
        context = {'letters': options, 'correct_letter': correct_letter}
        return render(request, self.template_name, context)
    
    
    def post(self, request):
        selected_letter = request.POST.get('letter')
        letters = list(string.ascii_uppercase)  # Буквы кириллицы алфавита
        correct_letter = random.choice(letters)  # Случайная буква из letters
        correct = (selected_letter == correct_letter)
        return JsonResponse({'correct': correct})