from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib import messages
from datetime import datetime


def top(request):
    if request.method == "POST":
        # フォームから値を取得
        title = request.POST.get("title", "").strip()
        deadline_str = request.POST.get("deadline", "").strip()

        # タイトルは必須
        if not title:
            messages.error(request, "タイトルは必須です。")
        else:
            todo = Todo(title=title)

            # 期限日が入力されていれば変換してセット
            if deadline_str:
                try:
                    # HTMLの datetime-local は "YYYY-MM-DDTHH:MM" 形式
                    todo.deadline = datetime.strptime(deadline_str, "%Y-%m-%dT%H:%M")
                except ValueError:
                    messages.error(request, "期限日の形式が正しくありません。")
                    return redirect("work09:top")

            # データベースに保存
            todo.save()
            return redirect("work09:top")  # POST後はリダイレクト

    # GETのとき、またはPOST後に一覧表示
    todos = Todo.objects.all().order_by("deadline")
    return render(request, "work09/top.html", {"todos": todos})


def delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)

    if request.method == "POST":  # POSTのときだけ削除
        todo.delete()
        return redirect("work09:top")
