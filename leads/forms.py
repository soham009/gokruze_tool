from django import forms
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm
from .models import Leads


class LeadForm(BSModalForm):

    class Meta:
        model = Leads
        exclude = ['Created_at']
        fields = ['Lead_Status','Remark']

