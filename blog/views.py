from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'base.html')

#rename index.html base.html
class HomePageView(ListView):
	model=Post
	template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name ='post_detail.html'
def AboutPageView(request):
    return render(request,'about.html')

def ContactPageView(request):
    if request.method == 'POST':
        message_name=request.POST['cName']
        message_email=request.POST['cEmail']
        message=request.POST['cMessage']
        send_mail(
            message_name,#name or subject
            message,#message
            message_email,#from_email
           ['sydsulmn7@gmail.com'] #reciepant mail
        )
        return render(request,'contact.html',{"message_name":message_name})
    else:
        return render(request,'contact.html')