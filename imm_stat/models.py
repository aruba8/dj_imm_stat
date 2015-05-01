from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


class UserStatistic(models.Model):
    user_id = models.IntegerField(null=True)
    username = models.CharField(max_length=80)
    stream = models.CharField(max_length=80, null=True)
    from_country = CountryField()
    interview_location = models.CharField(max_length=200, null=True)
    interview_date = models.DateTimeField(null=True)
    invitation_to_apply_date = models.DateTimeField(null=True)
    mpnp_file_date = models.DateTimeField(null=True)
    mpnp_request_additional_docs_date = models.DateTimeField(null=True)
    mpnp_nomination_date = models.DateTimeField(null=True)
    cio_received_date = models.DateTimeField(null=True)
    cio_processing_fee_date = models.DateTimeField(null=True)
    cio_file_number = models.DateTimeField(null=True)
    embassy = models.CharField(max_length=80, null=True)
    ecas_recieved = models.DateTimeField(null=True)
    ecas_in_process = models.DateTimeField(null=True)
    ecas_additional_documents_request1 = models.DateTimeField(null=True)
    ecas_medical_forms = models.DateTimeField(null=True)
    ecas_medical_exam_passed = models.DateTimeField(null=True)
    ecas_medical_results_received = models.DateTimeField(null=True)
    ecas_additional_documents_request2 = models.DateTimeField(null=True)
    povl_date = models.DateTimeField(null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    country = CountryField()
