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
from datetime import date, datetime
import datetime
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from leads import count_values
from leads import count_functions

# ----- Leads Application Views -----
#Home View
@login_required
def home(request):
    """Generates the two Dashboard Tables and Graph
    Parameters: HttpRequest object
    Returns : Nothing"""
    user_role = request.user.role
    return render(request, 'leads/dashboard.html', { 'total': count_values.total_dict, 'week': count_values.week_dict, 'month': count_values.month_dict, 'total_collect': count_values.total_collect, 'user_role': user_role, 'mumbai' : count_values.mumbai_dict, 'kochi' : count_values.kochi_dict, 'pune' : count_values.pune_dict, 'hyderabad' : count_values.hyderabad_dict , 'banglore' : count_values.banglore_dict, 'calcutta' : count_values.calcutta_dict, 'total_city_collect': count_values.total_city_collect })

# Lead List
@login_required
def leads(request):
    """Lists all leads collected
    Parameters: HttpRequest object
    Returns : Nothing"""
    user_role = request.user.role
    leads = Leads.objects.all()
    return render(request, 'leads/lead_list.html', { 'leads': leads,'user_role': user_role })

#Leads City
@login_required
def city_leads_list(request,city):
    """Lists all leads collected city wise
    Parameters: HttpRequest object, city
    Returns : Nothing"""
    user_role = request.user.role
    city_global = city
    leads = Leads.objects.filter(City=city)
    return render(request, 'leads/lead_city.html', { 'leads': leads,'city':city, 'user_role': user_role })

#Routes
@login_required
def routes(request):
    """Lists all Routes Generated
    Parameters: HttpRequest object
    Returns : Nothing"""
    user_role = request.user.role
    leads = Leads.objects.all()
    return render(request, 'routes/route_list.html', { 'routes_dict': count_values.routes_dict, 'user_role': user_role })

#Routes Detailed
@login_required
def routes_leads_list(request,location_from,location_to,lead_status):
    """Lists all Routes Generated based on location_From, location_To and Lead_Status
    Parameters: HttpRequest object, location_from,location_to,lead_status
    Returns : Nothing"""
    user_role = request.user.role
    leads = Leads.objects.filter(LocationFrom=location_from, LocationTo=location_to, Lead_Status =lead_status)
    return render(request, 'routes/routes_details.html', { 'leads': leads,'locationFrom': location_from,'locationTo': location_to, 'lead_status':lead_status, 'user_role': user_role })

#Routes City
@login_required
def city_routes_list(request,city):
    """Lists all Routes Generated based on City
    Parameters: HttpRequest object, City
    Returns : Nothing"""
    user_role = request.user.role
    x = list(set(list(Leads.objects.filter(City=city).values_list('LocationFrom', 'LocationTo','LocationFromOther'))))
    lead_Status_list = ["Uncontacted","Undecided","Converted","Interested"]
    routes = [ count_functions.Total_Routes_Count(a,lead_status) for a in x for lead_status in lead_Status_list ]
    final = [routes[i * 4:(i + 1) * 4] for i in range((len(routes) + 4 - 1) // 4 )]
    routes_dict = dict(zip(x, final))
    return render(request, 'routes/route_list.html', { 'routes_dict': routes_dict, 'user_role': user_role})
#Profile
@login_required
def profile(request):
    """Generates User Profile Details
    Parameters: HttpRequest object
    Returns : Nothing"""
    username = request.user.username
    user_role = request.user.role
    login = request.user.last_login + datetime.timedelta(hours=5,minutes=30)
    date_join = request.user.date_joined + datetime.timedelta(hours=5,minutes=30)
    data = { 'username': username , 'user_role': user_role, 'login' : login, 'date_join' : date_join }
    return render(request, 'accounts/profile.html', data )

#User
@login_required
def user_list(request):
    """List of All The Users of Application
    Parameters: HttpRequest object
    Returns : Nothing"""
    user_role = request.user.role
    users = CustomUser.objects.all()
    data = {'users' : users , 'user_role': user_role }
    return render(request, 'accounts/userlist.html', data )

@login_required
def reports(request):
    """Analytical Report
    Parameters: HttpRequest object
    Returns : Nothing"""
    user_role = request.user.role
    return render(request, 'reports/reports.html', { 'total': count_values.total_dict, 'week': count_values.week_dict, 'month': count_values.month_dict, 'total_collect': count_values.total_collect, 'user_role': user_role, 'mumbai' : count_values.mumbai_dict, 'kochi' : count_values.kochi_dict, 'pune' : count_values.pune_dict, 'hyderabad' : count_values.hyderabad_dict , 'banglore' : count_values.banglore_dict, 'calcutta' : count_values.calcutta_dict, 'total_city_collect': count_values.total_city_collect } )

@login_required
def dashboard_status(request,lead_status):
    user_role = request.user.role
    leads = Leads.objects.filter(Lead_Status = lead_status)
    return render(request, 'leads/lead_list.html', { 'leads': leads,'user_role': user_role })

@login_required
def dashboard_week(request):
    user_role = request.user.role
    today = datetime.datetime.now()
    week_start_date = today - datetime.timedelta(days=7)
    leads = Leads.objects.filter(SubmittedOnDate__range=[week_start_date, today]).all()
    return render(request, 'leads/lead_list.html', { 'leads': leads,'user_role': user_role })

@login_required
def dashboard_month(request):
    user_role = request.user.role
    today = datetime.datetime.now()
    week_start_date = today - datetime.timedelta(days=30)
    leads = Leads.objects.filter(SubmittedOnDate__range=[week_start_date, today]).all()
    return render(request, 'leads/lead_list.html', { 'leads': leads,'user_role': user_role })

@login_required
def week(request,lead_status):
    user_role = request.user.role
    today = datetime.datetime.now()
    week_start_date = today - datetime.timedelta(days=7)
    leads = Leads.objects.filter(Lead_Status = lead_status).filter(SubmittedOnDate__range=[week_start_date, today]).all()
    return render(request, 'leads/lead_list.html', { 'leads': leads,'user_role': user_role })

@login_required
def month(request,lead_status):
    user_role = request.user.role
    today = datetime.datetime.now()
    week_start_date = today - datetime.timedelta(days=30)
    leads = Leads.objects.filter(Lead_Status = lead_status).filter(SubmittedOnDate__range=[week_start_date, today]).all()
    return render(request, 'leads/lead_list.html', { 'leads': leads,'user_role': user_role })

# def city_leadstatus(request,)
# ----- Modals for lead_list View -----
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

#------------------- MODIFY City LEADS ----------------------

@method_decorator(login_required, name='dispatch')
class CityLeadUpdateView(BSModalUpdateView):
    model = Leads
    template_name = 'leads/lead_update.html'
    form_class = LeadForm
    success_message = 'Success: Lead was updated.'

    def get_success_url(self,**kwargs):
        lead_object = Leads.objects.get(pk=self.kwargs['pk'])
        city = lead_object.City
        return reverse_lazy('city_leads_list', kwargs={'city': city })

@method_decorator(login_required, name='dispatch')
class CityLeadReadView(BSModalReadView):
    model = Leads
    template_name = 'leads/lead_read.html'

class CityLeadDeleteView(BSModalDeleteView):
    model = Leads
    template_name = 'leads/lead_delete.html'
    success_message = 'Success: Lead was deleted.'

    def get_success_url(self,**kwargs):
        lead_object = Leads.objects.get(pk=self.kwargs['pk'])
        city = lead_object.City
        return reverse_lazy('city_leads_list', kwargs={'city': city })

class RouteLeadUpdateView(BSModalUpdateView):
    model = Leads
    template_name = 'leads/lead_update.html'
    form_class = LeadForm
    success_message = 'Success: Lead was updated.'

    def get_success_url(self,**kwargs):
        lead_object = Leads.objects.get(pk=self.kwargs['pk'])
        location_from = lead_object.LocationFrom
        location_to = lead_object.LocationTo
        lead_status = lead_object.Lead_Status
        return reverse_lazy('user_routes_details', kwargs={'location_from':location_from, 'location_to':location_to, 'lead_status':lead_status })

@method_decorator(login_required, name='dispatch')
class RouteLeadReadView(BSModalReadView):
    model = Leads
    template_name = 'leads/lead_read.html'

class RouteLeadDeleteView(BSModalDeleteView):
    model = Leads
    template_name = 'leads/lead_delete.html'
    success_message = 'Success: Lead was deleted.'

    def get_success_url(self,**kwargs):
        lead_object = Leads.objects.get(pk=self.kwargs['pk'])
        location_from = lead_object.LocationFrom
        location_to = lead_object.LocationTo
        lead_status = lead_object.Lead_Status
        return reverse_lazy('user_routes_details', kwargs={'location_from':location_from, 'location_to':location_to, 'lead_status':lead_status })