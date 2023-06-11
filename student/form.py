from django import forms
from .models import Enquery


class Enquery_form(forms.ModelForm):
    class Meta:
        model = Enquery
        fields = ['student_enquiry_id',
                    'Enuery_descriptin', 'Query_related_to',
                    'college_reply']


