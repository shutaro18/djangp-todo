
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .models import Task
# Create your views here.

# TaskListはListViewを継承している
# ListViewは、モデルのレコードを一覧表示するためのビュー
# 一覧表示するモデルを指定するには、model属性にモデルクラスを指定する
# 一覧表示するテンプレートを指定するには、template_name属性にテンプレートファイルのパスを指定する
class TaskList(ListView):
    model = Task
    # template_name = 'task_list.html'
    # <!-- html側のobject_listは分かりにくためviews.pyでcontext_object_nameを設定している -->
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    # template_name = 'task_detail.html'
    context_object_name = 'task'


class TaskCreate(CreateView):
    model = Task

    #fieldsは、モデルのフィールドを指定する
    # __all__は、モデルの全フィールドを指定する
    fields = '__all__'

    # success_urlは、レコード作成後に遷移するURLを指定する
    # reverse_lazyは、xxx-form.htmlのボタンを押した後に遷移するURLを指定する
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    context_object_name = 'task'
