from datetime import date

from django.forms  import *
from django.utils.translation import gettext_lazy as _

from .models import *

class SelectTeacherAndDateForm(Form):
    teacher = ModelChoiceField(label=_('Teacher'), queryset=Teacher.objects.all())
    date = DateField(label=_('Date'), initial=date.today)

SubstitutionFormSet = modelformset_factory(
    Substitution, fields=('period', 'substitute', 'room'), extra=8)