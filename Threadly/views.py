from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import PageForm
from datetime import datetime
from zoneinfo import ZoneInfo
from django.urls import reverse
from .models import Page
from .models import Page, Reply
from .forms import PageForm, ReplyForm
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.http import HttpResponse


class IndexView(View):
    def get(self, request):
        datetime_now = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y/%m/%d")
        return render(request, "Threadly/index.html", {"datetime_now": datetime_now})


class PageCreateView(View):
    def get(self, request):
        form = PageForm()
        return render(request, "Threadly/page_create.html", {"form": form})

    def post(self, request):
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save()
            # 投稿後はリダイレクト推奨
            return redirect(reverse("Threadly:page_detail", args=[page.id]))
        return render(request, "Threadly/page_create.html", {"form": form})


class PageDetailView(View):
    def get(self, request, pk):
        page = get_object_or_404(Page, pk=pk)
        reply_form = ReplyForm()
        replies = page.replies.all().order_by("created_at")  # 親の投稿に紐づく返信

        return render(
            request,
            "Threadly/page_detail.html",
            {"page": page, "reply_form": reply_form, "replies": replies},
        )

    def post(self, request, pk):
        page = get_object_or_404(Page, pk=pk)
        reply_form = ReplyForm(request.POST)

        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.page = page
            reply.save()

            return redirect(reverse("Threadly:page_detail", args=[pk]))

        # 失敗した時
        replies = page.replies.all().order_by("created_at")
        return render(
            request,
            "Threadly/page_detail.html",
            {"page": page, "reply_form": reply_form, "replies": replies},
        )


class PagelistView(View):
    def get(self, request):
        page_list = Page.objects.all().order_by("-created_at")
        return render(request, "Threadly/page_list.html", {"page_list": page_list})


def bootstrap_admin(request):
    User = get_user_model()

    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin", email="admin@example.com", password="admin1234"
        )
        return HttpResponse("admin created")

    return HttpResponse("admin already exists")


index = IndexView.as_view()
PageCreateView = PageCreateView.as_view()
PagelistView = PagelistView.as_view()
