from django.shortcuts import render, redirect
import random, datetime

def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0

    if 'activities' not in request.session:
        request.session['activities'] = [] 
    context = {
        'total_gold': request.session['total_gold'],
        'activities': request.session['activities']
    }
    return render(request, 'ninja_app/index.html', context)

def process_money(request):
    if request.POST['building'] == 'farm':
        gold = random.randint(0, 21)
        request.session['total_gold'] += gold
        request.session['activities'].append('You earned ' + str(gold) + ' gold from the ' + (request.POST['building']) + '!' + '(' + str(datetime.datetime.now()) + ')<br>')
    
    if request.POST['building'] == 'cave':
        gold = random.randint(5, 11)
        request.session['total_gold'] += gold
        request.session['activities'].append('You earned ' + str(gold) + ' gold from the ' + request.POST['building'] +  '!' + '(' + str(datetime.datetime.now()) + ')<br>')

    if request.POST['building'] == 'house':
        gold = random.randint(2,6)
        request.session['total_gold'] += gold
        request.session['activities'].append('You earned ' + str(gold) + ' gold from the ' + request.POST['building'] + '!' + '(' + str(datetime.datetime.now()) + ')<br>')

    if request.POST['building'] == 'casino':
        gold = random.randint(-50, 51)
        if gold >= 0:
            request.session['activities'].append('Entered a casino and earned ' + str(gold) +' gold' + ' ' + '(' + str(datetime.datetime.now()) + ')<br>')
        else:
            request.session['activities'].append('Entered a casino and lost ' + str(gold) + ' gold' + ' ' + '(' + str(datetime.datetime.now()) + ')<br>')
        request.session['total_gold'] += gold
            
    return redirect('/')

def reset(request):
    request.session['total_gold'] = 0
    request.session['activities'] = []
    return redirect('/')