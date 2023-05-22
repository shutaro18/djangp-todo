
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Task
# Create your views here.

# TaskListはListViewを継承している
# ListViewは、モデルのレコードを一覧表示するためのビュー
# 一覧表示するモデルを指定するには、model属性にモデルクラスを指定する
# 一覧表示するテンプレートを指定するには、template_name属性にテンプレートファイルのパスを指定する
class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'
