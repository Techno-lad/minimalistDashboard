from django.shortcuts import render

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, Avg #F, Sum
#from django.db.models.functions import ExtractYear, ExtractMonth
from django.http import JsonResponse

from employeeDash.models import Employees,Supervisor
#from utils.charts import months, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict



from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response





# Create your views here.

def get_data(request, *args, **kwargs):   #need to reveiw for endpoint clarity
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        supervisor = Supervisor.objects.all()
        employee   = Employees.objects.all()

        #supervisor location style querytset
        sup_qs_remotecount = supervisor.filter(location='remote').count() 
        sup_qs_onsitecount = supervisor.filter(location='onsite').count()
        sup_qs_hybridcount = supervisor.filter(location='hybrid').count()

        #employee location style querytset
        emp_qs_remotecount = employee.filter(location='remote').count()
        emp_qs_onsitecount = employee.filter(location='onsite').count()
        emp_qs_hybridcount = employee.filter(location='hybrid').count()

        #supervisor/team Avg handletime based on team members individual averages; This approach can be improved using a filter options for large volume dataset; for ref check django-interactive charts projects
        sup00_qs_avgChats = employee.filter(supervisor_id='Sup100').aggregate(Avg('Total_Chats'))['Total_Chats__avg'] #NB: ['TeamAvg_Cx_rating__avg'] used to obtain only the numeric value
        sup01_qs_avgChats = employee.filter(supervisor_id='Sup101').aggregate(Avg('Total_Chats'))['Total_Chats__avg']   
        sup02_qs_avgChats = employee.filter(supervisor_id='Sup102').aggregate(Avg('Total_Chats'))['Total_Chats__avg']
        sup03_qs_avgChats = employee.filter(supervisor_id='Sup103').aggregate(Avg('Total_Chats'))['Total_Chats__avg']
        sup04_qs_avgChats = employee.filter(supervisor_id='Sup104').aggregate(Avg('Total_Chats'))['Total_Chats__avg']
        
        sup00_qs_avgHt = supervisor.filter(SupervisorId='Sup100').aggregate(Avg('TeamAvg_HandleTime'))['TeamAvg_HandleTime__avg']
        sup01_qs_avgHt = supervisor.filter(SupervisorId='Sup101').aggregate(Avg('TeamAvg_HandleTime'))['TeamAvg_HandleTime__avg']
        sup02_qs_avgHt = supervisor.filter(SupervisorId='Sup102').aggregate(Avg('TeamAvg_HandleTime'))['TeamAvg_HandleTime__avg']
        sup03_qs_avgHt = supervisor.filter(SupervisorId='Sup103').aggregate(Avg('TeamAvg_HandleTime'))['TeamAvg_HandleTime__avg']
        sup04_qs_avgHt = supervisor.filter(SupervisorId='Sup104').aggregate(Avg('TeamAvg_HandleTime'))['TeamAvg_HandleTime__avg']

        sup00_qs_avgCxr = supervisor.filter(SupervisorId='Sup100').aggregate(Avg('TeamAvg_Cx_rating'))['TeamAvg_Cx_rating__avg']
        sup01_qs_avgCxr = supervisor.filter(SupervisorId='Sup101').aggregate(Avg('TeamAvg_Cx_rating'))['TeamAvg_Cx_rating__avg']
        sup02_qs_avgCxr = supervisor.filter(SupervisorId='Sup102').aggregate(Avg('TeamAvg_Cx_rating'))['TeamAvg_Cx_rating__avg']
        sup03_qs_avgCxr = supervisor.filter(SupervisorId='Sup103').aggregate(Avg('TeamAvg_Cx_rating'))['TeamAvg_Cx_rating__avg']
        sup04_qs_avgCxr = supervisor.filter(SupervisorId='Sup104').aggregate(Avg('TeamAvg_Cx_rating'))['TeamAvg_Cx_rating__avg']

        #supervisor location style querytset data
        labels = ["remote", "onsite", "hybrid"]
        default_items = [sup_qs_remotecount, sup_qs_onsitecount, sup_qs_hybridcount ]

        #employee location style querytset data
        labels1 = ["remote", "onsite", "hybrid"]
        default_items1 = [emp_qs_remotecount, emp_qs_onsitecount, emp_qs_hybridcount ]
        
        labels3 = ["AvgChats", "AvgTeamHandleTime", "TeamAvg_Cx_rating"]
        default_items3 = [sup00_qs_avgChats, sup00_qs_avgHt, sup00_qs_avgCxr]
        default_items4 = [sup01_qs_avgChats, sup01_qs_avgHt, sup01_qs_avgCxr]
        default_items5 = [sup02_qs_avgChats, sup02_qs_avgHt, sup02_qs_avgCxr]
        default_items6 = [sup03_qs_avgChats, sup03_qs_avgHt, sup03_qs_avgCxr]
        default_items7 = [sup04_qs_avgChats, sup04_qs_avgHt, sup04_qs_avgCxr]

        data = {    #NB  labels and default appears to be special keywords in chartjs the only vhange that can be made to the strings is in the foll []labels[] or []default[]
                "labels":   labels,
                "default":  default_items,

                "labels1":  labels1,
                "default1": default_items1,


                "labels3": labels3,
                "default3": default_items3,
                "default4": default_items4,
                "default5": default_items5,
                "default6": default_items6,
                "default7": default_items7
        }
        return Response(data)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})