from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


class Province(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class ImmigrationStream(models.Model):
    name = models.CharField(max_length=500)
    stream_description = models.CharField(max_length=2000)
    province = models.ForeignKey(Province)

    def __str__(self):
        return self.name


class ImmigrationProgram(models.Model):
    name = models.CharField(max_length=200)
    program_description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ImmigrationSubProgram(models.Model):
    name = models.CharField(max_length=200)
    sub_program_description = models.CharField(max_length=2000)
    program = models.ForeignKey(ImmigrationProgram)

    def __str__(self):
        return self.name


class UserStatisticFederalPhase(models.Model):
    user = models.ForeignKey(User)
    inland = models.BooleanField(default=False)
    immigration_program = models.ForeignKey(ImmigrationProgram, null=False)
    immigration_sub_program = models.ForeignKey(ImmigrationSubProgram, null=True)
    immigration_stream = models.ForeignKey(ImmigrationStream, null=True)
    cio_received_date = models.DateField(null=True)
    cio_processing_fee_date = models.DateField(null=True)
    cio_file_number = models.DateField(null=True)
    embassy = models.CharField(max_length=80, null=True)
    ecas_recieved = models.DateField(null=True)
    ecas_in_process = models.DateField(null=True)
    ecas_additional_documents_request1 = models.DateField(null=True)
    ecas_medical_forms = models.DateField(null=True)
    ecas_medical_exam_passed = models.DateField(null=True)
    ecas_medical_results_received = models.DateField(null=True)
    ecas_additional_documents_request2 = models.DateField(null=True)
    povl_date = models.DateField(null=True)


class UserStatisticProvincialPhase(models.Model):
    user = models.ForeignKey(User)
    province = models.ForeignKey(Province)
    immigration_stream = models.ForeignKey(ImmigrationStream)
    interview_location = models.CharField(max_length=200, null=True)
    interview_date = models.DateField(null=True)
    invitation_to_apply_date = models.DateField(null=True)
    prov_file_date = models.DateField(null=True)
    prov_request_additional_docs_date = models.DateField(null=True)
    prov_nomination_date = models.DateField(null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    country = CountryField()