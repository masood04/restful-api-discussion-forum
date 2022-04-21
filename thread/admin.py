from django.contrib import admin
from .models import Answer, Question, Tag, Vote

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(Vote)