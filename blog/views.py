import re
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.utils.http import urlencode
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
)
import operator
from django.urls import reverse_lazy
from django.contrib.staticfiles.views import serve
from django.http import HttpResponseRedirect
from django.db.models import Q
from PIL import Image
from django.conf import settings
import requests 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .forms import UserReviewForm
from .models import UserReview
from django.db.models import Avg


def handler404(request, exception=None):
    return render(request, 'blog/404.html')
def handler500(request, exception=None):
    return render(request, 'blog/500.html')
def brewery(request, id):
    url = "https://api.openbrewerydb.org/v1/breweries/" + id
    header = {
    "Content-Type":"application/json",
    }
    
    brewery_result = requests.get(url,headers=header)
    if brewery_result.status_code == 200:
        brewery_data = brewery_result.json()
    else:
        brewery_data = "Error"
    try:
        average_review = UserReview.objects.filter(breweryId=id).aggregate(avg_review=Avg('rate'))['avg_review']

    except UserReview.DoesNotExist:
        average_review = "No reviews"
    try:
        user_review = get_object_or_404(UserReview, breweryId=id, userName=request.user.username)
        check_field_value = user_review.check_field
    except Http404:
        check_field_value=True

    

    if request.method == 'POST':
        form = UserReviewForm(request.POST)
        rate_query=request.POST.get('rate')
        if form.is_valid():
            form.instance.breweryId = id
            form.instance.userName = request.user.username
            form.instance.rate = rate_query
            form.instance.check_field = False
            form.save()
            messages.success(request, 'Your review has been added successfully!')
            return redirect(reverse('brewery', args=[id]))

    else:
        form = UserReviewForm()
    context = {
        'brewery_data' : brewery_data,
        'form' : form,
        'rating': average_review,
        'check' : check_field_value
    } 
    
    return render(request, 'blog/brewery_details.html', context)


def br(request):
    url = "https://api.openbrewerydb.org/v1/breweries?per_page=200"
    header = {
    "Content-Type":"application/json",
    }
    
    results = requests.get(url,headers=header)
    if results.status_code == 200:
        data = results.json()
    else:
        data = "error"
    
    p = Paginator(data, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    if not bool(data) or data=="error":
        context = {'results' : '','page_obj': '', 'status':'error' }      
    else:
        context = {'results' : data, 'page_obj': page_obj, 'status':'no_error' }
   
     
    return render(request,'blog/home.html' ,context)


@login_required(redirect_field_name=None)
def search(request):
   
    querr=request.GET.get('q')
    query_option=request.GET.get('select_option')
    print(query_option)
    query=querr.strip()
    uquery=query.lower().replace(" ", "_")
    uquery=re.sub(r'_{2,}', '_', uquery)
    if query=="":
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    
    else:
        pass
    url=""
    header = {
    "Content-Type":"application/json",
    }
    if query_option==None or query_option=="search":
        url= "https://api.openbrewerydb.org/v1/breweries/search?query="+uquery+"&per_page=200"
    elif query_option=="name":
        url = "https://api.openbrewerydb.org/v1/breweries?by_name="+uquery+"&per_page=200"
    elif query_option=="city":
        url = "https://api.openbrewerydb.org/v1/breweries?by_city="+uquery+"&per_page=200"
    elif query_option=="type":
        url = "https://api.openbrewerydb.org/v1/breweries?by_type="+uquery+"&per_page=200"
    
    results = requests.get(url,headers=header)
    if results.status_code == 200:
        data = results.json()
    else:
        data = "error"
    
    p = Paginator(data, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    if not bool(data) or data=="error":
        context = {'results' : '', 'page_obj': '', 'search' : query, 'query_option' : query_option, 'status':'error' }

    else:
        context = {'results' : data, 'page_obj': page_obj, 'search' : query, 'query_option' : query_option, 'status':'no_error' }
   
     
    return render(request,'blog/search.html' ,context)
   


def getfile(request):
   return serve(request, 'File')

class UserPostListView(ListView):
    template_name = 'blog/user_posts.html'  

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return user

        #return Post.objects.filter(author=user).order_by('-date_posted')


