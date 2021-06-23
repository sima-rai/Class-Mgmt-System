from django.shortcuts import redirect, render
from django.views.generic import View, TemplateView, CreateView, FormView
from .forms import *
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout



# Create your views here.

class TeacherRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Teacher.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("cmsapp:teacherlogin")
        
        return super().dispatch(request, *args, **kwargs)


class StudentRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Student.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("cmsapp:studentlogin")
        
        return super().dispatch(request, *args, **kwargs)


def IndexView(request):
    return render(request, 'index.html')

class TeacherHomeView(TeacherRequiredMixin, TemplateView):
    template_name = "teacher/teacherhome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher_obj = Teacher.objects.get(user=self.request.user)
        print(teacher_obj)
        school = teacher_obj.school
        notices = Notice.objects.filter(teacher=teacher_obj).order_by("-id")
        print(notices)
        context['school']=school
        context['notices']=notices
        # context['teacher']=notices

        return context




class TeacherSignupView(CreateView):
    template_name = "teacher/teachersignup.html"
    form_class = TeacherSignupForm
    success_url = reverse_lazy("cmsapp:teachersignup")

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
        return redirect("cmsapp:teacherlogin")

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


class TeacherCreateNotice(CreateView):
    template_name = "teacher/teachernoticecreate.html"
    form_class = TeacherNoticeCreateForm
    success_url = reverse_lazy("cmsapp:teacherhome")

    def form_valid(self, form):
        user = self.request.user.id
        print(user, "fff")
        teacher = Teacher.objects.get(user=self.request.user.id)
        form.instance.teacher = teacher
        return super().form_valid(form)







class StudentSignupView(CreateView):
    template_name = "student/studentsignup.html"
    form_class = StudentSignupForm
    success_url = reverse_lazy("cmsapp:studentsignup")

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        email = form.cleaned_data["email"]
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        return super().form_valid(form)


class StudentLoginView(FormView):
    template_name = "student/studentlogin.html"
    form_class = StudentLoginForm
    success_url = reverse_lazy("cmsapp:studenthome")

    def form_valid(self, form):
        uname = form.cleaned_data["username"]
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Student.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form":self.form_class, "error":"Invalid Credentials"})
        
        return super().form_valid(form)

class StudentHomeView(StudentRequiredMixin, TemplateView):
    template_name = "student/studenthome.html"


class StudentLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("cmsapp:studentsignup")









