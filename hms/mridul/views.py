from django.shortcuts import render,redirect
from django.http import HttpResponse as hr
from . import forms
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib import messages
from . import models
from django.shortcuts import get_object_or_404, HttpResponseRedirect, render


def home(request):
    return render(request,'mridul/main_desktop.html')
def admin(request):
    return redirect('/admin/login/?next=/admin/')
def aboutus(request):
    return render(request,'mridul/aboutus.html')


def patient_dashboard(request, user_id):
    search = forms.DoctorSearch(request.POST or None)
    all_appointments = models.Appointment.objects.filter(user_id = user_id)
    user = get_object_or_404(models.Users, user_sr_no=user_id)

    if request.method == 'POST':
        specialisation = request.POST.get('specialisation')

        if specialisation:
            results = models.Doctor.objects.filter(specialization__icontains=specialisation)
            if results.exists():
                return render(request, 'mridul/patient_dash.html', {
                    'form': search, 
                    'results': results, 
                    'user': user
                })
            else:
                messages.error(request, "No doctors found for this specialization. Please try again.")
        else:
            messages.error(request, "Please enter a valid specialization.")
    return render(request, 'mridul/patient_dash.html', {
        'form': search,
        'user': user,
        'all_appointments': all_appointments
    })
def all_bookings(request,user_id):
    all_appointments = models.Appointment.objects.filter(user_id = user_id)
    
    user_instance = get_object_or_404(models.Users, user_sr_no=user_id)
    return  render(request,'mridul/all_bookings.html',
                   {'user_id':user_id , 
                    'all_appointments':all_appointments, 
                    'user':user_instance
                    }
                )

def login(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')
        user_queryset = models.Users.objects.filter(email_id=email_id)

        if user_queryset.exists(): 
            print("User exists.\n")
            user = user_queryset.first()
           
            if password == user.password:
                print("Password is correct.\n")
                if user.role_as_a == 'patient':
                    return HttpResponseRedirect(f'/patient_dashboard/{user.user_sr_no}/')
                elif user.role_as_a == 'doctor':
                    return HttpResponseRedirect(f'/doctor_dashboard/{user.user_sr_no}/')
                elif user.role_as_a == 'receptionist': 
                    return HttpResponseRedirect(f'/receptionist_dashboard/{user.user_sr_no}/')
            else:
                print("Password doesn't match.\n")
                messages.error(request, "Incorrect password. Please try again.")
        else:
            messages.error(request, "No account found with that email ID. Please register.")
            print("User doesn't exist.\n")
    return render(request, 'mridul/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        role = request.POST.get('role') 
        form = forms.RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            user.role_as_a = role 
            user.created_at = timezone.now()
            user.save() 
            print('\n******ohk! form successfully submitted*****\n')
            return HttpResponseRedirect('/')
        else:
            return render(request, 'mridul/index.html', {'form': form, 'active_tab': role}) 
            
    else:
        form = forms.RegisterForm()
    
    return render(request, 'mridul/index.html', {'form': form, 'active_tab': 'Patient'})

def doctor_dashboard(request,user_id):
    user = get_object_or_404(models.Users, user_sr_no=user_id) 
    doctor_data = models.Doctor.objects.filter(email = user.email_id)
    return render(request,'mridul/doctor_dash.html',{'doctor_data':doctor_data,'user':user})
def receptionist_dashboard(request,user_id):
    user = get_object_or_404(models.Users, user_sr_no=user_id)  
    all_appointments = models.Appointment.objects.all()
    # print(all_appointments)
   
    all_appointments = models.Appointment.objects.all()
    
    return render(request,'mridul/recept_dash.html',{'user_id':user_id,'user':user,'all_appointments':all_appointments})
def add_patient(request,user_id):
    user = get_object_or_404(models.Users, user_sr_no=user_id) 
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        address = request.POST.get('address')
        blood_group = request.POST.get('blood_group')
        emergency_contact_name = request.POST.get('emergency_contact_name')
        emergency_contact_number = request.POST.get('emergency_contact_number')
        
        add_patient = models.Patient(
            first_name = first_name,
            last_name = last_name,
            gender= gender,
            date_of_birth = date_of_birth,
            phone_no=phone_no,
            email=email,
            address=address,
            blood_group = blood_group,
            emergency_contact_name = emergency_contact_name,
            emergency_contact_number = emergency_contact_number
        )
        add_patient.save()
        print('Done sucessfully @@@@@@@')
        # appointment = models.Appointment.objects.filter()
        # patient = models.Patient.objects.filter(phone_no = )
        return HttpResponseRedirect(f'/receptionist_dashboard/{user_id}')
    return render(request,'mridul/add_patient.html',{'user':user})


def alldoctor(request,user_id):
    alldoctor = models.Doctor.objects.all()

    if not alldoctor.exists():  
        messages.error(request, "No doctors available at the moment.")
    
    return render(request,'mridul/alldoctor.html', {'alldoctor': alldoctor,'user_id':user_id})


def book_appointment(request, user_id):
    alldoctor = models.Doctor.objects.all() 
    
    if request.method == 'POST':
       
        doctor_id = request.POST.get('doctor') 
        user_instance = get_object_or_404(models.Users, user_sr_no=user_id)  

        if not alldoctor.filter(doctor_id=doctor_id).exists():
            return render(request, 'mridul/appointment_form.html', {'doctors': alldoctor, 'user_id': user_id, 'error': 'No Doctor matches the given query.'})
        doctor_instance = get_object_or_404(models.Doctor, doctor_id=doctor_id) 
        
        appointment = models.Appointment(
            doctor_id=doctor_instance,
            user_id=user_instance,    
            appointment_date=request.POST.get('appointment_date'),
            appointment_time=request.POST.get('appointment_time'),
            reason=request.POST.get('reason'),
            status='Waiting to be Scheduled', 
            created_at=timezone.now(),  
            updated_at=timezone.now()
        )
        appointment.save()

        print("Appointment done successfully")
        search = forms.DoctorSearch(request.POST or None)
        all_appointments = models.Appointment.objects.filter(user_id = user_id)
        return render(request,'mridul/patient_dash.html',{'user': user_instance ,'all_appointments' :all_appointments,'form':search})

    return render(request, 'mridul/appointment_form.html', {'doctors': alldoctor, 'user': user_instance,'form':search})


def update_appointment_status(request, app_id):
    appointment = get_object_or_404(models.Appointment, appointment_id=app_id)
    status = appointment.status
    user_id = appointment.user_id.user_sr_no
    if request.method == 'POST':
        new_status=None
        if 'confirm' in request.POST:
            new_status = 'Scheduled'
        elif 'cancel' in request.POST:
            new_status = 'Cancelled' 
        appointment.status = new_status
        appointment.updated_at = timezone.now()
        appointment.save()
        print("updated succesfully")
    return HttpResponseRedirect(f'/show_appointments/{user_id}/{status}/') 

def show_appointments(request,user_id,status):
    all_appointments = models.Appointment.objects.filter(status=status)
    user = get_object_or_404(models.Users, user_sr_no=user_id)
    if user.role_as_a == 'doctor':
        doctor = get_object_or_404(models.Doctor, email=user.email_id)
        all_appointments = models.Appointment.objects.filter(status=status, doctor_id = doctor.doctor_id)
    dict = {
        'user': user,
        'all_appointments':all_appointments
    }
    return render(request,'mridul/show_appointments.html',dict)

# def patient_prescriptions(request,app_id):
#     appointment = get_object_or_404(models.Appointment, appointment_id = app_id)  
#     if request.method == 'POST':
#         phone_no = request.POST.get('phone_no')
#         patient = models.Patient.objects.filter(phone_no=phone_no)
#         if patient.exists():
#             return render(request,'mridul/patient_prescriptions.html',{'appointment':appointment,'patient':patient})
#         else:
#             messages.error(request,'Patient not Found !\n Please add Patient First !')
#             return render(request,'mridul/patient_prescriptions.html',{'appointment':appointment})
        
#     return render(request,'mridul/patient_prescriptions.html',{'appointment':appointment})

def patient_prescriptions(request, app_id,user_id):
    appointment = get_object_or_404(models.Appointment, appointment_id=app_id)
    user= get_object_or_404(models.Users,user_sr_no = user_id)
    if request.method == 'POST':
        if 'phone_no' in request.POST:  
            phone_no = request.POST.get('phone_no')
            patient = models.Patient.objects.filter(phone_no=phone_no).first()
            if patient:
                return render(request,'mridul/patient_prescriptions.html',{'appointment':appointment,'patient':patient,'user':user})
            else:
                messages.error(request, "Patient not found! Please add the patient first.")
        
        elif 'patient_id' in request.POST:  # Full prescription form submitted
            # Retrieve data from form
            patient_id = request.POST.get('patient_id')
            patient = models.Patient.objects.filter(patient_id=patient_id)
            return HttpResponseRedirect(f'/receptionist_dashboard/{user_id}')  # Replace with the actual URL for redirection

    # GET Request: Load patient data if a patient ID is found in the URL params
    patient_id = request.GET.get('patient_id')
    patient = models.Patient.objects.filter(patient_id=patient_id).first() if patient_id else None

    return render(request, 'mridul/patient_prescriptions.html', {
        'appointment': appointment,
        'patient': patient,
        'user':user,
    })



























# def update_appointment(request, appointment_id):
#     appointment = get_object_or_404(models.Appointment, id=appointment_id)

#     if request.method == 'POST':
#         appointment_date = request.POST.get('appointment_date')
#         appointment_time = request.POST.get('appointment_time')

#         appointment.appointment_date = appointment_date
#         appointment.appointment_time = appointment_time
#         appointment.save()

#         messages.success(request, "Appointment updated successfully.")
#         return redirect('patient_dashboard', user_id=appointment.user_id)

#     # return redirect('settings', appointment_id=appointment.id)

# def cancel_appointment(request, appointment_id):
#     appointment = get_object_or_404(models.Appointment, id=appointment_id)

#     if appointment.status == "Waiting to be Scheduled":
#         appointment.delete()
#         messages.success(request, "Appointment canceled successfully.")
#     else:
#         messages.error(request, "You cannot cancel this appointment.")

#     return redirect('patient_dashboard', user_id=appointment.user_id.user_sr_no)
 


'''
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patient Dashboard</title>
    <!-- <link rel="stylesheet" href="{% static 'css/patient_dash.css' %}"> -->
    <!-- <link rel="stylesheet" href="{% static 'css/alldoctor.css' %}"> -->
    <link rel="stylesheet" href="{% static 'css/add_patient.css' %}"
    
</head>
<body>
    <aside class="sidebar">
        <div class="profile">
            <h2>{{user.first_name}} {{user.last_name}}</h2>
            <p>{{user.email_id}}</p>
            <button class="logout-btn">Log out</button>
        </div>
        <nav>
            <ul>
                <li><a href = "{% url 'receptionist_dashboard' user.user_sr_no %}">Back to Dashboard</a></li>
            </ul>
        </nav>
    </aside>
    <main class="main-content">
        <div class="form-container">
            <h1>Patient Registration</h1>
            <form action="{% url 'receptionist_dashboard' user.user_sr_no %}" method="POST">
                {% csrf_token %}
                <div class="form-group">
                    <label for="first_name">First Name</label>
                    <input type="text" id="first_name" name="first_name" required>
                </div>
                <div class="form-group">
                    <label for="last_name">Last Name</label>
                    <input type="text" id="last_name" name="last_name" required>
                </div>
                <div class="form-group">
                    <label for="gender">Gender</label>
                    <select id="gender" name="gender" required>
                        <option value="">Select</option>
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                        <option value="Other">Other</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="date_of_birth">Date of Birth</label>
                    <input type="date" id="date_of_birth" name="date_of_birth" required>
                </div>
                <div class="form-group">
                    <label for="phone_no">Phone Number</label>
                    <input type="text" id="phone_no" name="phone_no" maxlength="10" required>
                </div>
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email">
                </div>
                <div class="form-group">
                    <label for="address">Address</label>
                    <input type="text" id="address" name="address">
                </div>
                <div class="form-group">
                    <label for="blood_group">Blood Group</label>
                    <select id="blood_group" name="blood_group">
                        <option value="">Select</option>
                        <option value="A+">A+</option>
                        <option value="A-">A-</option>
                        <option value="B+">B+</option>
                        <option value="B-">B-</option>
                        <option value="AB+">AB+</option>
                        <option value="AB-">AB-</option>
                        <option value="O+">O+</option>
                        <option value="O-">O-</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="emergency_contact_name">Emergency Contact Name</label>
                    <input type="text" id="emergency_contact_name" name="emergency_contact_name">
                </div>
                <div class="form-group">
                    <label for="emergency_contact_number">Emergency Contact Number</label>
                    <input type="text" id="emergency_contact_number" name="emergency_contact_number" maxlength="10">
                </div>
                <button type="submit" class="submit-btn">Register</button>
            </form>
        </div>
        
    </main>
</body>
</html>
'''