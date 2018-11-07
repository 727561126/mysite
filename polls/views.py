from django.shortcuts import get_object_or_404, render
from .models import Question,User

def index(request):
    return render(request,'polls/login.html')

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})  

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
def login(request):
    username=request.POST['username']
    passwd=request.POST['passwd']
    user =get_object_or_404(User,username=username)

    return render(request,'polls/main.html',{'user':user})
def user(request):
    return request(request,'polls/main.html')