from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Book, jpro
from django.views import generic


class IndexView(generic.ListView):
    model = Book
    template_name = 'cms/book_list.html'
    context_object_name = 'books'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        books = Book.objects.all().order_by('id')
        self.object_list = books

        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)

class JproView(generic.ListView):
    model = jpro
    template_name = 'cms/jpro_list.html'
    context_object_name = 'jpro_books'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        jpro_books = jpro.objects.all().order_by('id')
        self.object_list = jpro_books

        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)

def book_edit(request, book_id=None):
    """書籍の編集"""
    return HttpResponse('書籍の編集')

def book_del(request, book_id):
    """書籍の削除"""
    return HttpResponse('書籍の削除')
