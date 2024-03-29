from django.core.management.base import BaseCommand, CommandError
from leads.models import Leads
from datetime import date
import datetime
import requests

class Command(BaseCommand):
    help = 'Fetchs Data at 1:00 PM'

    def handle(self, *args, **options):
        n=1
        while(n!=7):
            yesterday = datetime.date.today()-datetime.timedelta(days=n)
            qs = Leads.objects.all()
            url = 'https://www.gokruze.com/other/survey_records/kz_usr/123456/' + str(yesterday.strftime('%Y.%m.%d')).replace('.','')
            req = requests.get(url)
            response = req.json()
            if(response['msg']=='Record Found'):
                for title in response['data']:
                    Leads.objects.create(City=title['City'], Name=title['Name'], Gender=title['Gender'], EmailId=title['EmailId'], ContactNo=title['ContactNo'],LocationFrom=title['LocationFrom'],LocationTo=title['LocationTo'], LoginTime=title['LoginTime'],LogoutTime=title['LogoutTime'],CompanyName=title['CompanyName'],TravalToWork=title['TravalToWork'], MonthlySpend=title['MonthlySpend'],HearAboutUs=title['HearAboutUs'],SubmittedOnDate=datetime.datetime.strptime(title['SubmittedOn'] , '%d-%b-%Y %I:%M %p'),LocationFromOther=title['LocationFromOther'], SubmittedOn=title['SubmittedOn'] )
            n = n+1
        self.stdout.write(self.style.SUCCESS('Successfully Fetched Data'))
