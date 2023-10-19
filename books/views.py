from django.shortcuts import render 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Book, Order
from django.urls import reverse_lazy
from django.db.models import Q # for search method
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin 

import json


#use module ListView and build base on list.html
class BooksListView(ListView): 
    model = Book
    template_name = 'list.html'

#similar
class BooksDetailView(DetailView):
    model = Book
    template_name = 'detail.html'

#similar
class SearchResultsListView(ListView):
	model = Book
	template_name = 'search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		return Book.objects.filter(
		Q(title__icontains=query) | Q(author__icontains=query)
		)

#similar
class BookCheckoutView(DetailView):
    model = Book
    template_name = 'checkout.html'
    login_url     = 'login'

#similar
def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Book.objects.get(id=body['productId'])
	Order.objects.create(
		product=product
	)
	return JsonResponse('Payment completed!', safe=False)