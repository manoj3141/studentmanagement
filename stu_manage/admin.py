from django.contrib import admin

from stu_manage.models import Student

# Register your models here.
@admin.register(Student)

class Studentad(admin.ModelAdmin):
    list_display=['id','fname','lname','email','subject']