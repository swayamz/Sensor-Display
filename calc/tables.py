import django_tables2 as tables
from .models import FarmData

class SimpleTable(tables.Table):
    class Meta:
        model = FarmData 
