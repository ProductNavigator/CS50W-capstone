from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


##fs = FileSystemStorage(location='/media/photos')

User._meta.get_field('email')._unique = True

class User(AbstractUser):
    pass

class Type(models.Model):
    type = models.CharField(max_length=100)

    class Meta:
        ordering = ['type']

    def __str__(self):
        return self.type

class Why(models.Model):
    why = models.CharField(max_length=100)

    class Meta:
        ordering = ['why']

    def __str__(self):
        return self.why

class Who(models.Model):
    who = models.CharField(max_length=100)

    class Meta:
        ordering = ['who']

    def __str__(self):
        return self.who

class When(models.Model):
    when = models.CharField(max_length=100)

    class Meta:
        ordering = ['when']

    def __str__(self):
        return self.when
    
class Question(models.Model):
    text = models.CharField(max_length=10000)
    type = models.ManyToManyField(Type, blank=True, related_name="typeq")
    why = models.ManyToManyField(Why, blank=True, related_name="whyq")
    who = models.ManyToManyField(Who, blank=True, related_name="whoq")
    when = models.ManyToManyField(When, blank=True, related_name="whenq")
    dateadded = models.DateTimeField()
    
    class Meta:
        ordering = ['text']

    def __str__(self):
        return self.text


class Set(models.Model):
    questions = models.ManyToManyField(Question, related_name="questions_set")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_sets")
    dategenerated = models.DateTimeField(default=now)
    type = models.ForeignKey(Type, on_delete=models.CASCADE ,verbose_name="types of questions", blank=False, related_name="typeset")
    why = models.ForeignKey(Why, on_delete=models.CASCADE ,verbose_name="why you want to ask them", blank=False, related_name="whyset")
    who = models.ForeignKey(Who, on_delete=models.CASCADE ,verbose_name="who you want to ask", blank=False, related_name="whoset")
    when = models.ForeignKey(When, on_delete=models.CASCADE ,verbose_name="when you want to use them", blank=False, related_name="wheset")
    firsttime = models.BooleanField(default=True)


class ProposedQuestion(models.Model):
    ptext = models.CharField(max_length=10000)
    ptype = models.ForeignKey(Type, on_delete=models.CASCADE, blank=False, related_name="proposedtypeq")
    pwhy = models.ForeignKey(Why, on_delete=models.CASCADE, blank=False, related_name="proposedwhyq")
    pwho = models.ForeignKey(Who, on_delete=models.CASCADE, blank=False, related_name="proposedwhoq")
    pwhen = models.ForeignKey(When, on_delete=models.CASCADE, blank=False, related_name="proposedwhenq")
    pset = models.ForeignKey(Set, on_delete=models.CASCADE, blank=False, related_name="proposedsetq")
    pdateadded = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_question")


class Halloffame(models.Model):
    name = models.CharField(max_length=1000)
    twitter = models.URLField(max_length=1000, null=True, blank=True)
    linkedin = models.URLField(max_length=1000, null=True, blank=True)
    facebook = models.URLField(max_length=1000, null=True, blank=True)
    website = models.URLField(max_length=1000, null=True, blank=True)
    photo = models.URLField(max_length=1000, null=True, blank=True)
    question1 = models.CharField(max_length=10000)
    question2 = models.CharField(max_length=10000)
    question3 = models.CharField(max_length=10000)
    bio = models.CharField(max_length=10000)