from django.contrib import admin
from .models import student_profile, Annoucements, Detailed_Marks_Cards, DMC, Result_Tabulation, Enquery, answer_sheet_request, question_paper, hot_link, student_progress, adminprofile


# Register your models here.
@admin.register(student_profile)
class student(admin.ModelAdmin):
    list_display = ['student_photo', 'student_name', 'student_roll_id', 'college_name_student', 'student_program', 'student_admission_year', 'student_semester', 'student_father_name', 'student_mother_name', 'student_father_mobileno', 'student_mobile_no', 'student_email_id']
    filter = ['student-roll']


@admin.register(Annoucements)
class accnoucements(admin.ModelAdmin):
    list_display = ['description', 'document', 'upload_at']
    filter  = ['upload_at']

@admin.register(Detailed_Marks_Cards)
class student_document_admin (admin.ModelAdmin):
    list_display =  ['student_roll_id','student_document_pdf', 'student_program',
                     'student_semester', 'year_semester', 'type',
                     'upload_date']


@admin.register(DMC)
class student_document_admin (admin.ModelAdmin):
    list_display =  ['student_roll_id','student_document_pdf', 'student_program',
                     'student_semester', 'year_semester', 'type',
                     'upload_date']



@admin.register(Result_Tabulation)
class student_document_admin (admin.ModelAdmin):
    list_display =  ['student_roll_id','student_document_pdf', 'student_program',
                     'student_semester', 'year_semester', 'type',
                     'upload_date']

@admin.register(Enquery)
class student_enquiry(admin.ModelAdmin):
    list_display = ['student_enquiry_id', 'enq_date',
                    'Enuery_descriptin', 'Query_related_to',
                    'college_reply']


@admin.register(answer_sheet_request)
class student_ans_sheet(admin.ModelAdmin):
    list_display = [
        'student_enquiry_id', 'semester', 'subject_name', 'sub_pdf', 'status', 'enq_date'
    ]

@admin.register(question_paper)
class student_question_paper(admin.ModelAdmin):
    list_display = [
        'student_enquiry_id','sub_name', 'semester', 'sub_pdf',
        'branch', 'type', 'date'
    ]

@admin.register(hot_link)
class event_link(admin.ModelAdmin):
    list_display = [
        'event_title', 'link_event', 'event_date'
    ]


@admin.register(student_progress)
class student_progress_admin(admin.ModelAdmin):
    list_display = [
        'student_id', 'student_photo',
        'student_name', 'student_semester',
        'student_mobile_no','student_mst1', 'student_mst2',
        'student_mst3', 'student_final_result'
    ]


@admin.register(adminprofile)
class adminProfile(admin.ModelAdmin):
    list_display = [
    "name","collegeId",
    "mobileno", "photo"
    ]