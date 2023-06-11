from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
# Create your models here.

class Annoucements(models.Model):
    description = models.CharField(max_length=200)
    document = models.FileField(upload_to='media/accoucements')
    upload_at = models.DateTimeField(auto_now_add=True)





class student_profile(models.Model):
    student_photo =models.ImageField(upload_to='student_photo')
    student_name = models.CharField(max_length=200)
    student_roll_id = models.CharField(unique=True,max_length=30, primary_key=True, blank=False)
    college_name_student = models.CharField(max_length=500)
    student_program = models.CharField(max_length=200)
    student_admission_year = models.CharField(max_length=200)
    student_semester = models.IntegerField()
    student_father_name = models.CharField(max_length=200)
    student_mother_name = models.CharField(max_length=200)
    student_father_mobileno = models.IntegerField()
    student_mobile_no = models.IntegerField()
    student_email_id = models.EmailField(max_length=60)


#Student  Document----------------------------
class Detailed_Marks_Cards(models.Model):
    student_roll_id = models.CharField(max_length=30,blank=False)
    student_document_pdf = models.FileField(upload_to='student_document')
    student_program = models.CharField(max_length=100)
    student_semester = models.CharField(max_length=100)
    year_semester = models.DateTimeField()
    type = models.CharField(max_length=30)
    upload_date = models.DateTimeField(auto_now_add=True)

class hot_link(models.Model):
    event_title = models.CharField(max_length=2000)
    link_event = models.CharField(max_length=200)
    event_date = models.DateTimeField(auto_now_add=True)


class DMC(models.Model):
    student_roll_id = models.CharField(max_length=30, blank=True)
    student_document_pdf = models.FileField(upload_to='student_document')
    student_program = models.CharField(max_length=100)
    student_semester = models.CharField(max_length=100)
    year_semester = models.DateTimeField()
    type = models.CharField(max_length=30)
    upload_date = models.DateTimeField(auto_now_add=True)


class Result_Tabulation (models.Model):
    student_roll_id = models.CharField(max_length=30, blank=False)
    student_document_pdf = models.FileField(upload_to='student_document')
    student_program = models.CharField(max_length=100)
    student_semester = models.CharField(max_length=100)
    year_semester = models.DateTimeField()
    type = models.CharField(max_length=30)
    upload_date = models.DateTimeField(auto_now_add=True)


class Enquery(models.Model):
    student_enquiry_id = models.ForeignKey(User,on_delete= models.CASCADE, blank=True)
    enq_date = models.DateTimeField(auto_now_add=True)
    Enuery_descriptin = models.CharField(max_length=2000)
    Query_related_to = models.CharField(max_length=2000)
    college_reply = models.CharField(default='Pending', max_length=6000)






# Option for dropwodn answerhseet
# class option(models.Model):

class answer_sheet_request(models.Model):
    semester_opt = (
        ('1', 'Semester 1'),
        ('2', 'Semester 2'),
        ('3', 'Semester 3'),
        ('4', 'Semester 4'),
        ('5', 'Semester 5'),
        ('6', 'Semester 6'),
        ('7', 'Semester 7'),
        ('8', 'Semester 8'),
    )
    student_enquiry_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    semester = models.CharField(max_length=200, default=0, choices=semester_opt, blank=False)
    subject_name = models.CharField(max_length=200, default=None, blank=False)
    sub_pdf = models.FileField(blank=True, upload_to='ansersheetstudent')
    status = models.CharField(max_length=200, default='Pending', blank=True)
    enq_date = models.DateTimeField(auto_now_add=True)



class question_paper(models.Model):
    semester_opt = (
        ('1', 'Semester 1'),
        ('2', 'Semester 2'),
        ('3', 'Semester 3'),
        ('4', 'Semester 4'),
        ('5', 'Semester 5'),
        ('6', 'Semester 6'),
        ('7', 'Semester 7'),
        ('8', 'Semester 8'),
    )
    branch_ption = (
        ('CSE', 'Computer Science'),
        ('ME', 'Mechnical ')
    )
    student_enquiry_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    sub_name = models.CharField(max_length=200)
    semester = models.CharField(max_length=200, default=0, choices=semester_opt, blank=False)
    sub_pdf = models.FileField(blank=True, upload_to='questionpaper')
    branch = models.CharField(blank=False, choices=branch_ption, max_length=200 )
    type = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)




class student_progress(models.Model):
    student_id = models.ForeignKey(User, max_length=200, on_delete=models.CASCADE, blank=False)
    student_photo = models.ImageField( upload_to='student_result_photo')
    student_name = models.CharField(max_length=200)
    student_semester = models.IntegerField()
    student_mobile_no = models.IntegerField()
    student_mst1 = models.IntegerField()
    student_mst2 = models.IntegerField()
    student_mst3 = models.IntegerField()
    student_final_result = models.IntegerField()






