from django.contrib import admin
from .models import Educationtable
from .models import Experiencetable
from .models import Persontable
from .models import Projecttable
from .models import Skilltable

# Register your models here.
admin.site.register(Educationtable)
admin.site.register(Experiencetable)
admin.site.register(Persontable)
admin.site.register(Projecttable)
admin.site.register(Skilltable)


