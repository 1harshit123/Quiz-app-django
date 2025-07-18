from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.

class Quiz(models.Model):
    title = models.CharField(_("title of the quiz"), max_length=100)
    description = models.CharField(_("description of the quiz"), max_length=256) 
    created_by = models.ForeignKey(User, verbose_name=_("Created by"), on_delete=models.CASCADE)  
    no_of_question = models.IntegerField(_("How many questions this quiz have"))  
    time_duration = models.IntegerField(_("time duration in minutes"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, verbose_name=_("Quize title"), on_delete=models.CASCADE)
    image = models.ImageField(_("Image of the question"), upload_to="static/questions_image", height_field=None, width_field=None, max_length=None, blank=True) #have to return to fill the dimansions of the image
    text = models.TextField(_("The real text of the question"))
    question_no = models.PositiveIntegerField(_("Question number of question"))

    def __str__(self):
        return f"question no.{self.question_no} quiz {self.quiz}"

OPTION_CHOICES = (
    ('A', 'Option A'),
    ('B', 'Option B'),
    ('C', 'Option C'),
    ('D', 'Option D'),
)

class Answer(models.Model):
    option_label = models.CharField(_("option label"), max_length=1, choices=OPTION_CHOICES)
    question = models.ForeignKey(Question, verbose_name=_(""), on_delete=models.CASCADE)
    text = models.TextField(_("Option"))
    correctness = models.BooleanField(_("for correct of incorrect option"))

# quizzes/models.py
class QuizAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'quiz')  # One attempt per user/quiz

class UserAnswer(models.Model):
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


