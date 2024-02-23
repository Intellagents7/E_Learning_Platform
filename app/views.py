from django.shortcuts import render, redirect
from app.models import Student, Course, Assignment
from .forms import StudentForm, AssignmentForm

def index(request):
    return render(request, 'index.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect to dashboard or any other page after successful login
            return redirect('dashboard')
        else:
            # Return an error message indicating invalid credentials
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        # Render the login form for GET requests
        return render(request, 'login.html')


def dashboard(request):
    # Assuming the user is authenticated and logged in
    if request.method == 'GET':
        # Retrieve data to display on the dashboard
        students = Student.objects.all()
        courses = Course.objects.all()
        assignments = Assignment.objects.all()
        context = {
            'students': students,
            'courses': courses,
            'assignments': assignments
        }
        return render(request, 'dashboard.html', context)
    elif request.method == 'POST':
        # Handle form submissions on the dashboard
        if 'student_form' in request.POST:
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        elif 'assignment_form' in request.POST:
            form = AssignmentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
    else:
        # Render error page for unsupported request methods
        return render(request, 'error.html', {'message': 'Unsupported request method'})
