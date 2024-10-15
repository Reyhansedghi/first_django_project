
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, VerifyCodeForm,LoginForm,UserProfileForm
from django.views import View
import random
from extensions.utils import send_otp
from .models import User, OtpCode
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
class AuthView(View):
    login_form_class=LoginForm
    register_form_class=UserRegistrationForm
    verify_form_class=VerifyCodeForm
    template_name = "accounts/login.html"

    def get(self, request):
        if "user_registration_info" in request.session:
            form=self.verify_form_class
            
            status="verify"
            return render(request, self.template_name, {"form": form,"status":status,"registerform":self.register_form_class})
        else:
            status="login"
            form=self.login_form_class
            return render(request, self.template_name, {"form": form,"status":status,"registerform":self.register_form_class})
   
    def post(self, request):
        if 'register' in request.POST:
            return self.handle_registration(request)
        elif 'login' in request.POST:
            return self.handle_login(request)
        elif 'verify' in request.POST and "user_registration_info" in request.session:
            return self.handle_verification(request)
        return self.get(request)
        
    def handle_registration(self, request):
        form = self.register_form_class(request.POST)
        if form.is_valid():
            code = random.randint(1000, 9999)
            cd = form.cleaned_data
            phone_number = cd["phone_number"]
            send_otp(code, phone_number)
            OtpCode.objects.create(phone_number=phone_number, code=code)
            request.session["user_registration_info"] = {
                "phone_number": phone_number,
                "password": cd["password2"],}
            return redirect('accounts:login')
        
        return render(request, self.template_name, {"registerform": form,"form":form,"status":'register',})
    
    def handle_login(self, request):
        form = self.login_form_class(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            password = form.cleaned_data["password"]
            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                return redirect("blog:post_list")
        return render(request, self.template_name, {"form": form,"registerform": self.register_form_class,"status":'login'})
    
    def handle_verification(self,request):
            user_session = request.session["user_registration_info"]
            code_instance = OtpCode.objects.get(phone_number=user_session["phone_number"])
            if not code_instance:
                    return render(request,self.template_name,{"error":"invalid session."})
            form = self.verify_form_class(request.POST)
            if form.is_valid():
                code = form.cleaned_data["code"]
                if code == code_instance.code:
                    
                    user=User(phone_number=user_session["phone_number"],)
                    user.set_password(user_session["password"])
                    user.save()
                    login(request, user)
                    code_instance.delete()
                    del request.session["user_registration_info"]
                    return redirect("blog:post_list")
            return render(request, self.template_name, {"form": form,"registerform": self.register_form_class,"status":'verify'})


@login_required
def profile(request):
    if request.method == 'POST':
        
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)

        if profile_form.is_valid():
            cd = profile_form.cleaned_data
            userprofile=request.user.userprofile
            userprofile.status=cd['status']
            userprofile.companytype=cd['companytype']
            userprofile.first_name=cd['first_name']
            userprofile.last_name=cd['last_name']
            userprofile.company_name=cd['company_name']
            userprofile.city=cd['city']
            userprofile.social_media=cd['social_media']
            userprofile.save()
         #hame fielda byd poor she
    else:
        
        profile_form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'accounts/profile.html', {'profile_form': profile_form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("blog:post_list")
    

