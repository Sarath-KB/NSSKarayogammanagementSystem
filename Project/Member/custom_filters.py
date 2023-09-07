from django import template
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def add_month(date, months):
   new_date=date+timedelta(days=months*30)
   return new_date