from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib import messages
# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/pages/index.html"

class ProfileView(View):
    template_name= 'dashboard/pages/users-profile.html'

    def get(self,request):
        return render(request,self.template_name)
    def post(self, request):
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        bio=request.POST.get("bio")
        phone_number=request.POST.get("phone_number")
        email=request.POST.get("email")
        twitter_url=request.POST.get("twitter")
        github_url=request.POST.get("github")
        instagram_url=request.POST.get("instagram")
        facebook_url= request.POST.get("facebook")

        user= request.user
        profile=request.profile
        user.firstname=firstname
        user.lastname=lastname
        user.email=email
        profile.bio=bio
        profile.phone_number=phone_number
        profile.twitter=twitter_url
        profile.instagram=instagram_url
        profile.github=github_url
        profile.facebook=facebook_url

        user.save()
        profile.save()
        messages.success(request, "profile updated successfully")
        return render(self.template_name)

