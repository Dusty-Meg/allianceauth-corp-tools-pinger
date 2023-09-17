# Generated by Aaron on 2022-01-03

from django.db import migrations


def add_ping_types(apps, schema_editor):
    PingType = apps.get_model('pinger', 'PingType')

    # StructureUnderAttack
    PingType.objects.create(name="Wars: War Declared",
                            class_tag="WarDeclared")


class Migration(migrations.Migration):

    dependencies = [
        ('pinger', '0015_add_more_types'),
    ]

    operations = [
        migrations.RunPython(add_ping_types)
    ]
