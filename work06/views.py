from django.http import HttpResponse
from django.shortcuts import render
from .forms import ReiwaForm, BmiForm, WarikanForm, TyokinForm, SisokuForm


def top(request):
    return render(
        request,
        "work06/index.html",
    )


def reiwa(request):
    result = None
    if request.method == "POST":
        form = ReiwaForm(request.POST)
        if form.is_valid():
            reiwa = form.cleaned_data["reiwa_year"]
            seireki = 2018 + reiwa
            result = f"令和{reiwa}年 → 西暦{seireki}年"
    else:
        form = ReiwaForm()

    return render(request, "work06/reiwa.html", {"form": form, "result": result})


def bmi(request):
    result = None
    if request.method == "POST":
        form = BmiForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data["height"] / 100
            weight = form.cleaned_data["weight"]
            bmi_value = round(weight / (height**2), 2)
            result = f"BMIは {bmi_value} です"
    else:
        form = BmiForm()
    return render(request, "work06/bmi.html", {"form": form, "result": result})


def warikan(request):
    result = None
    if request.method == "POST":
        form = WarikanForm(request.POST)
        if form.is_valid():
            total = form.cleaned_data["total"]
            people = form.cleaned_data["people"]
            share = round(total / people, 2)
            result = f"一人当たり {share} 円です"
    else:
        form = WarikanForm()
    return render(request, "work06/warikan.html", {"form": form, "result": result})


def tyokin(request):
    result = None
    if request.method == "POST":
        form = TyokinForm(request.POST)
        if form.is_valid():
            money = form.cleaned_data["money"]
            year = form.cleaned_data["year"]
            total = round(money * year * 12, 2)
            result = f"{year}年後には {total} 円貯まります"
    else:
        form = TyokinForm()
    return render(
        request, "work06/tyokin.html", {"form": form, "result": result})


def sisoku(request):
    result = None
    if request.method == "POST":
        form = SisokuForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data["a"]
            b = form.cleaned_data["b"]
            addition = a + b
            subtraction = a - b
            multiplication = a * b
            division = round(a / b, 2) if b != 0 else "無限大"
            result = f"足し算: {addition}, 引き算: {subtraction}, 掛け算: {multiplication}, 割り算: {division}"
    else:
        form = SisokuForm()
    return render(
        request, "work06/sisoku.html", {"form": form, "result": result})


# Create your views here.
