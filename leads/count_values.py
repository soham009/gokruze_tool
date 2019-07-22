from leads import count_functions
from leads.models import Leads

leads = Leads.objects.all()
x = list(set(list(Leads.objects.values_list('LocationFrom', 'LocationTo','LocationFromOther'))))
lead_Status_list = ["Uncontacted","Undecided","Converted","Interested"]
total = [ count_functions.Total_Count_LeadStatus(x) for x in lead_Status_list ]
week = [ count_functions.Weekly_Count_LeadStatus(x) for x in lead_Status_list ]
month = [ count_functions.Monthly_Count_LeadStatus(x) for x in lead_Status_list ]
mumbai = [ count_functions.City_Count(x,"Mumbai") for x in lead_Status_list ]
kochi = [ count_functions.City_Count(x,"Kochi") for x in lead_Status_list ]
pune = [ count_functions.City_Count(x,"Pune") for x in lead_Status_list ]
banglore = [ count_functions.City_Count(x,"Banglore") for x in lead_Status_list ]
hyderabad = [ count_functions.City_Count(x,"Hyderabad") for x in lead_Status_list ]
calcutta = [ count_functions.City_Count(x,"Calcutta") for x in lead_Status_list ]
mumbai_dict = dict(zip(lead_Status_list, mumbai))
kochi_dict = dict(zip(lead_Status_list, kochi))
pune_dict = dict(zip(lead_Status_list, pune))
banglore_dict = dict(zip(lead_Status_list, banglore))
calcutta_dict = dict(zip(lead_Status_list, calcutta))
hyderabad_dict = dict(zip(lead_Status_list, hyderabad))
total_dict = dict(zip(lead_Status_list, total))
week_dict = dict(zip(lead_Status_list, week))
month_dict = dict(zip(lead_Status_list, month))
total_city_collect = { 'mumbai_all' : count_functions.Total_City_Count('Mumbai'), 'kochi_all' : count_functions.Total_City_Count('Kochi'), 'pune_all' : count_functions.Total_City_Count('Pune'), 'hyderabad_all' : count_functions.Total_City_Count('Hyderabad'), 'banglore_all' : count_functions.Total_City_Count('Banglore'), 'calcutta_all' : count_functions.Total_City_Count('Calcutta')}
total_collect = { 'all': count_functions.Total_Count(), 'week': count_functions.Weekly_Count(), 'month': count_functions.Montly_Count(),}
routes = [ count_functions.Total_Routes_Count(a,lead_status) for a in x for lead_status in lead_Status_list ]
final = [routes[i * 4:(i + 1) * 4] for i in range((len(routes) + 4 - 1) // 4 )]
routes = [ count_functions.Total_Routes_Count(a,lead_status) for a in x for lead_status in lead_Status_list ]
final = [routes[i * 4:(i + 1) * 4] for i in range((len(routes) + 4 - 1) // 4 )]
routes_dict = dict(zip(x,final))