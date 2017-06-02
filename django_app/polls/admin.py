from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    # fields = ('pub_date', 'question_text',)
    list_display = (
        'question_text',
        'pub_date',
        'was_published_recently',
    )
    fieldsets = [
        (None, {
            'fields': [
                'question_text'
            ]
        }),
        ('Date Information', {
            'fields': [
                'pub_date',
            ]
        })
    ]
    list_filter = ['pub_date']
    inlines = (ChoiceInline,)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
