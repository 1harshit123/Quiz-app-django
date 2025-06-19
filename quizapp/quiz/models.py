from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
quiz app
question answer 
quiz
question -> image or text, options,  question no, set 
answer -> question(foreign_key), correctness
user -> first_name, last_name, email, password, username, 

class Quiz(models.Model):
    title = models.CharField(_("title of the quiz"), max_length=100)
    decription = models.CharField(_("description of the quiz"), max_length=256)
    created_at = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    no_of_question = models.CharField(_("How many question this quiz have"), max_length=50)
    time_duration = models.DurationField(_("time duration"))
