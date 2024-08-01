from django.shortcuts import render
from django.core.mail import send_mail,settings
from django.http import HttpResponse
from django.views import View


# Create your views here.
class SendEmailView(View):
  def get(self,request):
    sub="Welcome"
    msg="This is from Django"
    from_addr=settings.EMAIL_HOST_USER
    to='hashimmohammedtp@gmail.com'
    # print(sub,msg,from_addr,to)
    res=send_mail(sub,msg,from_addr,[to])
    if res==1:
      return HttpResponse("Email send successfull")
    else:
      return HttpResponse("Falild to Send!")

class MailSendView(View):
  def get(self,request):
    return render(request,'emailSend.html')
  def post(self,request):
    sub=request.POST.get("sub")
    msg=request.POST.get("msg")
    to=request.POST.get("to")
    from_addr=settings.EMAIL_HOST_USER
    res=send_mail(sub,msg,from_addr,[to])
    if res==1:
      return HttpResponse("Email send successfull")
    else:
      return HttpResponse("Falild to Send!")