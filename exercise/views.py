from django.shortcuts import render, redirect
from .models import Patient
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login as auth_login
from .models import Feedback
from .models import ConsultationRequest
from .models import ConsultationRequest, Feedback, Patient
import os
from dotenv import load_dotenv
from django.http import JsonResponse
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chatbot_response(request):
    if request.method == "POST":
        user_message = request.POST.get("message")

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": user_message}
                ]
            )
            reply = response.choices[0].message.content.strip()
            return JsonResponse({"reply": reply})
        except Exception as e:
            return JsonResponse({"reply": f"Something went wrong: {str(e)}"})






def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            patient = Patient.objects.get(username=username, password=password)
            request.session['patient_id'] = patient.id
            request.session['patient_name'] = patient.full_name
            request.session['patient_email'] = patient.email  # 🔹 Add this line
            return redirect('home')
        except Patient.DoesNotExist:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        data = request.POST
        file = request.FILES.get('report')
        username = data.get('username')

        # Check if username already exists
        if Patient.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose another.")
            return render(request, 'register.html')

        # Proceed to create the new patient
        Patient.objects.create(
            full_name = data.get('fullname'),
            username = username,
            dob = data.get('dob'),
            gender = data.get('gender'),
            contact = data.get('contact'),
            email = data.get('email'),
            password = data.get('password'),
            address = data.get('address'),
            city = data.get('city'),
            state = data.get('state'),
            zip = data.get('zip'),
            country = data.get('country'),
            conditions = data.get('conditions'),
            reason = data.get('reason'),
            previous_sessions = data.get('previous_sessions'),
            appointment = data.get('appointment'),
            emergency_name = data.get('emergency_name'),
            emergency_relation = data.get('emergency_relation'),
            emergency_phone = data.get('emergency_phone'),
            insurance = data.get('insurance'),
            policy = data.get('policy'),
            report = file,
            newsletter = 'newsletter' in data
        )
        return redirect('login')  # redirect after successful registration

    return render(request, 'register.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def logout_view(request):
    request.session.flush()
    messages.success(request, "You have been logged out.")
    return redirect('login') 

def profile(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('login')

    patient = Patient.objects.get(id=patient_id)

    if request.method == 'POST':
        data = request.POST
        patient.full_name = data.get('fullname')
        patient.contact = data.get('contact')
        patient.email = data.get('email')
        patient.address = data.get('address')
        patient.city = data.get('city')
        patient.state = data.get('state')
        patient.zip = data.get('zip')
        patient.country = data.get('country')
        patient.save()
        messages.success(request, "Profile updated successfully.")
        return redirect('profile')

    return render(request, 'profile.html', {'patient': patient}) 

def is_doctor(user):
    return user.email == 'chakrabortytridisha@gmail.com'

#@login_required
#@user_passes_test(is_doctor)
#@staff_member_required  # Only doctor can access
def appointment_dashboard(request):
    #if request.session.get('patient_email') != 'chakrabortytridisha@gmail.com':
     #   return redirect('home')  # deny access if not doctor

    patients = Patient.objects.all().order_by('-id')

    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        new_status = request.POST.get('status')
        patient = Patient.objects.get(id=patient_id)
        patient.status = new_status
        patient.save()
        messages.success(request, f"Status updated for {patient.full_name}")
        return redirect('appointments')

    return render(request, 'appointment_dashboard.html', {'patients': patients})

def submit_feedback(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('login')

    patient = Patient.objects.get(id=patient_id)

    if request.method == 'POST':
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')

        Feedback.objects.create(
            patient=patient,
            comment=comment,
            rating=rating
        )
        messages.success(request, "Thank you for your feedback!")
        return redirect('home')

    return render(request, 'feedback.html')

def consultation_request(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('login')

    patient = Patient.objects.get(id=patient_id)

    if request.method == 'POST':
        symptoms = request.POST.get('symptoms')
        time = request.POST.get('preferred_time')
        mode = request.POST.get('mode')

        ConsultationRequest.objects.create(
            patient=patient,
            symptoms=symptoms,
            preferred_time=time,
            mode=mode
        )
        messages.success(request, "Your consultation request has been submitted.")
        return redirect('home')

    return render(request, 'consultation_request.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "tridisha" and password == "123456789":
            request.session['admin_logged_in'] = True
            messages.success(request, "Logged in successfully.")
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid credentials.")

    return render(request, 'admin_login.html')

def admin_dashboard(request):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')

    consultation_count = ConsultationRequest.objects.count()
    appointment_count = Patient.objects.exclude(appointment=None).count()
    feedback_count = Feedback.objects.count()

    return render(request, 'admin_dashboard.html', {
        'consultation_count': consultation_count,
        'appointment_count': appointment_count,
        'feedback_count': feedback_count,
    })


def admin_consultation(request):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')

    search_query = request.GET.get('search', '')
    mode_filter = request.GET.get('mode', '')

    consultations = ConsultationRequest.objects.select_related('patient').all()

    if search_query:
        consultations = consultations.filter(patient__full_name__icontains=search_query)

    if mode_filter and mode_filter != 'All':
        consultations = consultations.filter(mode=mode_filter)

    return render(request, 'admin_consultation.html', {
        'consultations': consultations,
        'search_query': search_query,
        'mode_filter': mode_filter
    })

def admin_appointments(request):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')

    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')

    patients = Patient.objects.all()

    if search_query:
        patients = patients.filter(full_name__icontains=search_query)

    if status_filter and status_filter != 'All':
        patients = patients.filter(status=status_filter)

    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        new_status = request.POST.get('status')
        patient = Patient.objects.get(id=patient_id)
        patient.status = new_status
        patient.save()
        messages.success(request, f"Status updated for {patient.full_name}")
        return redirect('admin_appointments')

    return render(request, 'admin_appointments.html', {
        'patients': patients,
        'search_query': search_query,
        'status_filter': status_filter
    })

def admin_feedback(request):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')

    sort_option = request.GET.get('sort', 'latest')

    if sort_option == 'rating_high':
        feedbacks = Feedback.objects.select_related('patient').order_by('-rating')
    elif sort_option == 'rating_low':
        feedbacks = Feedback.objects.select_related('patient').order_by('rating')
    else:
        feedbacks = Feedback.objects.select_related('patient').order_by('-id')  # latest

    return render(request, 'admin_feedback.html', {
        'feedbacks': feedbacks,
        'sort_option': sort_option
    })

def simulated_payment(request):
    if request.method == 'POST':
        # Simulate payment success
        messages.success(request, "Payment successful! You may now submit your consultation request.")
        return redirect('consultation_request')  # ✅ redirect back here
    return render(request, 'simulated_payment.html')

def admin_logout(request):
    request.session.flush()  # Clears the admin session
    messages.success(request, "Admin logged out successfully.")
    return redirect('login')  # Redirect to the original login form
