from django import forms
from .models import ManageQuestion

class QuestionForm(forms.ModelForm):
  class Meta:
      model = ManageQuestion
      fields = ['question', 'option_a', 'option_b', 'option_c', 'option_d', 'subject', 'correct_answer',]
