from django.contrib import admin
from .models import Planet
from .models import Jedi
from .models import Question
from .models import Candidate

admin.site.register(Planet)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name_c', 'planet', 'age', 'email',
                    'tested', 'status_padavan')


@admin.register(Jedi)
class JediAdmin(admin.ModelAdmin):
    list_display = ('name_j', 'planet')


admin.site.register(Question)
