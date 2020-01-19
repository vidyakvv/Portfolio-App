from django.db import models
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Educationtable(models.Model):
    degree = models.CharField(max_length=45)
    university = models.CharField(max_length=45)
    specialization = models.CharField(max_length=45)
    termstart = models.TextField(db_column='termStart')  # Field name made lowercase. This field type is a guess.
    termend = models.CharField(db_column='termEnd', max_length=45)  # Field name made lowercase.
    gpa = models.CharField(max_length=4, blank=True, null=True)
    coursework = models.TextField(blank=True, null=True)
    personid = models.IntegerField(db_column='personID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'educationTable'


class Experiencetable(models.Model):
    title = models.CharField(max_length=45)
    employer = models.CharField(max_length=45)
    startmonth = models.CharField(db_column='startMonth', max_length=10)  # Field name made lowercase.
    endmonth = models.CharField(db_column='endMonth', max_length=10)  # Field name made lowercase.
    startyear = models.TextField(db_column='startYear')  # Field name made lowercase. This field type is a guess.
    endyear = models.CharField(db_column='endYear', max_length=45)  # Field name made lowercase.
    content = models.TextField()
    personid = models.IntegerField(db_column='personID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'experienceTable'


class Persontable(models.Model):
    name = models.CharField(unique=True, max_length=20)
    email = models.CharField(unique=True, max_length=45)
    address = models.CharField(max_length=45)
    linkedin = models.CharField(db_column='linkedIn', max_length=45, blank=True, null=True)  # Field name made lowercase.
    github = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'personTable'


class Projecttable(models.Model):
    projectid = models.AutoField(db_column='projectID', primary_key=True)  # Field name made lowercase.
    projectname = models.CharField(db_column='projectName', unique=True, max_length=100)  # Field name made lowercase.
    content = models.TextField()
    technologies = models.CharField(max_length=100)
    termstart = models.CharField(db_column='termStart', max_length=10)  # Field name made lowercase.
    termend = models.CharField(db_column='termEnd', max_length=10)  # Field name made lowercase.
    termstartyear = models.TextField(db_column='termStartYear')  # Field name made lowercase. This field type is a guess.
    termendyear = models.TextField(db_column='termEndYear')  # Field name made lowercase. This field type is a guess.
    personid = models.IntegerField(db_column='personID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'projectTable'


class Skilltable(models.Model):
    name = models.CharField(unique=True, max_length=45)
    scale = models.IntegerField()
    personid = models.PositiveIntegerField(db_column='personID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'skillTable'


