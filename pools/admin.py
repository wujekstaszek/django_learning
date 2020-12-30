from django.contrib import admin


from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('Date information',{'fields':['pub_date']}	),
    ('Text',{'fields':['question_text']}),
    ]
    inlines = [ChoiceInline]
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
# Register your models here.
