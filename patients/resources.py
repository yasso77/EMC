
from import_export import resources, fields
from import_export import resources
from .models import Patient

class PatientsResources(resources.ModelResource):
    #id = fields.Field(attribute='id', column_name='id')  # Explicitly include the 'id' field

    class Meta:
        model = Patient
        fields = ['Name','mobile','Age','Case','City','Reserved By','Arrived On	Remarks']
        import_id_fields = ["mobile"]
        skip_unchanged = True
        use_bulk = False