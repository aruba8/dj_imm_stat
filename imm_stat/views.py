from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
from django.template.context import RequestContext
from django.views import generic
from django.contrib.auth import logout
from imm_stat.forms import UserCreateForm, UserProfileForm, UserUpdateForm, FederalStatisticForm, ProvincialStatisticForm

from imm_stat.models import UserStatisticFederalPhase, User, UserStatisticProvincialPhase


class IndexView(generic.ListView):
    template_name = 'imm_stat/index.html'
    context_object_name = 'userdata'

    def get_queryset(self):
        return UserStatisticFederalPhase.objects.all()


@login_required
def profile(request):
    user = User.objects.get(pk=request.user.id)
    return render(request, 'imm_stat/profile.html', {'user': user})

@login_required
def profile_update(request):
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=user.userprofile)
        if user_update_form.is_valid() and profile_form.is_valid():
            user_update_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            print user_update_form.errors, profile_form.errors
    else:
        user_update_form = UserUpdateForm(instance=user)
        profile_form = UserProfileForm(instance=user.userprofile)

    return render(request, 'imm_stat/edit_profile.html',
                  {'user': user, 'user_update_form': user_update_form, 'profile_form': profile_form})


def statistic_view(request, pk):
    federal_statistic = UserStatisticFederalPhase.objects.filter(user_id=pk).first()
    provincial_statistic = UserStatisticProvincialPhase.objects.filter(user_id=pk).first()
    return render(request, 'imm_stat/statistic.html', {'federal_statistic': federal_statistic,
                                                       'provincial_statistic': provincial_statistic})


@login_required
def edit_federal_statistic_view(request):
    user = request.user
    user_stat = UserStatisticFederalPhase.objects.filter(user_id=user.id).first()

    if request.method == 'POST':
        statistic_form = FederalStatisticForm(request.user, request.POST, instance=user_stat)
        if statistic_form.is_valid():
            statistic_form.save()
            return HttpResponseRedirect(reverse('statistic', args=[user.id]))
        else:
            print statistic_form.errors
    else:
        if user_stat:
            statistic_form = FederalStatisticForm(instance=user_stat, current_user=user)
        else:
            statistic_form = FederalStatisticForm(current_user=user)
    return render(request, 'imm_stat/edit_federal_statistic.html', {'statistic_form': statistic_form})


@login_required
def edit_provincial_statistic_view(request):
    user = request.user
    user_stat = UserStatisticProvincialPhase.objects.filter(user_id=user.id).first()

    if request.method == 'POST':
        statistic_form = ProvincialStatisticForm(request.user, request.POST, instance=user_stat)
        if statistic_form.is_valid():
            statistic_form.save()
            return HttpResponseRedirect(reverse('statistic', args=[user.id]))
        else:
            print statistic_form.errors
    else:
        if user_stat:
            statistic_form = ProvincialStatisticForm(instance=user_stat, current_user=user)
        else:
            statistic_form = ProvincialStatisticForm(current_user=user)
    return render(request, 'imm_stat/edit_province_statistic.html', {'statistic_form': statistic_form})


def logout_view(request):
    logout(request)
    
    
def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_ = profile_form.save(commit=False)
            profile_.user = user
            profile_.save()
            user = authenticate(username=user_form.data['username'], password=user_form.data['password1'])
            login(request, user)
            return redirect('/')
        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserCreateForm()
        profile_form = UserProfileForm()

    return render_to_response('registration/register.html',
                              {'form': user_form, 'registered': registered, 'profile_form': profile_form}, context)