from django.contrib import admin
from .models import Choice, Question

admin.site.register(Choice)

#question과 choice를 함께 편집할 수 있도록
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 # 추가옵션을 몇 개 기본으로 띄워놓을 것인지


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('질문 섹션', {'fields': ['question_text']}),
        ('생성일', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    readonly_fields = ['pub_date']
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text', 'choice__choice_text']

admin.site.register(Question, QuestionAdmin)