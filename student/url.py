from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import  settings
from django.views import View
from . import views




urlpatterns = [
    #login setu student
    path('', views.student,  name = "student"),
    path('register/', views.student_register, name = 'register_student'),
    path('Logout/', views.Logout, name = 'Logout'),

    # -------------------------
    # Authentication System------------------------

    #user_home
    path('home', views.user_home, name = 'home'),
    # path('student_progress/<int: semester>', views.student_progress),
    path('home/annoucements', views.annoucements, name = 'home/annoucements'),
    path('home/studentdocument', views.student_document, name = 'home/studentdocument'),
    path('home/studentprofilee', views.student_profilee, name = 'home/studentprofilee'),
    path('home/banktransactions', views.student_banktransactions, name = 'home/banktransactions'),
    path('home/enquiry', views.student_enquiry, name = 'home/enquiry'),
    path('home/contectverification', views.student_contact_verification, name = 'home/contectverification'),
    path('home/answersheet', views.student_apply_answersheet, name = 'home/answersheet'),
    path('home/question', views.student_question, name = 'home/question'),
    path('home/uploadphoto', views.student_photo_and_sign, name = 'home/uploadphoto'),
    path('home/finepay', views.finepay, name = 'home/finepay'),

    # Testting Url

    path('test/', views.test, name = 'test'),
# ----------------------------------------------------------------


    # -------------------------------------- Admin Section  ----------------------------------
path('login', views.loginadmin, name = "loginadmin"),   #Admin Login
    # ---------------------

path('homeadmin', views.homeadmin, name = "homeadmin"), # Admin Home
#annocument---
path("acc_add", views.ann_admin, name = "adminannoucements"),
path("upload", views.ann_uploade, name = "upload"),
path("delete/<id>", views.delete_anno, name = "delete"),
# path("update/<id>", views.ann_update, name = "update")

# Student Document Admin Section
path("doc_student", views.doc_stu_admin, name = "doc_student"), #---- Data Reterive
path("doc_student/<id>", views.doc_stu_delete_admin, name = "doc_student_del"),  #Delete Query
path("student_dmc", views.doc_stu_upload_Re_tab, name = "upload_retabluation_result"), #Upload Retabulation Result---------
path("student_Detailed_MC", views.doc_stu_upload_DMCS, name = "upload_Detaild_MC_result"), #Upload Detailed Marks
path("student_DMC", views.doc_stu_upload_DMC, name = "upload_DMC_result"),


#Student Profile Admin.------------------

path("stup_admin", views.stu_profile_admin, name = "stuprofile_admin"), # Data Exctraction URL
path("add_student", views. stu_add_admin, name = "stu_addadmin"), #Add Student Profile by Admin.
path("view_profile/<id>", views.view_profile_admin, name = "profile"), # View Detailed Profile Of Student.
path("delprofile/<id>", views.del_profile_stu_admin, name = "delete"), #Delete user profile based on User Name.
path("editprofile/<id>", views.edit_profile_stu_admin, name= "edit"), #Edit the profile details of the studen by the admin.

# Admin Enquery
path("enqu_admin", views.admin_reply_enq, name = "adminenq"),  #All view command by ADMIn.,
path("enq_reply/<id>", views.reply_enq_admin, name = "adminreply"), #edit replay which is default is pedning.


#Admin Answersheet Upload
path("adminansupload", views.anssheetuploadadmin, name = "anssheetupload"),
path("answersheetupload/<id>",views. upload_ans_admin, name="answersheetupload"),


#Upload Older Question Paper by Admin.
path("adminquestion", views.admin_older_question_paper, name = "olderquestion"),
path("addquestion", views.admin_olderq_add, name = "addquestion"),
path("deleteoldq/<id>", views.admin_oldrq_del, name ="deloldq"),












]


