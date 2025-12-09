from django.db import models
import uuid


class Page(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID"
    )
    title = models.CharField(max_length=100, verbose_name="タイトル")
    body = models.TextField()
    name = models.CharField(max_length=30, default="名無し")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")

    def __str__(self):
        return self.title


class Reply(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="replies")
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="children"
    )
    name = models.CharField(default="名無し", max_length=30)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply to {self.page.title}"
