from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.forms import ModelForm
from .models import User, Question, Type, Why, Who, When, Set, ProposedQuestion, Halloffame
from django.core.exceptions import NON_FIELD_ERRORS
from datetime import datetime
from django.contrib.auth.decorators import login_required
import random

def index(request):
    return render(request, "PQ/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "PQ/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "PQ/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "PQ/register.html", {
                "message": "Passwords must match."
            })

        #Make sure the email is empty
        try:
            User.objects.get(email=email)
            return render(request, "PQ/register.html", {
                "message": "This email is already taken."
            })
        except User.DoesNotExist:                           
            # Attempt to create new user
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
            except IntegrityError:
                return render(request, "PQ/register.html", {
                "message": "Username already taken."
                })
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "PQ/register.html")

def generate(request):
    if request.method == "POST":
        #garther information about the input
        form = Generate(request.POST)

        #if user authenticated create this question as him
        if request.user.is_authenticated:
            user_id = request.user.id
            user = User.objects.get(pk=user_id)

            if form.is_valid():
                    type1 = form.cleaned_data["type"]
                    why = form.cleaned_data["why"]
                    who = form.cleaned_data["who"]
                    when = form.cleaned_data["when"]
                    dateadded = datetime.now()

                    ########### select questions from database:
                    setofquestions_pre = Question.objects.filter(type=type1, why=why, who=who, when=when)

                    ##get random items from selected _pre set
                    numberofselectedquestionsall = len(setofquestions_pre)
                    if numberofselectedquestionsall < 5:
                        setofquestions = random.sample(list(setofquestions_pre), k=numberofselectedquestionsall)
                    else:
                        setofquestions = random.sample(list(setofquestions_pre), k=5)

                    #create new Set:
                    s = Set.objects.create(dategenerated = dateadded, user = user, type = type1, why = why, who = who, when = when)
                    s.save()

                    #find current set
                    current_set = Set.objects.get(dategenerated = dateadded, user = user)
                    set_id = current_set.id
                    print(set_id)

                    #add questions to the existing set
                    for q in setofquestions:
                        print(q)
                        current_set.questions.add(q)

                    #show created set:
                    return HttpResponseRedirect(reverse("set", args=(set_id,)))
            else:
                return render(request, "PQ/set.html", {
                "error": "Ops. Something went wrong!" 
                })
        else:
            #if user is not authenticated create this question as admin
                user_id = 1
                user = User.objects.get(pk=user_id)

                if form.is_valid():
                        type1 = form.cleaned_data["type"]
                        why = form.cleaned_data["why"]
                        who = form.cleaned_data["who"]
                        when = form.cleaned_data["when"]
                        dateadded = datetime.now()

                        ########### select questions from database:
                        setofquestions_pre = Question.objects.filter(type=type1, why=why, who=who, when=when)[:5]
                        
                        numberofselectedquestionsall = len(setofquestions_pre)
                        if numberofselectedquestionsall < 5:
                            setofquestions = random.sample(list(setofquestions_pre), k=numberofselectedquestionsall)
                        else:
                            setofquestions = random.sample(list(setofquestions_pre), k=5)
                        

                        #create new Set:
                        s = Set.objects.create(dategenerated = dateadded, user = user, type = type1, why = why, who = who, when = when)
                        s.save()

                        #find current set
                        current_set = Set.objects.get(dategenerated = dateadded, user = user)
                        set_id = current_set.id
                        print(set_id)

                        #add questions to the existing set
                        for q in setofquestions:
                            current_set.questions.add(q)

                        #show created set:
                        return HttpResponseRedirect(reverse("set", args=(set_id,)))
                else:
                    return render(request, "PQ/set.html", {
                    "error": "Ops. Something went wrong!" 
                    })
    else:
        return render(request, "PQ/generate.html", {
            "form": Generate(),
    })

def set(request,set_id):
###IF POST
    if request.method == "POST":
    #If Modal send POST to register user:
        if "registermodalname" in request.POST:
            username = request.POST["username"]
            email = request.POST["email"]

            # Ensure password matches confirmation
            password = request.POST["password"]
            confirmation = request.POST["confirmation"]
            if password != confirmation:
                return render(request, "PQ/register.html", {
                    "message": "Passwords must match."
                })

            #Make sure the email is empty
            try:
                User.objects.get(email=email)
                return render(request, "PQ/register.html", {
                    "message": "This email is already taken."
                })
            except User.DoesNotExist:                           
                # Attempt to create new user
                try:
                    user = User.objects.create_user(username, email, password)
                    user.save()
                except IntegrityError:
                    return render(request, "PQ/register.html", {
                    "message": "Username already taken."
                    })
                #add this set to registering user
                set = Set.objects.get(pk = set_id)
                set.user = user
                set.firsttime = False
                set.save(update_fields=['user','firsttime'])
                login(request, user)
                return HttpResponseRedirect(reverse("set", args=(set_id,)))
        #if Modal send POST to login user:
        elif "loginmodalname" in request.POST:
                # Attempt to sign user in
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)

            # Check if authentication successful
            if user is not None:
                #add this set to loggingin user
                set = Set.objects.get(pk = set_id)
                set.user = user
                set.save(update_fields=['user'])
                login(request, user)
                return HttpResponseRedirect(reverse("set", args=(set_id,)))
            else:
                ###How to add here message?
                return HttpResponseRedirect(reverse("set", args=(set_id,)))
        #if Modal send POST to add proposed Question
        else:
            set = Set.objects.get(pk = set_id)
            ptext = request.POST["question"]
            ptype = set.type
            pwhy = set.why
            pwho = set.who
            pwhen = set.when
            pdateadded = datetime.now()
            s = ProposedQuestion.objects.create(pdateadded = pdateadded, user = request.user, ptext = ptext, ptype = ptype, pwhy = pwhy, pwho = pwho, pwhen = pwhen, pset = set)
            s.save()

            set.firsttime = False
            set.save(update_fields=['firsttime'])

            return HttpResponseRedirect(reverse("set", args=(set_id,)))

    ####IF GET
    else:
        #check if the set is existing
        try:
            set = Set.objects.get(pk = set_id)
        except Set.DoesNotExist:
        #if not show error
            return render(request, "PQ/error.html", {
            "error": "Error - you don't have privilidges to see this set or it does not exists" 
            })
        #get the correct set
        set = Set.objects.get(pk = set_id)

        #If this is first timesomeone see this set:
        if set.firsttime == True:
            #check if the set.user is the same as active user or admin:
            user = set.user
            if user.id == request.user.id or 1:
            #if yes create iterable lists of questuions
                questions = set.questions.all()
            # and render it to the screen
                return render(request, "PQ/set.html", {
                "set": set,
                "questions": questions,
                "firsttime": "firstime",
                })
            #if not show error
            else:
                return render(request, "PQ/set.html", {
                "error": "Error - you don't have privilidges to see this setor it does not exists" 
                })
        else:
            #check if the set.user is the same as active user or admin:
            user = set.user
            if user.id == request.user.id:
            #if yes create iterable lists of questuions
                questions = set.questions.all()
            # and render it to the screen
                return render(request, "PQ/set.html", {
                "set": set,
                "questions": questions,
                })
            #if not show error
            else:
                return render(request, "PQ/set.html", {
                "error": "Error - you don't have privilidges to see this setor it does not exists" 
                })

@login_required(login_url='index')
def user(request):
    user = request.user
    sets = Set.objects.filter(user=user)
    return render(request, "PQ/user.html", {
            "sets": sets, 
            "user": user,
     })


def halloffame(request):
    hallsets = Halloffame.objects.all()
    return render(request, "PQ/halloffame.html", {
            "hallsets": hallsets, 
     })


class Generate(ModelForm):
    class Meta:
        model = Set
        fields = ['type', 'why', 'who', 'when']
        widgets = {
            'type': forms.RadioSelect(),
            'why': forms.RadioSelect(),
            'who': forms.RadioSelect(),
            'when': forms.RadioSelect(),
        }
    template_name = "PQ/generate_snippet.html"
    error_messages = {
            NON_FIELD_ERRORS: {
                'must provide': "Please select at least one %(field_labels)s ",
            }
        }
