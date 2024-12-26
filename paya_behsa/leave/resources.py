from import_export import resources
from .models import Driver

class DriverResource(resources.ModelResource):
    class Meta:
        model = Driver