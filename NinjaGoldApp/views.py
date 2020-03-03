from django.shortcuts import render, redirect
import random as rand


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activity_log'] = []

    return render(request, 'index.html')


def process_money(request):

    print("**-->  POST request: ", request.POST)

    if 'Farm' in request.POST:
        amount = rand.randrange(10, 21)
        request.session['activity_log'].append(
            'You earned '+str(amount)+' gold from the farm!')

    if 'Cave' in request.POST:
        amount = rand.randrange(5, 11)
        request.session['activity_log'].append(
            'You earned '+str(amount)+' gold from the cave!')

    if 'House' in request.POST:
        amount = rand.randrange(2, 6)
        request.session['activity_log'].append(
            'You earned '+str(amount)+' gold from the house!')

    if 'Casino' in request.POST:
        amount = rand.randrange(-50, 50)
        if amount >= 0:
            request.session['activity_log'].append(
                'You won '+str(amount) + ' gold from the casino!')
        if amount < 0:
            request.session['activity_log'].append(
                'Sucker!!! You lost'+str(amount)+'gold in the casino!')

    print(amount)
    print('total gold: ', request.session['gold'])
    request.session['gold'] += amount

    print("**--> ", request.session['activity_log'])

    return redirect('/')


def reset(request):
    request.session.clear()
    return redirect('/')
