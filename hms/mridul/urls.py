from django.urls import path
from . import views
urlpatterns = [
    path('mri/', views.register,name='register'),
    path('',views.home,name='home'),
    path('admin/',views.admin,name='adminpage'),
    path('login/', views.login, name='login'),
    path('patient_dashboard/<int:user_id>/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/<int:user_id>/',views.doctor_dashboard,name='doctor_dashboard'),
    path('receptionist_dashboard/<int:user_id>/',views.receptionist_dashboard,name='receptionist_dashboard'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('alldoctor/<int:user_id>/',views.alldoctor,name='alldoctor'),
    path('book-appointment/<int:user_id>/', views.book_appointment, name='book_appointment'),
    path('all-bookings/<int:user_id>/',views.all_bookings,name='all_bookings'),
    path('patient-prescriptions/<int:app_id>/<int:user_id>/',views.patient_prescriptions,name="patient_prescriptions"),
    path('add-patient/<int:user_id>/',views.add_patient,name='add_patient'),
    path('show_appointments/<int:user_id>/<status>/',views.show_appointments,name='show_appointments'),
    path('update_appointment_status/<int:app_id>/',views.update_appointment_status,name='update_appointment_status'),

]