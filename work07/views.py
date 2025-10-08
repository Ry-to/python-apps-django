from django.http import HttpResponse
from django.shortcuts import render
import random


def top(request):
    return render(request, "work07/top.html")


def omikuji(request):
    result = None
    if request.method == "POST":
        omikuji_list = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]
        result = random.choice(omikuji_list)
    return render(request, "work07/omikuji.html", {"result": result})


def janken(request):
    result = None
    Computer_hand = None
    if request.method == "POST":
        choices = ["グー", "チョキ", "パー"]
        User_hand = request.POST.get("hand")
        Computer_hand = random.choice(choices)
        if User_hand == Computer_hand:
            result = "あいこ"
        elif (
            (User_hand == "グー" and Computer_hand == "チョキ")
            or (User_hand == "チョキ" and Computer_hand == "パー")
            or (User_hand == "パー" and Computer_hand == "グー")
        ):
            result = "あなたの勝ち"
        else:
            result = "あなたの負け"
    return render(request, "work07/janken.html", {"result": result})


def HiandLow(request):
    result = None
    Computer_hand = None
    if request.method == "POST":
        Computer_hand = random.randint(1, 10)
        User_hand = request.POST.get("hand")
        if Computer_hand == 5:
            result = f"引き分け。コンピュータの数字は{Computer_hand}でした"
        elif User_hand == "Hi" and Computer_hand > 5:
            result = f"あなたの勝ち。コンピュータの数字は{Computer_hand}でした"
        elif User_hand == "Low" and Computer_hand < 5:
            result = f"あなたの勝ち。コンピュータの数字は{Computer_hand}でした"
    return render(
        request,
        "work07/hiandrow.html",
        {
            "result": result,
            "computer_hand": Computer_hand,
        },
    )


# Create your views here.
