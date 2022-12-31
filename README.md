# STUDYBUDDY

## Querying items

1. All objects
    queryset = ModelNmae.objects.all()

2. Getting a single item
    queryitem = ModelName.objects.get(attribute=value)

3. Filtering objects
    queryset =  ModelName.objects.filter(attribute__startswith=value)
    queryset =  ModelName.objects.filter(attribute__contains=value)
    queryset =  ModelName.objects.filter(attribute__icontains=value)
    queryset =  ModelName.objects.filter(attribute__gt=value)
    queryset =  ModelName.objects.filter(attribute__gte=value)
    queryset =  ModelName.objects.filter(attribute__lt=value)
    queryset =  ModelName.objects.filter(attribute__lte=value)
    queryset =  ModelName.objects.filter(attribute=value)

4. excuding items
    queryset = ModelName.objects.exclude(attribute=value)

5. Multiple Parameters
    queryset = Project.objects.filter(title='first project').order_by('value1', 'value2')

<https://djangostars.com/blog/rest-apis-django-development/>
<https://realpython.com/django-hosting-on-heroku/>
