from django.urls import include, path,re_path
from leads import views

urlpatterns = [
        #---- Leads Application ----
        #Dashboard  - gokruze/
        path("", views.home, name="home"),
        #Leads List
        path("leads", views.leads, name="leads"),
        #Routes List
        path("routes", views.routes, name="routes"),
        #Profile Page
        path("profile", views.profile, name="profile"),
        #Users List
        path("users", views.user_list, name="users"),
        #Reports
        path("reports", views.reports, name="reports"),
        #Dashboard Week
        path("dashboard_week", views.dashboard_week, name="dashboard_week"),
        #Dashboard Month
        path("dashboard_month", views.dashboard_month, name="dashboard_month"),
        #---- Django Bootstrap Modal ----
        path('create/', views.LeadCreateView.as_view(), name='create_lead'),
        path('update/<int:pk>', views.LeadUpdateView.as_view(), name='update_lead'),
        path('read/<int:pk>', views.LeadReadView.as_view(), name='read_lead'),
        path('delete/<int:pk>', views.LeadDeleteView.as_view(), name='delete_lead'),
        path('cityread/<int:pk>', views.CityLeadReadView.as_view(), name='city_read_lead'),
        path('cityupdate/<int:pk>', views.CityLeadUpdateView.as_view(), name='city_update_lead'),
        path('citydelete/<int:pk>', views.CityLeadDeleteView.as_view(), name='city_delete_lead'),
        path('routeread/<int:pk>', views.RouteLeadReadView.as_view(), name='route_read_lead'),
        path('routeupdate/<int:pk>', views.RouteLeadUpdateView.as_view(), name='route_update_lead'),
        path('routedelete/<int:pk>', views.RouteLeadDeleteView.as_view(), name='route_delete_lead'),
        #---- Dynamic Pages as per parameters passed ----
        re_path(r'^routes/details/(?P<location_from>[\w\-\s\(\)]+)/(?P<location_to>[\w\-\s\(\)]+)/(?P<lead_status>\w+)/$',views.routes_leads_list,name='user_routes_details'),
        re_path(r'^city/details/(?P<city>[\w\-\s]+)/$',views.city_routes_list,name='city_routes_list'),
        re_path(r'^leads/(?P<city>[\w\-\s]+)/$',views.city_leads_list,name='city_leads_list'),
        re_path(r'^dashboard/(?P<lead_status>\w+)/$',views.dashboard_status,name='dashboard_status'),
        re_path(r'^week/(?P<lead_status>\w+)/$',views.week,name='week'),
        re_path(r'^month/(?P<lead_status>\w+)/$',views.month,name='month'),
        # re_path(r'^city/lead_status/(?P<lead_status>\w+)/$',views.city_leadstatus,name='city_leadstatus'),
]
