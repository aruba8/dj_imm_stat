from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


class Stream(models.Model):
    SKILLED_IMMIGRANTS = 'EE'
    QUEBEC_SKILLED_IMMIGRANTS = 'QE'
    STARTUP = 'SU'
    FAMILY_SPONSORSHIP = 'FS'
    IMMIGRANT_INVESTOR = 'II'
    SELF_EMPLOYED = 'SE'
    PROVINCIAL_NOMINEE = 'PN'
    CAREGIVER = 'CR'
    REFUGEE = 'RF'

    STREAM_CHOICES = (
        (SKILLED_IMMIGRANTS, 'Skilled immigrants (Express Entry)'),
        (QUEBEC_SKILLED_IMMIGRANTS, 'Quebec-selected skilled workers (or investor or entrepreneur program)'),
        (STARTUP, 'Start-up visa'),
        (IMMIGRANT_INVESTOR, 'Immigrant Investor Venture Capital Pilot Program'),
        (SELF_EMPLOYED, 'Self-employed Persons Program'),
        (FAMILY_SPONSORSHIP, 'Family sponsorship'),
        (PROVINCIAL_NOMINEE, 'Provincial nominees'),
        (CAREGIVER, 'Caregivers'),
        (REFUGEE, 'Refugees')
    )

    stream = models.CharField(max_length=2, choices=STREAM_CHOICES, default=SKILLED_IMMIGRANTS)

    def get_by_choice(self, choice):
        return dict(v for v in self.STREAM_CHOICES)[choice]


class ProvincialStream(models.Model):
    MB_GENERAL_STREAM = 'MBG'
    MB_STRATEGIC_STREAM = 'MBS'

    STREAM_CHOICES =(
        (MB_GENERAL_STREAM, 'Manitoba MPNP general stream'),
        (MB_STRATEGIC_STREAM, 'Manitoba MPNP strategic stream')
    )

    stream = models.CharField(max_length=3, choices=STREAM_CHOICES, default=MB_GENERAL_STREAM)

    def get_by_choice(self, choice):
        return dict(v for v in self.STREAM_CHOICES)[choice]


class UserStatistic(models.Model):
    user_id = models.IntegerField(null=True)
    username = models.CharField(max_length=80)
    stream = models.CharField(max_length=2, null=True, choices=Stream.STREAM_CHOICES)
    provincial_stream = models.CharField(max_length=80, null=True, choices=ProvincialStream.STREAM_CHOICES)
    from_country = CountryField()
    interview_location = models.CharField(max_length=200, null=True)
    interview_date = models.DateField(null=True)
    invitation_to_apply_date = models.DateField(null=True)
    mpnp_file_date = models.DateField(null=True)
    mpnp_request_additional_docs_date = models.DateField(null=True)
    mpnp_nomination_date = models.DateField(null=True)
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


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    country = CountryField()