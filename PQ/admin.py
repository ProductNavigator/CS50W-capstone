from django.contrib import admin
from .models import User, Question, Type, Why, Who, When, Set, ProposedQuestion, Halloffame

# Register your models here.
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Type)
admin.site.register(Why)
admin.site.register(Who)
admin.site.register(When)
admin.site.register(Set)
admin.site.register(ProposedQuestion)
admin.site.register(Halloffame)