from django.contrib import admin

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Date information", {"fields": ["pub_date"]}),
        (None, {"fields": ["question_text"]}),
    ]

admin.site.register(Question, QuestionAdmin)