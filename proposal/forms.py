from django import forms

from .models import Proposal


class ProposalForm(forms.ModelForm):
    """
    Form for model Proposal
    """
    def __init__(self, *args, **kwargs):
        super(ProposalForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['name'].widget.attrs['placeholder'] = 'ФИО'
        self.fields['company_name'].widget.attrs['placeholder'] = 'Компания'
        self.fields['text'].widget.attrs['placeholder'] = 'Сообщение'

    class Meta:
        model = Proposal
        fields = '__all__'

        labels = {
            'email': '',
            'name': '',
            'company_name': '',
            'text': ''
        }