from django.shortcuts import render, redirect
from .models import Memo


def top(request):
    memos = Memo.objects.all().order_by("-created_at")  # メモを取得
    return render(request, "work08/top.html", {"memos": memos})  # テンプレに渡す


def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Memo.objects.create(title=title, content=content)
        return redirect("work08:top")

    return render(request, "work08/create.html")


# Create your views here.
