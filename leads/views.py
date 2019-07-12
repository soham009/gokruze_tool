# Create your views here.
from django.shortcuts import render
from .forms import LeadForm
from django.urls import reverse_lazy
from django.views.generic import View, ListView, TemplateView
from leads.models import Leads, CustomUser
from django.views import generic
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
import datetime
from datetime import date
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
city_global = ''
# Create your views here

#Home View
@login_required
def home(request):
    user_role = request.user.role
    lead_Status_list = ["Uncontacted","Undecided","Converted","Interested"]
    total = [ Total_Count_LeadStatus(x) for x in lead_Status_list ]
    week = [ Weekly_Count_LeadStatus(x) for x in lead_Status_list ]
    month = [ Monthly_Count_LeadStatus(x) for x in lead_Status_list ]
    total_dict = dict(zip(lead_Status_list, total))
    week_dict = dict(zip(lead_Status_list, week))
    month_dict = dict(zip(lead_Status_list, month))
    total_collect = { 'all': Total_Count(), 'week': Weekly_Count(), 'month': Montly_Count(),}
    return render(request, 'dashboard.html', { 'total': total_dict, 'week': week_dict, 'month': month_dict, 'total_collect': total_collect, 'user_role': user_role })

# Lead List
@login_required
def leads(request):
    user_role = request.user.role
    leads = Leads.objects.all()
    return render(request, 'leads/lead_list.html', { 'leads': leads,'user_role': user_role })

#Leads City
@login_required
def city_leads_list(request,city):
    user_role = request.user.role
    city_global = city
    leads = Leads.objects.filter(City=city)
    return render(request, 'leads/city.html', { 'leads': leads,'city':city, 'user_role': user_role })


#Routes
@login_required
def routes(request):
    user_role = request.user.role
    leads = Leads.objects.all()
    x = list(set(list(Leads.objects.values_list('LocationFrom', 'LocationTo','LocationFromOther'))))
    lead_Status_list = ["Uncontacted","Undecided","Converted","Interested"]
    routes = [ Total_Routes_Count(a,lead_status) for a in x for lead_status in lead_Status_list ]
    final = [routes[i * 4:(i + 1) * 4] for i in range((len(routes) + 4 - 1) // 4 )]
    routes_dict = dict(zip(x, final))
    return render(request, 'routes_bus/route_list.html', { 'routes_dict': routes_dict, 'user_role': user_role })

#Routes Detailed
@login_required
def routes_leads_list(request,location_from,location_to,lead_status):
    user_role = request.user.role
    leads = Leads.objects.filter(LocationFrom=location_from, LocationTo=location_to, Lead_Status =lead_status)
    return render(request, 'routes_bus/routes_details.html', { 'leads': leads,'locationFrom': location_from,'locationTo': location_to, 'lead_status':lead_status, 'user_role': user_role })

#Routes City
@login_required
def city_routes_list(request,city):
    user_role = request.user.role
    x = list(set(list(Leads.objects.filter(City=city).values_list('LocationFrom', 'LocationTo','LocationFromOther'))))
    lead_Status_list = ["Uncontacted","Undecided","Converted","Interested"]
    routes = [ Total_Routes_Count(a,lead_status) for a in x for lead_status in lead_Status_list ]
    final = [routes[i * 4:(i + 1) * 4] for i in range((len(routes) + 4 - 1) // 4 )]
    routes_dict = dict(zip(x, final))
    return render(request, 'routes_bus/route_list.html', { 'routes_dict': routes_dict, 'user_role': user_role})

#Profile
@login_required
def profile(request):
    username = request.user.username
    user_role = request.user.role
    login = request.user.last_login + datetime.timedelta(hours=5,minutes=30)
    date_join = request.user.date_joined + datetime.timedelta(hours=5,minutes=30)
    data = { 'username': username , 'user_role': user_role, 'login' : login, 'date_join' : date_join }
    return render(request, 'profile.html', data )

#User
@login_required
def user_list(request):
    user_role = request.user.role
    users = CustomUser.objects.all()
    data = {'users' : users , 'user_role': user_role }
    return render(request, 'userlist.html', data )

@login_required
def reports(request):
    user_role = request.user.role
    data = {'user_role': user_role }
    return render(request, 'reports.html', data )

#------------------- Counts ----------------------

#Total_Count
def Total_Count():
    count = Leads.objects.all().count()
    return count

#Weekly_Count
def Weekly_Count():
    today = datetime.datetime.now()
    week_start_date = today - datetime.timedelta(days=7)
    count = Leads.objects.filter(SubmittedOnDate__range=[week_start_date, today]).count()
    return count

#Montly_Count
def Montly_Count():
    today = datetime.datetime.now()
    month_start_date = today - datetime.timedelta(days=30)
    count = Leads.objects.filter(SubmittedOnDate__range=[month_start_date, today]).count()
    return count


#Total_Count_LeadStatus
def Total_Count_LeadStatus(lead_status):
    count = Leads.objects.filter(Lead_Status=lead_status).count()
    return count

#Weekly_Count_LeadStatus
def Weekly_Count_LeadStatus(lead_status):
    today = datetime.datetime.now()
    week_start_date = today - datetime.timedelta(days=7)
    count = Leads.objects.filter(Lead_Status=lead_status).filter(SubmittedOnDate__range=[week_start_date, today]).count()
    return count

#Monthly_Count_LeadStatus
def Monthly_Count_LeadStatus(lead_status):
    today = datetime.datetime.now()
    month_start_date = today - datetime.timedelta(days=30)
    count = Leads.objects.filter(Lead_Status=lead_status).filter(SubmittedOnDate__range=[month_start_date, today]).count()
    return count


def Total_Routes_Count(a,lead_status):
    if(a[0]=='Other'):
        count = Leads.objects.filter(LocationFromOther = a[2],LocationTo = a[1],Lead_Status=lead_status).count()
    else:
        count = Leads.objects.filter(LocationFrom = a[0],LocationTo = a[1],Lead_Status=lead_status).count()
    return count

#------------------- MODIFY LEADS ----------------------
@method_decorator(login_required, name='dispatch')
class LeadCreateView(BSModalCreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadForm
    success_message = 'Success: Lead was created.'
    success_url = reverse_lazy('leads')

@method_decorator(login_required, name='dispatch')
class LeadUpdateView(BSModalUpdateView):
    model = Leads
    template_name = 'leads/lead_update.html'
    form_class = LeadForm
    success_message = 'Success: Lead was updated.'
    success_url = reverse_lazy('leads')

@method_decorator(login_required, name='dispatch')
class LeadReadView(BSModalReadView):
    model = Leads
    template_name = 'leads/lead_read.html'

@method_decorator(login_required, name='dispatch')
class LeadDeleteView(BSModalDeleteView):
    model = Leads
    template_name = 'leads/lead_delete.html'
    success_message = 'Success: Lead was deleted.'
    success_url = reverse_lazy('leads')
""" 
#------------------- MODIFY City LEADS ----------------------
@method_decorator(login_required, name='dispatch')
class CityLeadUpdateView(BSModalUpdateView):
    model = Leads
    template_name = 'leads/lead_update.html'
    form_class = LeadForm
    success_message = 'Success: Lead was updated.'
    success_url = reverse_lazy('reports', kwargs={'city': city_global })

@method_decorator(login_required, name='dispatch')
class CityLeadReadView(BSModalReadView):
    model = Leads
    template_name = 'leads/lead_read.html' """