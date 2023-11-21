import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from .models import Region, District


def add_regions_and_districts():
    with open('regions.json', encoding='utf-8') as file:
        data = json.load(file)
    for i in range(len(data['regions'])):
        region = data['regions'][i]['name']
        Region.objects.create(name=region)
        for i1 in range(len(data['districts'])):
            district = data['districts'][i1]['name']
            if data['regions'][i]['id'] == data['districts'][i1]['region_id']:
                region_id = Region.objects.get(name=region).id
                District.objects.create(name=district, region_id=region_id)