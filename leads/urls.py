from django.urls import include, path,re_path
from leads import views

urlpatterns = [
        path("", views.home, name="home"),
        path("leads", views.leads.as_view(), name="leads"),
        path("routes", views.routes, name="routes"),
        path('create/', views.LeadCreateView.as_view(), name='create_lead'),
        path('update/<int:pk>', views.LeadUpdateView.as_view(), name='update_lead'),
        path('read/<int:pk>', views.LeadReadView.as_view(), name='read_lead'),
        path('delete/<int:pk>', views.LeadDeleteView.as_view(), name='delete_lead'),
        re_path(r'^routes/details/(?P<location_from>[\w\-\s\(\)]+)/(?P<location_to>[\w\-\s\(\)]+)/(?P<lead_status>\w+)/$',views.routes_leads_list,name='user_routes_details'),
        re_path(r'^city/details/(?P<city>[\w\-\s]+)/$',views.city_routes_list,name='city_routes_list'),
        re_path(r'^leads/(?P<city>[\w\-\s]+)/$',views.city_leads_list,name='city_leads_list'),
]
