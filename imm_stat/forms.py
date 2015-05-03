from django import forms
from django.contrib.auth.models import User
from imm_stat.models import UserStatistic, ProvincialStream
from models import UserProfile, Stream
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('email',)


class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['country'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserProfile
        fields = ('country',)


class UserCreateForm(UserCreationForm):
    email = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat password'

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class StatisticForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StatisticForm, self).__init__(*args, **kwargs)
        self.fields['stream'].widget.attrs['class'] = 'form-control'
        self.fields['provincial_stream'].widget.attrs['class'] = 'form-control'
        self.fields['from_country'].widget.attrs['class'] = 'form-control'
        self.fields['interview_location'].widget.attrs['class'] = 'form-control'
        self.fields['interview_date'].widget.attrs['class'] = 'form-control date'
        self.fields['invitation_to_apply_date'].widget.attrs['class'] = 'form-control date'
        self.fields['mpnp_file_date'].widget.attrs['class'] = 'form-control date'
        self.fields['mpnp_request_additional_docs_date'].widget.attrs['class'] = 'form-control date'
        self.fields['mpnp_nomination_date'].widget.attrs['class'] = 'form-control date'
        self.fields['cio_received_date'].widget.attrs['class'] = 'form-control date'
        self.fields['cio_processing_fee_date'].widget.attrs['class'] = 'form-control date'
        self.fields['cio_file_number'].widget.attrs['class'] = 'form-control date'
        self.fields['embassy'].widget.attrs['class'] = 'form-control'
        self.fields['ecas_recieved'].widget.attrs['class'] = 'form-control date'
        self.fields['ecas_in_process'].widget.attrs['class'] = 'form-control date'
        self.fields['ecas_medical_forms'].widget.attrs['class'] = 'form-control date'
        self.fields['ecas_medical_exam_passed'].widget.attrs['class'] = 'form-control date'
        self.fields['ecas_medical_results_received'].widget.attrs['class'] = 'form-control date'
        self.fields['povl_date'].widget.attrs['class'] = 'form-control date'

    stream = forms.ChoiceField(choices=Stream.STREAM_CHOICES)
    provincial_stream = forms.ChoiceField(choices=ProvincialStream.STREAM_CHOICES)
    # from_country = forms.CharField(required=False)
    interview_location = forms.CharField(required=False)
    interview_date = forms.DateField(required=False)
    invitation_to_apply_date = forms.DateField(required=False)
    mpnp_file_date = forms.DateField(required=False)
    mpnp_request_additional_docs_date = forms.DateField(required=False)
    mpnp_nomination_date = forms.DateField(required=False)
    cio_received_date = forms.DateField(required=False)
    cio_processing_fee_date = forms.DateField(required=False)
    cio_file_number = forms.DateField(required=False)
    embassy = forms.CharField(required=False)
    ecas_recieved = forms.DateField(required=False)
    ecas_in_process = forms.DateField(required=False)
    ecas_additional_documents_request1 = forms.DateField(required=False)
    ecas_medical_forms = forms.DateField(required=False)
    ecas_medical_exam_passed = forms.DateField(required=False)
    ecas_medical_results_received = forms.DateField(required=False)
    ecas_additional_documents_request2 = forms.DateField(required=False)
    povl_date = forms.DateField(required=False)

    class Meta:
        model = UserStatistic
        fields = ('stream', 'provincial_stream', 'from_country', 'interview_location', 'interview_date',
                  'invitation_to_apply_date', 'mpnp_file_date', 'mpnp_request_additional_docs_date',
                  'mpnp_nomination_date', 'cio_received_date', 'cio_processing_fee_date', 'cio_file_number', 'embassy',
                  'ecas_recieved', 'ecas_in_process', 'ecas_medical_forms', 'ecas_medical_exam_passed',
                  'ecas_medical_results_received', 'povl_date', )