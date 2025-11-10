from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre,Publisher
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from  django.contrib.auth.decorators import permission_required

from .forms import RenewBookForm

@login_required
def index(request):
    num_books = Book.objects.all().count()

    num_instances = BookInstance.objects.all().count()

    num_num_instance_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(
        request, 'index.html', context={'num_books': num_books, 'num_instances': num_instances, 'num_num_instance_available': num_num_instance_available, 'num_authors': num_authors, 'num_visits': num_visits}
    )

class BookListView(generic.ListView):
    model = Book

    context_object_name = 'my_book_list'

    template_name = 'catalog/book_list.html'

    

    def get_queryset(self):
        return Book.objects.all()[:5] 
    
    def get_context_data(self, **kwargs):
        context =  super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'какие то непонятные данные'
        return context

class BookDetailView(generic.DetailView):
    model = Book

    
def renew_book_libration(request,pk):
    book_inst = get_object_or_404(BookInstance, pk=pk)

    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()
            return HttpResponseRedirect(reverse('all-borrowed'))
        
        else:
            proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
            form = RenewBookForm(initial={'renewal_date':
                proposed_renewal_date,})
            
            return render(request, 'catalog/book_renew_libration.html',{'form':
                form, 'bookinst':book_inst})




