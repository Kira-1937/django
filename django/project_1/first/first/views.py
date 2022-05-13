from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
      return render(request,"index.html")

   # data ={
    #    'title':'just first1 project',
    #    'bdata':'why are u gay',
     #   'clist':['Php','java','c','c++'],
     #   'numbers':[10,20,30,40,50],
    #    'student_table':[
    #        {'name':'mohit','phone_no':6969696969},
    #        {'name':'vikram','phone_no':8901097310},
    #    ]
   # }
    
def aboutUs(request):
   return render(request,"table.html")
    
# def course(request):
#         return HttpResponse("welcome to course")

# def coursedetails(request,courseid):
#             return HttpResponse(courseid)