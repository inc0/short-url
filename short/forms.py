# -*- coding: utf-8 -*-
from django import forms
from models import *

class UrlForm(forms.Form):
    url = forms.URLField(label=u"Url you wish to crop")