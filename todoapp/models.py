from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)

    # __str__メソッドは、オブジェクトを文字列として表現するために使用されます。
    # このメソッドは、モデルのインスタンスを文字列に変換するために使用されます。
    def __str__(self):
        return self.title

    # Metaクラスはモデルの振る舞いを定義するためのものです。
    # orderingは、モデルのクエリセット（データベースからのデータの取得）の結果を並べ替えるために使用されます。
    class Meta:
        ordering = ["completed"]
