from django.shortcuts import render
from django.utils import timezone
#from .models import post_list
# Create your views here.

def post_list(request):
	Post.objects.filter(published_data__lte=timezone.now()).order_by('published_data')
	return render(request, 'blog/post_list.html',{'posts':posts})