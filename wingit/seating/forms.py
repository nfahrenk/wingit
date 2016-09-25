from django.forms import ModelForm, MultipleChoiceField, CharField
from seating.models import Person
from LIKE_CHOICES import CHOICES

class PersonForm(ModelForm):    
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['twitter_handle'] = CharField(required=False)
        self.fields['likes'] = MultipleChoiceField(required=False, choices=CHOICES)

    class Meta:
        model = Person
        fields = ["likes", "twitter_handle"]

