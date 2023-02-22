from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Quiz)
admin.site.register(quiz_allocation)
# admin.site.register(Question)
admin.site.register(Answer)

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    exclude = ['created_by',]

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()

admin.site.register(Question, QuestionAdmin)
