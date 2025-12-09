from django.forms import ModelForm
from .models import Page, Reply


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ["title", "body", "name"]
        labels = {
            "title": "タイトル",
            "body": "本文",
            "name": "ニックネーム",
        }


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ["body", "name"]
        labels = {
            "body": "本文",
            "name": "ニックネーム",
        }
