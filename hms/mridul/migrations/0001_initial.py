# Generated by Django 4.2.7 on 2024-10-23 16:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('admission_id', models.AutoField(primary_key=True, serialize=False)),
                ('admission_date', models.DateField()),
                ('discharge_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'admission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContactSupport',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('status', models.CharField(blank=True, max_length=11, null=True)),
                ('response', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'contact_support',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('education', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('consultation_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('time_slot_begin', models.TimeField()),
                ('time_slot_end', models.TimeField()),
                ('experience', models.IntegerField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
            ],
            options={
                'db_table': 'doctor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FinalBills',
            fields=[
                ('bill_id', models.IntegerField(primary_key=True, serialize=False)),
                ('advance_paid', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pending_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('paid_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('refund', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'final_bills',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('date_of_birth', models.DateField()),
                ('phone_no', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=3, null=True)),
                ('emergency_contact_name', models.CharField(blank=True, max_length=100, null=True)),
                ('emergency_contact_number', models.CharField(blank=True, max_length=15, null=True)),
                ('registration_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('billing_date', models.DateField(blank=True, null=True)),
                ('payment_status', models.CharField(blank=True, max_length=7, null=True)),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prescriptions',
            fields=[
                ('prescription_id', models.AutoField(primary_key=True, serialize=False)),
                ('prescription_date', models.DateField()),
                ('symptoms', models.TextField()),
                ('cause', models.TextField(blank=True, null=True)),
                ('lab_tests', models.TextField(blank=True, null=True)),
                ('hospitalization_needed', models.CharField(blank=True, max_length=3, null=True)),
                ('type_of_hospitalization', models.CharField(blank=True, max_length=12, null=True)),
                ('surgery_needed', models.CharField(blank=True, max_length=3, null=True)),
                ('dietary_precautions', models.TextField(blank=True, null=True)),
                ('remark_on_lab_test', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'prescriptions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_value', models.IntegerField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rating',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('receptionist_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('hire_date', models.DateField(blank=True, null=True)),
                ('shift', models.CharField(blank=True, max_length=7, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'receptionist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_number', models.CharField(max_length=10)),
                ('room_type', models.CharField(blank=True, max_length=12, null=True)),
                ('status', models.CharField(blank=True, max_length=9, null=True)),
                ('daily_rate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'room',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=15, null=True)),
                ('last_name', models.CharField(blank=True, max_length=15, null=True)),
                ('email_id', models.CharField(max_length=50, unique=True)),
                ('phone_no', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('role_as_a', models.CharField(blank=True, max_length=12, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='mridul.patient')),
                ('prescription', models.TextField()),
                ('lab_test_reports', models.TextField(blank=True, null=True)),
                ('lab_bills', models.TextField(blank=True, null=True)),
                ('final_bill', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'documents',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MedicinalPrescription',
            fields=[
                ('prescription', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='mridul.prescriptions')),
                ('medicine_name', models.TextField()),
                ('dosage', models.TextField()),
                ('remark', models.TextField(blank=True, null=True)),
                ('date_of_prescription', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'medicinal_prescription',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PreSurgeryInfo',
            fields=[
                ('prescription', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='mridul.prescriptions')),
                ('surgery_type', models.TextField()),
                ('suggested_date', models.DateField()),
                ('suggested_time', models.CharField(blank=True, max_length=50, null=True)),
                ('advice', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pre_surgery_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('reason', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Scheduled', max_length=9, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 10, 23, 16, 19, 8, 445708, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 10, 23, 16, 19, 8, 445708, tzinfo=datetime.timezone.utc))),
                ('doctor_id', models.ForeignKey(db_column='doctor_id', on_delete=django.db.models.deletion.CASCADE, to='mridul.doctor')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='mridul.users')),
            ],
            options={
                'db_table': 'appointment',
                'managed': True,
            },
        ),
    ]
