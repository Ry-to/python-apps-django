from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def create(request):
    if request.method == "POST":
        Task.objects.create(
            title=request.POST["title"],
            description=request.POST.get("description", ""),
            due_time=request.POST["due_time"],
        )
        return redirect("todo")  # 作成後に一覧ページへ
    return render(request, "create.html")


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed  # 完了フラグを反転
    task.save()
    return redirect("todo")


def todo(request):
    # 未完了(False) → 完了(True) の順に、さらに due_time 昇順で並べる
    tasks = Task.objects.all().order_by("completed", "due_time")
    return render(request, "todo.html", {"tasks": tasks})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("todo")  # 削除後は一覧ページに戻る


# Create your views here.
