from django.db import migrations

def update_reference_organization(apps, schema_editor):
    Reference = apps.get_model('portfolio', 'Reference')
    # Update the organization name for the specific reference
    Reference.objects.filter(name='[REFERENCE_NAME]').update(organization='[NEW_ORGANIZATION_NAME]')

class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '[LATEST_MIGRATION]'),
    ]

    operations = [
        migrations.RunPython(update_reference_organization),
    ]
