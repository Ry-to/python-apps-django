from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import PageForm
from .models import Page
from datetime import date, datetime
from zoneinfo import ZoneInfo


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        today = date.today()
        page_list = Page.objects.filter(page_date=today).order_by("-id")

        datetime_now = datetime.now(ZoneInfo("Asia/Tokyo")).strftime(
            "%Y年%m月%d日 %H時%M分"
        )
        return render(
            request,
            "todo/index.html",
            {"page_list": page_list, "datetime_now": datetime_now},
        )


class PageCreateViwe(LoginRequiredMixin, View):
    def get(self, request):
        form = PageForm()
        return render(request, "todo/page_form.html", {"form": form})

    def post(self, request):
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo:index")
        return render(request, "todo/page_form.html", {"form": form})


class PageListView(LoginRequiredMixin, View):
    def get(self, request):
        page_list = Page.objects.order_by("page_date")
        return render(request, "todo/page_list.html", {"page_list": page_list})


class PageDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "todo/page_detail.html", {"page": page})


class PageUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        form = PageForm(instance=page)
        return render(request, "todo/page_update.html", {"form": form, "page": page})

    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect("todo:page_detail", id=id)
        return render(request, "todo/page_update.html", {"form": form, "page": page})


class PageDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "todo/page_confirm_delete.html", {"page": page})

    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        page.delete()
        return redirect("todo:index")


class PageDoneView(LoginRequiredMixin, View):
    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        page.is_done = not page.is_done
        page.save()
        return redirect("todo:index")


index = IndexView.as_view()
page_create = PageCreateViwe.as_view()
page_list = PageListView.as_view()
page_detail = PageDetailView.as_view()
page_updeta = PageUpdateView.as_view()
page_delete = PageDeleteView.as_view()
