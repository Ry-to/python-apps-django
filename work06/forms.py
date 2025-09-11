from django import forms


class ReiwaForm(forms.Form):
    reiwa_year = forms.IntegerField(label="令和何年？", min_value=1)


class BmiForm(forms.Form):
    height = forms.FloatField(label="身長 (cm)", min_value=0)
    weight = forms.FloatField(label="体重 (kg)", min_value=0)


class WarikanForm(forms.Form):
    total = forms.FloatField(label="合計金額 (円)", min_value=0)
    people = forms.IntegerField(label="人数", min_value=1)


class TyokinForm(forms.Form):
    money = forms.FloatField(label="月の貯金額 (円)", min_value=0)
    year = forms.IntegerField(label="年 (年)", min_value=0)


class SisokuForm(forms.Form):
    a = forms.FloatField(label="１つ目の数字", min_value=0)
    b = forms.FloatField(label="２つ目の数字", min_value=0)
