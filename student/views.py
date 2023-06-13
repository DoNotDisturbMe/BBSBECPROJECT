import datetime
import time
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.core.mail import message
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseRedirect, HttpResponse, request
from  django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.views import View
from  django.urls import  reverse_lazy
from django.views.generic.edit import CreateView
from .models import student_profile, Annoucements, Detailed_Marks_Cards, DMC, Result_Tabulation, Enquery, answer_sheet_request, question_paper, hot_link, student_progress, adminprofile
from .form import Enquery_form
from .decorators import login_required_with_autologout
# Create your views here.

#test
def test(request):
    return render(request, 'student/test.html')
# ----------------------------------------------------


#------------------------------Login-------------------------------------
@never_cache
def student(request):
        if request.method == 'POST':
            roll_no = request.POST.get('username')
            pass1 = request.POST.get('password')
            if roll_no == User.username in User and pass1 == User.password in User:
                messages.success(request, "Successfully Login...")
                login_success = authenticate(request,username = roll_no, password = pass1)
                if login_success is not None:
                    login(request, login_success)
                    messages.success(request, 'Success')
                    return redirect('home')
            if roll_no != User.username or pass1 != User.password:
                messages.info(request, "Please enter correct infromation...")
        return render(request, 'registration/login.html')


# ---------------------------------------  Registration.

def student_register(request):
    if request.method == 'POST':
        urolno = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2= request.POST.get('password1')
        print(urolno, email, pass2, pass1)
        if pass2 != pass1:
            return messages.info(request, "You confirms password does't match.")
        else:
            if urolno not in User:
                messages.info(request, "Contact You Mentor...")
            else:
                user_save = User.objects.create_user(urolno, email, pass2)
                user_save.save()
                HttpResponseRedirect("You account created Successfully !!")
                # redirect('/student')
            return redirect('student')
    return  render(request, 'registration/register.html')



def Logout(request):
    logout(request)
    return redirect('student')

# @login_required()
# def chagepassword(request, id):
#     User.objects.filter(username=id).update()

@login_required_with_autologout
def adlogout(request):
    Logout(request)
    return redirect("loginadmin")


#----------------------- After Login (student) ---------------------------------

@login_required_with_autologout
def user_home(request):
    user_id = request.user
    new_anou = Annoucements.objects.all()
    hot_lin = hot_link.objects.all()
    data = Enquery.objects.filter(student_enquiry_id=user_id).order_by("-id")
    student_pfile = student_profile.objects.filter(student_roll_id=user_id)
    # student_pro = student_progress.objects.all()
    # print(student_pro)
    profile = {
        'student_profile': student_pfile,
        'annou': new_anou,
        'hotlin':hot_lin,
        'data':data,
       # 'student_pro':student_pro
    }
    return render(request, 'student/student_home.html',profile)


@login_required_with_autologout
def student_progress(request, semester):
    user_request = request.user
    student_progresss = student_progress.objects.filter(student_id=user_request)
    data = {
        'student_pro': student_progresss
        }
    return render(request, 'student/student_progess.html', data)

@login_required_with_autologout
def annoucements(request):
    new_anou = Annoucements.objects.all()
    data = {
        'annou':new_anou
    }
    return  render(request, 'student/annoucements.html', data)


@login_required_with_autologout
def student_document(request):
    user_id = request.user
    Detailed_Marked_Card = Detailed_Marks_Cards.objects.filter(student_roll_id=user_id)
    DMCs = DMC.objects.filter(student_roll_id = user_id)
    Result_Tabulations = Result_Tabulation.objects.filter(student_roll_id= user_id)


    data = {
        'Detailed_Marked_Card': Detailed_Marked_Card,
        'DMC':DMCs,
        'Result':Result_Tabulations
    }
    return  render(request, 'student/student_document.html', data)

@login_required_with_autologout
def student_profilee(request):
    user_id = request.user
    student_pfile = student_profile.objects.filter(student_roll_id=user_id)
    data = {
        'stu_profile':student_pfile
    }
    return  render(request, 'student/student_profile.html', data)


@login_required_with_autologout
def student_banktransactions(request):
    return render(request, 'student/Banktransactions.html')



@login_required_with_autologout
def student_enquiry(request):
    user_id = request.user
    if request.method == 'POST':
        select_query = request.POST.get('selected_query')
        select_query1 = request.POST.get('selected_query1')
        discription  = request.POST.get('description')

        enquiry_save = Enquery.objects.create(student_enquiry_id=user_id, Enuery_descriptin= discription,
                                              Query_related_to=select_query1)
        enquiry_save.save()
        return  redirect('home/enquiry')
        # print(select_query, select_query1, discription)
    data = Enquery.objects.filter(student_enquiry_id=user_id).order_by("-id")
    fitler_data = {
        'data':data
    }
    print(fitler_data)
    return  render(request, 'student/student_enquiry.html', fitler_data)

@login_required_with_autologout
def student_contact_verification(request):
    filter_user = request.user
    filter_user_data = student_profile.objects.filter(student_roll_id=filter_user)[:1]
    data = {
        'filter_user_data':filter_user_data
    }
    return render(request, 'student/Contectverification.html', data)

@login_required_with_autologout
def student_apply_answersheet(request):
    user_account = request.user
    if request.method == 'POST':
        select_semester = request.POST.get('select_semester')
        subject = request.POST.get('subject')
        print(subject, select_semester)
        create_request = answer_sheet_request.objects.create(subject_name=subject, semester=select_semester, student_enquiry_id=user_account)
        create_request.save()
        return redirect("/")

    filter_data = answer_sheet_request.objects.filter(student_enquiry_id= user_account).order_by("-id")
    data  = {
        'filter_data':filter_data
    }
    return render(request, 'student/apply answersheet.html', data)


@login_required_with_autologout
def student_question(request):
    user_account = request.user
    type = request.POST.get('type')
    branch = request.POST.get('branch')
    select_semester = request.POST.get('select_semester')
    filter_question = question_paper.objects.filter(type = type, branch = branch, semester=select_semester)
    data = {
        'pdf_question':filter_question
    }

    return  render(request, 'student/old_question.html', data)


@login_required_with_autologout
def student_photo_and_sign(request):
    return render(request, 'student/photo and sing.html')

@login_required_with_autologout
def finepay(request):
    return  render(request, 'student/finepay.html')




#--------------------------- admin_login ------------------------------------------

# @admin_allowed()
def loginadmin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        passweod = request.POST.get('password')
        print(username, passweod)
        admin_login = authenticate(request, username = username, password = passweod)
        if admin_login is not None:
            messages.success(request, "You have Successfuly login!!")
            login(request, admin_login)
            return redirect("homeadmin")
        else:
            messages.info(request, "Enter valid id or password? ")
            return redirect(request, 'loginadmin')
    return render(request, 'template_admin/adminlogin.html')




# ----------------------------------------------------------------------------- Admin Section
@login_required_with_autologout
def homeadmin(request):
    uname = request.user
    admindata = adminprofile.objects.all()
    new_anou = Annoucements.objects.all()
    hot_lin = hot_link.objects.all()
    data = Enquery.objects.all().order_by("-id")
    data = {
        "admindata":admindata,
        'annou': new_anou,
        'hotlin': hot_lin,
        'data': data,
    }
    return render(request, "template_admin/adminhome.html", data)



# Annocument Admin --------
@login_required_with_autologout
def ann_admin(request):
    user_request = request.user
    admin_ann = Annoucements.objects.all().order_by("-id")
    data = {
        "annou":admin_ann
    }
    return render(request, 'template_admin/admin_annoucements.html', data)
# uploat annocuemetns

@login_required_with_autologout
def ann_uploade(request):
    if request.method == "POST":
        des = request.POST.get('description')
        file = request.FILES.get('document_anno')
        # print(des, file)
        ann_data = Annoucements.objects.create(description=des, document=file)
        ann_data.save()
        HttpResponseRedirect("Your Annocement Successfully Uploaded....")
        return redirect("adminannoucements")
    return render(request, "template_admin/annoucement_upload_admin.html")

@login_required_with_autologout
def delete_anno(request, id):
    edit_anno = Annoucements.objects.filter(id = id)
    edit_anno.delete()
    return redirect("adminannoucements")
#
# def ann_update(request, id):
#     if request.method == "POST":
#         filter_fordel = Annoucements.objects.get(id)
#         filter_fordel.delete()
#         des = request.POST.get('description')
#         file = request.FILES.get('document_anno')
#         print(des, file)
#         ann_data = Annoucements.objects.create(description=des, document=file)
#         ann_data.save()
#         return redirect("adminannoucements")
#

# Document of Student (Admin)  -----------------------------------------------------
@login_required_with_autologout
def doc_stu_admin(request):
    # user_id = request.user
    Detailed_Marked_Card = Detailed_Marks_Cards.objects.all()
    DMCs = DMC.objects.all()
    Result_Tabulations = Result_Tabulation.objects.all()

    data = {
        'Detailed_Marked_Card': Detailed_Marked_Card,
        'DMC': DMCs,
        'Result': Result_Tabulations
    }
    return render(request, "template_admin/student_document_admin.html", data)

@login_required_with_autologout
def doc_stu_delete_admin(request, id):
    Result_Tab = Result_Tabulation.objects.filter(id = id)
    Result_Tab.delete()
    detailed_mark = Detailed_Marks_Cards.objects.filter(id=id)
    detailed_mark.delete()
    DMCs = DMC.objects.filter(id=id)
    DMCs.delete()
    return redirect("doc_student")
@login_required_with_autologout
def doc_stu_upload_Re_tab(request):                  #Result Upload of Retabluation..............
    if request.method == "POST":
        student_roll = request.POST.get("studentrollno")
        student_re_doc = request.FILES.get("student_retab")
        stu_program = request.POST.get('stu_program')
        stu_sem = request.POST.get('student_sem')
        stu_year_sem  = request.POST.get('year_sem')
        stu_type_result = request.POST.get('type')
        new_data_retab = Result_Tabulation.objects.create(student_roll_id= student_roll,
                                         student_document_pdf=student_re_doc,
                                         student_program=stu_program,
                                         student_semester= stu_sem,
                                         year_semester=stu_year_sem,
                                         type = stu_type_result)
        new_data_retab.save()
        return redirect("doc_student")
    return render(request, 'template_admin/Result_tab.html')


@login_required_with_autologout
def doc_stu_upload_DMCS(request):  # Detailed Marks Upload----------
    if request.method == "POST":
        student_roll = request.POST.get("studentrollno")
        student_re_doc = request.FILES.get("student_retab")
        stu_program = request.POST.get('stu_program')
        stu_sem = request.POST.get('student_sem')
        stu_year_sem  = request.POST.get('year_sem')
        stu_type_result = request.POST.get('type')
        new_data_retab = Detailed_Marks_Cards.objects.create(student_roll_id= student_roll,
                                         student_document_pdf=student_re_doc,
                                         student_program=stu_program,
                                         student_semester= stu_sem,
                                         year_semester=stu_year_sem,
                                         type = stu_type_result)
        new_data_retab.save()
        return redirect("doc_student")
    return render(request, 'template_admin/DMCs_Upload.html')

@login_required_with_autologout
def doc_stu_upload_DMC(request):  #DMC Upload----------
    if request.method == "POST":
        student_roll = request.POST.get("studentrollno")
        student_re_doc = request.FILES.get("student_retab")
        stu_program = request.POST.get('stu_program')
        stu_sem = request.POST.get('student_sem')
        stu_year_sem  = request.POST.get('year_sem')
        stu_type_result = request.POST.get('type')
        new_data_retab = DMC.objects.create(student_roll_id= student_roll,
                                         student_document_pdf=student_re_doc,
                                         student_program=stu_program,
                                         student_semester= stu_sem,
                                         year_semester=stu_year_sem,
                                         type = stu_type_result)
        new_data_retab.save()
        return redirect("doc_student")
    return render(request, 'template_admin/Detailed_MC_Upload.html')



# Student Profile Admin section (Admin)  -----------------------------------------------------
@login_required_with_autologout
def stu_profile_admin(request):    #Data Exctration All Student.
    if request.method == "POST":
        name = request.POST.get("namefilter")
        roll = request.POST.get('rollno')
        print(name, roll)
        filterdata = student_profile.objects.filter(student_roll_id=roll, student_name=name)

        data = {
            'filter_profile_st':filterdata,
        }
        return render(request, 'template_admin/admin_student_profile.html', data)
    else:
        filter_profile_st = student_profile.objects.all()
        data = {
            'filter_profile_st':filter_profile_st,
        }
        return render(request, 'template_admin/admin_student_profile.html', data)

@login_required_with_autologout
def stu_add_admin(request): # Add Student Profile In Database.,---------------
    if request.method == "POST":
        name_stu = request.POST.get('namefilter')
        roll_stu = request.POST.get('rollno')
        c_name = request.POST.get('cname')
        stu_pro = request.POST.get('stuprogram')
        admission_y = request.POST.get('adminssion_y')
        stu_sem = request.POST.get('Semester')
        father_n = request.POST.get('f_name')
        mohter_n = request.POST.get('m_name')
        fm_no = request.POST.get('f_mNo')
        stu_m = request.POST.get('stu_m')
        stu_email = request.POST.get('stu_email')
        stu_photo = request.FILES.get('stu_photo')
        print(
            name_stu, roll_stu, c_name, stu_pro, admission_y,
            stu_sem, father_n, mohter_n, fm_no, stu_m , stu_email,
            stu_photo
        )
        create_profile = student_profile.objects.create(student_photo=stu_photo, student_name =name_stu,
                                       student_roll_id=roll_stu,  college_name_student=c_name,
                                       student_program=stu_pro, student_admission_year=admission_y,
                                       student_semester=stu_sem, student_father_name=father_n,
                                       student_mother_name=mohter_n, student_father_mobileno=fm_no,
                                       student_mobile_no=stu_m, student_email_id=stu_email)
        create_profile.save()
        return redirect("stuprofile_admin")

    return  render(request, 'template_admin/add_student_admin.html')

@login_required_with_autologout
def view_profile_admin(request, id): #----------------- View Student profile In Detailed.
    stu_profile = student_profile.objects.filter(student_roll_id=id)
    data = {
        'stu_profile':stu_profile
    }
    return render(request, "template_admin/viewprofileadmin.html", data)


@login_required_with_autologout
def del_profile_stu_admin(request, id):   #Delte Profile Based On the User Name....
    stu_profile = student_profile.objects.filter(student_roll_id= id)
    stu_profile.delete()
    return redirect("stuprofile_admin")

@login_required_with_autologout
def edit_profile_stu_admin(request, id): #Edit The profile of student.
    if request.method == "POST":
        name_stu = request.POST.get('namefilter')
        roll_stu = request.POST.get('rollno')
        c_name = request.POST.get('cname')
        stu_pro = request.POST.get('stuprogram')
        admission_y = request.POST.get('adminssion_y')
        stu_sem = request.POST.get('Semester')
        father_n = request.POST.get('f_name')
        mohter_n = request.POST.get('m_name')
        fm_no = request.POST.get('f_mNo')
        stu_m = request.POST.get('stu_m')
        stu_email = request.POST.get('stu_email')
        # stu_photo = request.FILES.get('stu_photo')
        print(
            name_stu, roll_stu, c_name, stu_pro, admission_y,
            stu_sem, father_n, mohter_n, fm_no, stu_m, stu_email,
            # stu_photo
        )
        create_profile = student_profile.objects.filter(student_roll_id=id).update(student_name=name_stu,
                                                        student_roll_id=roll_stu, college_name_student=c_name,
                                                        student_program=stu_pro, student_admission_year=admission_y,
                                                        student_semester=stu_sem, student_father_name=father_n,
                                                        student_mother_name=mohter_n, student_father_mobileno=fm_no,
                                                        student_mobile_no=stu_m, student_email_id=stu_email)
        return redirect(reverse("stuprofile_admin"))


    data = student_profile.objects.filter(student_roll_id=id)
    student_edit_profile = {
        'student_profile_edit':data
    }
    return render(request, "template_admin/edit_stu_profile_admin.html", student_edit_profile)


# Student Enquery Admin Section ---------------------
@login_required_with_autologout
def admin_reply_enq(request):              #View Query by Admin (All Query)
    data = Enquery.objects.all().order_by("-id")
    fitler_data = {
        'data': data
        }
    print(fitler_data)
    return render(request, "template_admin/student_enq_admin.html",fitler_data)

@login_required_with_autologout
def reply_enq_admin(request, id):
    if request.method == 'POST':
        # student_id = Enquery.student_enquiry_id      #user Id  2001308
        quey_id_user = request.POST.get('id')        #query ID like 1, 2 3 ,4
        # quey_date = request.POST.get('enq_date')
        # enq_des = request.POST.get('enq_des')
        # enq_re = request.POST.get('req_related')
        c_reply = request.POST.get('college_reply')
        print(c_reply)
        Enquery.objects.filter(id = quey_id_user).update(
           # Enuery_descriptin = enq_des,
           # Query_related_to = enq_re,
           college_reply  = c_reply)
        return redirect(reverse("adminenq"))

    data = Enquery.objects.filter(id = id)
    filter_data = {
        "data" : data
    }
    return render(request, 'template_admin/enq_reply_admin.html', filter_data)




#Contact Verification By Admin Pannel ----------------------------





#Answer sheet PDF Uploaded by Mentor...........
@login_required_with_autologout
def anssheetuploadadmin(request):
    data = answer_sheet_request.objects.all().order_by("-id")
    data1 = {
        "filter_data":data
    }
    return render(request, 'template_admin/admin_upload_answersheet.html', data1)

@login_required_with_autologout
def upload_ans_admin(request, id):
    if request.method == "POST":
        enq_id = request.POST.get("enq_id")
        pdf_up = request.FILES.get("pdfupload")
        statusss = request.POST.get("statuss")
        semesterr = request.POST.get("semester")
        print(enq_id, pdf_up)
        answer_sheet_request.objects.filter(id = id).update(semester = semesterr,status = statusss,sub_pdf = pdf_up )
        return redirect(reverse("anssheetupload"))
    data = answer_sheet_request.objects.filter(id = id)
    data1 = {
        "uploadans":data
    }
    return render(request, "template_admin/upload_ans_admin.html", data1)


# Older Question Paper Upload By Admin------
@login_required_with_autologout
def admin_older_question_paper(request):   #Retrive All File from Data Base....
    data = question_paper.objects.all().order_by("id")
    dic_data = {
        "pdf_question":data
    }
    return  render(request, "template_admin/older_question_by_admin.html", dic_data)

@login_required_with_autologout
def admin_olderq_add(request):
    if request.method == "POST":
        user_add = request.user
        subject_name = request.POST.get("subname")
        semester = request.POST.get('semester')
        branch = request.POST.get('Branch')
        type1 = request.POST.get('type')
        subject_pdf = request.FILES.get("sub_pdf")
        print(subject_name, semester, branch, type1, subject_pdf)
        new_data = question_paper.objects.create(student_enquiry_id= user_add, sub_name=subject_name, semester = semester,
                                      branch = branch, type = type1,
                                      sub_pdf=subject_pdf)
        new_data.save()
        return redirect(reverse("olderquestion"))

    return render(request, "template_admin/add question paper.html")


@login_required_with_autologout
def admin_oldrq_del(request, id):
    user_req_delete = question_paper.objects.filter(id= id)
    user_req_delete.delete()
    return redirect("olderquestion")