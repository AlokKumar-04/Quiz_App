from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'correct_option')
    list_filter = ('correct_option',)
    search_fields = ('question_text',)

# Register your models here.
