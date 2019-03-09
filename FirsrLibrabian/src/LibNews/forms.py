from django.forms.models import ModelForm
from LibNews.models import LibNews



class NewsForm(ModelForm):
    class Meta:
        model = LibNews
        fields = '__all__'