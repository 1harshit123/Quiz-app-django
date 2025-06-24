from django.contrib import admin
from .models import Quiz, Question, Answer, QuizAttempt, UserAnswer

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'no_of_question', 'time_duration')
    search_fields = ('title',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_no', 'quiz', 'text')
    search_fields = ('text',)
    list_filter = ('quiz',)
    ordering = ('quiz', 'question_no')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('option_label', 'question', 'text', 'correctness')
    list_filter = ('correctness', 'option_label')
    search_fields = ('text',)

@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'completed_at')
    list_filter = ('quiz', 'completed_at')
    search_fields = ('user__username', 'quiz__title')
    ordering = ('-completed_at',)

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('attempt', 'question', 'selected_answer')
    search_fields = ('attempt__user__username', 'question__text')

# Alternatively, you can register models without decorators like this:
# admin.site.register(Quiz, QuizAdmin)
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Answer, AnswerAdmin)
# admin.site.register(QuizAttempt, QuizAttemptAdmin)
# admin.site.register(UserAnswer, UserAnswerAdmin)
