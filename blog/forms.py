from django.forms import ModelForm, Textarea
from .models import Blogpost

class PostForm(ModelForm):
    class Meta:
        model = Blogpost
        fields = '__all__'

        widgets = {
            'body': Textarea()
        }