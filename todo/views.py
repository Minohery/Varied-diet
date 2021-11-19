from django.shortcuts import render

# Create your views here.

from .forms import forme, forme2
from .models import assignment
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from itertools import permutations
from random import shuffle


#The list of meals and number of tables is given in arguments 
def shuffle_and_check(L, num):
    v1=False
    v2=False
    v3=False
    new_L = []
    LL=list(L)
    while (v1 != True or v2 !=True or v3 != True) and (len(new_L) != num):
        LL=list(L)
        shuffle(LL)
        for i in range(len(LL)-1):
            #If the algorithm does not find 2 same consecutive meals
            if LL[i].task == LL[i+1].task:
                v1=False
                break
            v1=True
        for j in range(len(LL)-2):
            #If the algorithm does not find 2 same meals separated by 1 meal
            if LL[j].task == LL[j+2].task:
                v2=False
                break
            v2=True
        for k in range(len(LL)-3):
            #If the algorithm does not find 2 same meals separated by 2 meals
            if LL[k].task == LL[k+3].task:
                v2=False
                break
            v3=True
        if v1==True and v2==True and v3==True:
            if [LL] not in new_L:

                #Add LL to the list of lists
                new_L += [LL]
                v1=False
                v2=False
                v3=False


    return new_L



#If break_bool=1, bool(break_bool)=True.
#Elif break_bool=0, bool(break_bool)=False.
#That means that if the value is true, it consists of a breakfast
#Else, it is a lunch or a dinner.
def add(request, break_bool, number):
    #If it is a breakfast
    if break_bool==1:
        template_name="todo/liste_breakfast.html"

    #If it is a lunch or a dinner
    else:
        template_name="todo/liste.html"
    if request.method=="POST":
        form=forme(request.POST)
        if form.is_valid():

            #Create an assignment that has attributes equal to what the user input.
            a=assignment.objects.create(task=request.POST["dish"], date_and_time=timezone.now(), breakfast=bool(break_bool))
            a.save()
            if assignment.objects.filter(breakfast=bool(break_bool)).all().count() > number:
                a.delete()
                #return HttpResponseRedirect(reverse('todo:liste'))

        #If the user clicks the refresh button after he/she lands on "liste" page, no more information will be send to post
        return HttpResponseRedirect(reverse('todo:liste', args=(int(break_bool),)))
    else:
        form=forme()
    return render(response, template_name, {'form':forme(), 'liste':assignment.objects.filter(breakfast=bool(break_bool)).order_by('-date_and_time').reverse()})

def liste(response, break_bool):
    if break_bool==1:
        template_name="todo/liste_breakfast.html"
    else:
        template_name="todo/liste.html"
    return render(response, template_name, {'form':forme(), 'liste':assignment.objects.filter(breakfast=bool(break_bool)).order_by('-date_and_time').reverse(), "forme2":forme2()})

def delete(request, num, break_bool):
    assignment.objects.get(pk=num).delete()
    return HttpResponseRedirect(reverse('todo:liste', args=(int(break_bool),)))


def draw(request):
    #Permutations of the lunch and diner.
    template_name="todo/table.html"
    if request.method=="POST":
        num = request.POST["num"]
        p_real = []
        draft = []
        new_L = []
        p = shuffle_and_check(assignment.objects.filter(breakfast=False), int(num))
        for t in p:

            #Lunch
            for o in range(0,13,2):
                draft += [t[o]]
                
            #Dinner
            for bb in range(1,14,2):
                draft += [t[bb]]
            p_real += [draft]
            draft = []

        q = shuffle_and_check(assignment.objects.filter(breakfast=True), int(num))

        #Merge the two lists (Breakfast+Lunch/Dinner)
        for i, j in enumerate(q):
            new_L += [j+p_real[i]]
        return render(request, template_name, {"new_L":new_L,})
