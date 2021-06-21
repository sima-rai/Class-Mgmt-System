from django.shortcuts import redirect, render
from django.views.generic import View, TemplateView, CreateView, FormView
from .forms import *
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout



# Create your views here.



def IndexView(request):
    return render(request, 'index.html')

class TeacherHomeView(TemplateView):
    template_name = "teacher/teacherhome.html"


class TeacherSignupView(CreateView):
    template_name = "teacher/teachersignup.html"
    form_class = TeacherSignupForm
    success_url = reverse_lazy("cmsapp:teacherhome")

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        email = form.cleaned_data["email"]
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        return super().form_valid(form)


class TeacherLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("cmsapp:teachersignup")

class TeacherLoginView(FormView):
    template_name = "teacher/teacherlogin.html"
    form_class = TeacherLoginForm
    success_url = reverse_lazy("cmsapp:teacherhome")

    def form_valid(self, form):
        uname = form.cleaned_data["username"]
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Teacher.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form":self.form_class, "error":"Invalid Credentials"})
        
        return super().form_valid(form)






