from django.forms import ModelForm
from .models import Candidate, Planet#, Question

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = ['name_c', 'planet', 'email', 'age']

        # Выпадающее меню со списком планет из модели Planet
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['planet'].queryset = Planet.objects.all()


# class QuestionsForm(ModelForm):
#     class Meta:
#         model = Question
#         fields = ['title', 'question', 'answer']

#         # Выпадающее меню со списком планет из модели Planet
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields['answer'].queryset = Question.objects.all()



# class CandidateForm(forms.Form):
#     name = forms.CharField(label='Твое имя', max_length=25)
#     planet = forms.ModelChoiceField(queryset=Planet.objects.all())
#     age = forms.IntegerField(widget=forms.TextInput())
#     email = forms.EmailField(max_length=25)