from django.shortcuts import render
from .models import SingleBoardComputer, Status
# Create your views here.



def test(request):
  client_list = SingleBoardComputer.objects.all().values("id","name")
  return render(request, 'sbc_monitor/content_fills.html', {"client_list": client_list, })

def test2(request, id):  
  client_list = SingleBoardComputer.objects.all().values("id","name")
  client = SingleBoardComputer.objects.get(id=id)
  log_client = Status.objects.filter(sbc=id).order_by("-updated")
  status = log_client.first() # !!! log_client должен быть отсортирован!
  
  return render(request, 'sbc_monitor/content_fills.html', {
    "client_list": client_list, 
    "log_client":log_client,
    "client":client,    
    "status":status,
  })