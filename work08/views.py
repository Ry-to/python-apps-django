from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from django.contrib import messages


def top(request):
    memos = Memo.objects.all().order_by("-created_at")  # メモを取得
    return render(request, "work08/top.html", {"memos": memos})  # テンプレに渡す


def create(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        # 🔸 空文字チェック（0文字ならエラー表示して戻す）
        if not title or not content:
            messages.error(request, "タイトルと内容は空にできません。")
            return render(request, "work08/create.html")

        # 🔹 正常時：データベースに保存
        Memo.objects.create(title=title, content=content)
        messages.success(request, "メモを作成しました！")
        return redirect("work08:top")

    # GETアクセス時
    return render(request, "work08/create.html")


def delete(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)

    if request.method == "POST":  # POSTのときだけ削除
        memo.delete()
        messages.success(request, "メモを削除しました。")
        return redirect("work08:top")


# Create your views here.
