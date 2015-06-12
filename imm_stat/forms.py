from django import forms
from django.contrib.auth.models import User
from imm_stat.models import UserStatisticFederalPhase, UserStatisticProvincialPhase, ImmigrationProgram, ImmigrationSubProgram
from models import UserProfile, ImmigrationStream, Province
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


class FederalStatisticForm(forms.ModelForm):

    def __init__(self, current_user, *args, **kwargs):
        self.current_user = current_user
        super(FederalStatisticForm, self).__init__(*args, **kwargs)
        self.fields['inland'].widget.attrs['class'] = 'checkbox'
        self.fields['immigration_stream'].widget.attrs['class'] = 'form-control date'
        self.fields['immigration_sub_program'].widget.attrs['class'] = 'form-control date'
        self.fields['immigration_program'].widget.attrs['class'] = 'form-control date'
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

    inland = forms.BooleanField(required=False)
    immigration_program = forms.ModelChoiceField(queryset=ImmigrationProgram.objects.all())
    immigration_sub_program = forms.ModelChoiceField(queryset=ImmigrationSubProgram.objects.all())
    immigration_stream = forms.ModelChoiceField(queryset=ImmigrationStream.objects.all())
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

    def save(self, commit=True):
        data = UserStatisticFederalPhase.objects.filter(user=self.current_user).first()
        if data is None:
            data = UserStatisticFederalPhase()
        data.user_id = self.current_user.id
        data.inland = self.cleaned_data['inland']
        data.immigration_program = self.cleaned_data['immigration_program']
        data.immigration_sub_program = self.cleaned_data['immigration_sub_program']
        data.immigration_stream = self.cleaned_data['immigration_stream']
        data.cio_received_date = self.cleaned_data['cio_received_date']
        data.cio_processing_fee_date = self.cleaned_data['cio_processing_fee_date']
        data.cio_file_number = self.cleaned_data['cio_file_number']
        data.embassy = self.cleaned_data['embassy']
        data.ecas_recieved = self.cleaned_data['ecas_recieved']
        data.ecas_in_process = self.cleaned_data['ecas_in_process']
        data.ecas_additional_documents_request1 = self.cleaned_data['ecas_additional_documents_request1']
        data.ecas_medical_forms = self.cleaned_data['ecas_medical_forms']
        data.ecas_medical_exam_passed = self.cleaned_data['ecas_medical_exam_passed']
        data.ecas_medical_results_received = self.cleaned_data['ecas_medical_results_received']
        data.ecas_additional_documents_request2 = self.cleaned_data['ecas_additional_documents_request2']
        data.povl_date = self.cleaned_data['povl_date']
        data.save()
        return data

    class Meta:
        model = UserStatisticFederalPhase
        fields = ('immigration_program', 'immigration_stream', 'immigration_sub_program',
                  'cio_received_date', 'cio_processing_fee_date', 'cio_file_number', 'embassy',
                  'ecas_recieved', 'ecas_in_process', 'ecas_medical_forms', 'ecas_medical_exam_passed',
                  'ecas_medical_results_received', 'povl_date', )


class ProvincialStatisticForm(forms.ModelForm):
    def __init__(self, current_user, *args, **kwargs):
        self.current_user = current_user
        super(ProvincialStatisticForm, self).__init__(*args, **kwargs)
        self.fields['province'].widget.attrs['class'] = 'form-control date'
        self.fields['immigration_stream'].widget.attrs['class'] = 'form-control date'
        self.fields['interview_location'].widget.attrs['class'] = 'form-control date'
        self.fields['interview_date'].widget.attrs['class'] = 'form-control date'
        self.fields['invitation_to_apply_date'].widget.attrs['class'] = 'form-control date'
        self.fields['prov_file_date'].widget.attrs['class'] = 'form-control date'
        self.fields['prov_request_additional_docs_date'].widget.attrs['class'] = 'form-control'
        self.fields['prov_nomination_date'].widget.attrs['class'] = 'form-control date'

    province = forms.ModelChoiceField(queryset=Province.objects.all())
    immigration_stream = forms.ModelChoiceField(queryset=ImmigrationStream.objects.all())
    interview_location = forms.CharField(required=False)
    interview_date = forms.DateField(required=False)
    invitation_to_apply_date = forms.DateField(required=False)
    prov_file_date = forms.DateField(required=False)
    prov_request_additional_docs_date = forms.DateField(required=False)
    prov_nomination_date = forms.DateField(required=False)

    def save(self, commit=True):
        data = UserStatisticProvincialPhase.objects.filter(user=self.current_user).first()
        if data is None:
            data = UserStatisticProvincialPhase()
        data.user_id = self.current_user.id
        data.province = self.cleaned_data['province']
        data.immigration_stream = self.cleaned_data['immigration_stream']
        data.interview_location = self.cleaned_data['interview_location']
        data.interview_date = self.cleaned_data['interview_date']
        data.invitation_to_apply_date = self.cleaned_data['invitation_to_apply_date']
        data.prov_file_date = self.cleaned_data['prov_file_date']
        data.prov_request_additional_docs_date = self.cleaned_data['prov_request_additional_docs_date']
        data.prov_nomination_date = self.cleaned_data['prov_nomination_date']
        data.save()
        return data

    class Meta:
        model = UserStatisticFederalPhase
        fields = ('province', 'immigration_stream',
                  'interview_location', 'interview_date', 'invitation_to_apply_date', 'prov_file_date',
                  'prov_request_additional_docs_date', 'prov_nomination_date', )

