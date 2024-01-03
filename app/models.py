from django.db import models

from users.models import User


# Create your models here.

class StudentMaster(models.Model):
    regdno = models.CharField(db_column='REGDNO', primary_key=True, max_length=100)  # Field name made lowercase.
    pinno = models.CharField(db_column='PINNO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rollno = models.CharField(db_column='ROLLNO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=300, blank=True, null=True)  # Field name made lowercase.
    father_name = models.CharField(db_column='FATHER_NAME', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ssc_year = models.CharField(db_column='SSC_YEAR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssc_marks = models.CharField(db_column='SSC_MARKS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssc_percentage = models.CharField(db_column='SSC_PERCENTAGE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inter_year = models.CharField(db_column='INTER_YEAR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inter_marks = models.CharField(db_column='INTER_MARKS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inter_percentage = models.CharField(db_column='INTER_PERCENTAGE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    academic_year_from = models.CharField(db_column='ACADEMIC_YEAR_FROM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    academic_year_to = models.CharField(db_column='ACADEMIC_YEAR_TO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    curr_sem = models.IntegerField(db_column='CURR_SEM', blank=True, null=True)  # Field name made lowercase.
    sem1_sgpa = models.FloatField(db_column='SEM1_SGPA', blank=True, null=True)  # Field name made lowercase.
    sem2_sgpa = models.FloatField(db_column='SEM2_SGPA', blank=True, null=True)  # Field name made lowercase.
    sem3_sgpa = models.FloatField(db_column='SEM3_SGPA', blank=True, null=True)  # Field name made lowercase.
    sem4_sgpa = models.FloatField(db_column='SEM4_SGPA', blank=True, null=True)  # Field name made lowercase.
    sem5_sgpa = models.FloatField(db_column='SEM5_SGPA', blank=True, null=True)  # Field name made lowercase.
    sem6_sgpa = models.FloatField(db_column='SEM6_SGPA', blank=True, null=True)  # Field name made lowercase.
    sem7_sgpa = models.FloatField(db_column='SEM7_SGPA', blank=True, null=True)  # Field name made lowercase.
    sem8_sgpa = models.FloatField(db_column='SEM8_SGPA', blank=True, null=True)  # Field name made lowercase.
    sem9_sgpa = models.FloatField(db_column='SEM9_SGPA', blank=True, null=True)  # Field name made lowercase.
    sem10_sgpa = models.FloatField(db_column='SEM10_SGPA', blank=True, null=True)  # Field name made lowercase.
    sem11_sgpa = models.FloatField(db_column='SEM11_SGPA', blank=True, null=True)  # Field name made lowercase.
    sem12_sgpa = models.FloatField(db_column='SEM12_SGPA', blank=True, null=True)  # Field name made lowercase.
    sem13_sgpa = models.FloatField(db_column='SEM13_SGPA', blank=True, null=True)  # Field name made lowercase.
    sem14_sgpa = models.FloatField(db_column='SEM14_SGPA', blank=True, null=True)  # Field name made lowercase.
    sem15_sgpa = models.FloatField(db_column='SEM15_SGPA', blank=True, null=True)  # Field name made lowercase.
    cgpa = models.FloatField(db_column='CGPA', blank=True, null=True)  # Field name made lowercase.
    academic_backlogs = models.CharField(db_column='ACADEMIC_BACKLOGS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    doorno = models.CharField(db_column='DOORNO', max_length=350, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=350, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=350, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=350, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=350, blank=True, null=True)  # Field name made lowercase.
    pincode = models.CharField(db_column='PINCODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=350, blank=True, null=True)  # Field name made lowercase.
    parent_contact_no = models.CharField(db_column='PARENT_CONTACT_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parent_email_id = models.CharField(db_column='PARENT_EMAIL_ID', max_length=350, blank=True, null=True)  # Field name made lowercase.
    hostler = models.CharField(db_column='HOSTLER', max_length=5, blank=True, null=True)  # Field name made lowercase.
    hostel_acno = models.CharField(db_column='HOSTEL_ACNO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    hostel_roomno = models.CharField(db_column='HOSTEL_ROOMNO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    hostel_floor = models.CharField(db_column='HOSTEL_FLOOR', max_length=25, blank=True, null=True)  # Field name made lowercase.
    hostel_code = models.CharField(db_column='HOSTEL_CODE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bank_name = models.CharField(db_column='BANK_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    bank_acno = models.CharField(db_column='BANK_ACNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    section = models.CharField(db_column='SECTION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    branch_code = models.CharField(db_column='BRANCH_CODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    course_code = models.CharField(db_column='COURSE_CODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    degree_code = models.CharField(db_column='DEGREE_CODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    college_code = models.CharField(db_column='COLLEGE_CODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campus = models.CharField(db_column='CAMPUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dept_code = models.CharField(db_column='DEPT_CODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='REMARKS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dt_time = models.DateTimeField(db_column='DT_TIME', blank=True, null=True)  # Field name made lowercase.
    batch = models.CharField(db_column='BATCH', max_length=100, blank=True, null=True)  # Field name made lowercase.
    specialization_code = models.CharField(max_length=100, blank=True, null=True)
    specialization_desc = models.CharField(max_length=1000, blank=True, null=True)
    religion = models.CharField(db_column='RELIGION', max_length=350, blank=True, null=True)  # Field name made lowercase.
    ssc_board = models.CharField(db_column='SSC_BOARD', max_length=350, blank=True, null=True)  # Field name made lowercase.
    inter_board = models.CharField(db_column='INTER_BOARD', max_length=350, blank=True, null=True)  # Field name made lowercase.
    degree_board = models.CharField(db_column='DEGREE_BOARD', max_length=350, blank=True, null=True)  # Field name made lowercase.
    pg_board = models.CharField(db_column='PG_BOARD', max_length=350, blank=True, null=True)  # Field name made lowercase.
    ssc_grade = models.CharField(db_column='SSC_GRADE', max_length=350, blank=True, null=True)  # Field name made lowercase.
    inter_grade = models.CharField(db_column='INTER_GRADE', max_length=350, blank=True, null=True)  # Field name made lowercase.
    degree_grade = models.CharField(db_column='DEGREE_GRADE', max_length=350, blank=True, null=True)  # Field name made lowercase.
    pg_grade = models.CharField(db_column='PG_GRADE', max_length=350, blank=True, null=True)  # Field name made lowercase.
    rank = models.CharField(db_column='RANK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    category2 = models.CharField(db_column='CATEGORY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parallel_course = models.CharField(db_column='PARALLEL_COURSE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    gemes = models.CharField(db_column='GEMES', max_length=350, blank=True, null=True)  # Field name made lowercase.
    mothername = models.CharField(db_column='MOTHERNAME', max_length=350, blank=True, null=True)  # Field name made lowercase.
    guardianname = models.CharField(db_column='GUARDIANNAME', max_length=350, blank=True, null=True)  # Field name made lowercase.
    permanent_address = models.CharField(db_column='PERMANENT_ADDRESS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    local_address = models.CharField(db_column='LOCAL_ADDRESS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    guardian_contact = models.CharField(db_column='GUARDIAN_CONTACT', max_length=350, blank=True, null=True)  # Field name made lowercase.
    occupation_parent = models.CharField(db_column='OCCUPATION_PARENT', max_length=350, blank=True, null=True)  # Field name made lowercase.
    mole1 = models.CharField(db_column='MOLE1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mole2 = models.CharField(db_column='MOLE2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    blood_group = models.CharField(db_column='BLOOD_GROUP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    major_illnesss_treated = models.CharField(db_column='MAJOR_ILLNESSS_TREATED', max_length=350, blank=True, null=True)  # Field name made lowercase.
    degree_year = models.CharField(db_column='DEGREE_YEAR', max_length=350, blank=True, null=True)  # Field name made lowercase.
    degree_marks = models.CharField(db_column='DEGREE_MARKS', max_length=350, blank=True, null=True)  # Field name made lowercase.
    degree_percentage = models.CharField(db_column='DEGREE_PERCENTAGE', max_length=350, blank=True, null=True)  # Field name made lowercase.
    pg_year = models.CharField(db_column='PG_YEAR', max_length=350, blank=True, null=True)  # Field name made lowercase.
    pg_marks = models.CharField(db_column='PG_MARKS', max_length=350, blank=True, null=True)  # Field name made lowercase.
    pg_percentage = models.CharField(db_column='PG_PERCENTAGE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hostel_block = models.CharField(db_column='HOSTEL_BLOCK', max_length=350, blank=True, null=True)  # Field name made lowercase.
    management_deposit = models.FloatField(db_column='MANAGEMENT_DEPOSIT', blank=True, null=True)  # Field name made lowercase.
    management_deposit_date = models.DateTimeField(db_column='MANAGEMENT_DEPOSIT_DATE', blank=True, null=True)  # Field name made lowercase.
    management_receipt_no = models.CharField(db_column='MANAGEMENT_RECEIPT_NO', max_length=350, blank=True, null=True)  # Field name made lowercase.
    caution_deposit = models.FloatField(db_column='CAUTION_DEPOSIT', blank=True, null=True)  # Field name made lowercase.
    caution_receipt_date = models.DateTimeField(db_column='CAUTION_RECEIPT_DATE', blank=True, null=True)  # Field name made lowercase.
    caution_receipt_no = models.CharField(db_column='CAUTION_RECEIPT_NO', max_length=350, blank=True, null=True)  # Field name made lowercase.
    pf = models.FloatField(db_column='PF', blank=True, null=True)  # Field name made lowercase.
    hostel_arrears = models.FloatField(db_column='HOSTEL_ARREARS', blank=True, null=True)  # Field name made lowercase.
    hostel_arrears_mon = models.CharField(db_column='HOSTEL_ARREARS_MON', max_length=350, blank=True, null=True)  # Field name made lowercase.
    hostel_arrears_year = models.CharField(db_column='HOSTEL_ARREARS_YEAR', max_length=350, blank=True, null=True)  # Field name made lowercase.
    hostel_account_close = models.CharField(db_column='HOSTEL_ACCOUNT_CLOSE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    admission_fee = models.FloatField(db_column='ADMISSION_FEE', blank=True, null=True)  # Field name made lowercase.
    hostel_refund_to_student = models.FloatField(db_column='HOSTEL_REFUND_TO_STUDENT', blank=True, null=True)  # Field name made lowercase.
    hostel_closing_reason = models.CharField(db_column='HOSTEL_CLOSING_REASON', max_length=500, blank=True, null=True)  # Field name made lowercase.
    hostel_adjustment_from_management = models.FloatField(db_column='HOSTEL_ADJUSTMENT_FROM_MANAGEMENT', blank=True, null=True)  # Field name made lowercase.
    hostel_adjustment_from_caution = models.FloatField(db_column='HOSTEL_ADJUSTMENT_FROM_CAUTION', blank=True, null=True)  # Field name made lowercase.
    hostel_total_adjustment = models.FloatField(db_column='HOSTEL_TOTAL_ADJUSTMENT', blank=True, null=True)  # Field name made lowercase.
    hostel_closing_date = models.DateTimeField(db_column='HOSTEL_CLOSING_DATE', blank=True, null=True)  # Field name made lowercase.
    hostel_closing_arrear = models.FloatField(db_column='HOSTEL_CLOSING_ARREAR', blank=True, null=True)  # Field name made lowercase.
    hostel_deposit_reason = models.CharField(db_column='HOSTEL_DEPOSIT_REASON', max_length=500, blank=True, null=True)  # Field name made lowercase.
    demand = models.IntegerField(db_column='DEMAND', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ftype = models.CharField(db_column='FTYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    module_code = models.CharField(db_column='MODULE_CODE', max_length=350, blank=True, null=True)  # Field name made lowercase.
    admission_fee_date = models.DateTimeField(db_column='ADMISSION_FEE_DATE', blank=True, null=True)  # Field name made lowercase.
    hostel_transfer_to_misc = models.FloatField(db_column='HOSTEL_TRANSFER_TO_MISC', blank=True, null=True)  # Field name made lowercase.
    hostel_joining_date = models.DateTimeField(db_column='HOSTEL_JOINING_DATE', blank=True, null=True)  # Field name made lowercase.
    user_type = models.CharField(db_column='USER_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=350, blank=True, null=True)  # Field name made lowercase.
    parent_user_id = models.CharField(db_column='PARENT_USER_ID', max_length=350, blank=True, null=True)  # Field name made lowercase.
    parent_password = models.CharField(db_column='PARENT_PASSWORD', max_length=350, blank=True, null=True)  # Field name made lowercase.
    year_of_admission = models.CharField(db_column='YEAR_OF_ADMISSION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    eamcet_rank = models.CharField(db_column='EAMCET_RANK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gat_rank = models.CharField(db_column='GAT_RANK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    admission_type = models.CharField(db_column='ADMISSION_TYPE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    present_stay = models.CharField(db_column='PRESENT_STAY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    transport_type = models.CharField(db_column='TRANSPORT_TYPE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    co_curricular_activities = models.CharField(db_column='CO_CURRICULAR_ACTIVITIES', max_length=200, blank=True, null=True)  # Field name made lowercase.
    extra_curricular_activities = models.CharField(db_column='EXTRA_CURRICULAR_ACTIVITIES', max_length=200, blank=True, null=True)  # Field name made lowercase.
    displinary_action_taken = models.CharField(db_column='DISPLINARY_ACTION_TAKEN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    health_problems = models.CharField(db_column='HEALTH_PROBLEMS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    contact_ice = models.CharField(db_column='CONTACT_ICE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    strengths = models.CharField(db_column='STRENGTHS', max_length=300, blank=True, null=True)  # Field name made lowercase.
    weaknesses = models.CharField(db_column='WEAKNESSES', max_length=300, blank=True, null=True)  # Field name made lowercase.
    counselor = models.CharField(db_column='COUNSELOR', max_length=300, blank=True, null=True)  # Field name made lowercase.
    amc_chairperson_name = models.CharField(db_column='AMC_CHAIRPERSON_NAME', max_length=300, blank=True, null=True)  # Field name made lowercase.
    additional_info = models.CharField(db_column='ADDITIONAL_INFO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    backlogs = models.CharField(db_column='BACKLOGS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    backlog_subject1 = models.CharField(db_column='BACKLOG_SUBJECT1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_sub1_year_appeared = models.CharField(db_column='BACKLOG_SUB1_YEAR_APPEARED', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_sub1_year_cleared = models.CharField(db_column='BACKLOG_SUB1_YEAR_CLEARED', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_subject2 = models.CharField(db_column='BACKLOG_SUBJECT2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_sub2_year_appeared = models.CharField(db_column='BACKLOG_SUB2_YEAR_APPEARED', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_sub2_year_cleared = models.CharField(db_column='BACKLOG_SUB2_YEAR_CLEARED', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_subject3 = models.CharField(db_column='BACKLOG_SUBJECT3', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_sub3_year_appeared = models.CharField(db_column='BACKLOG_SUB3_YEAR_APPEARED', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_sub3_year_cleared = models.CharField(db_column='BACKLOG_SUB3_YEAR_CLEARED', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_subject4 = models.CharField(db_column='BACKLOG_SUBJECT4', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_sub4_year_appeared = models.CharField(db_column='BACKLOG_SUB4_YEAR_APPEARED', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_sub4_year_cleared = models.CharField(db_column='BACKLOG_SUB4_YEAR_CLEARED', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_subject5 = models.CharField(db_column='BACKLOG_SUBJECT5', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_sub5_year_appeared = models.CharField(db_column='BACKLOG_SUB5_YEAR_APPEARED', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_sub5_year_cleared = models.CharField(db_column='BACKLOG_SUB5_YEAR_CLEARED', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_subject6 = models.CharField(db_column='BACKLOG_SUBJECT6', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_sub6_year_appeared = models.CharField(db_column='BACKLOG_SUB6_YEAR_APPEARED', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_sub6_year_cleared = models.CharField(db_column='BACKLOG_SUB6_YEAR_CLEARED', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_subject7 = models.CharField(db_column='BACKLOG_SUBJECT7', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_sub7_year_appeared = models.CharField(db_column='BACKLOG_SUB7_YEAR_APPEARED', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_sub7_year_cleared = models.CharField(db_column='BACKLOG_SUB7_YEAR_CLEARED', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_subject8 = models.CharField(db_column='BACKLOG_SUBJECT8', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_sub8_year_appeared = models.CharField(db_column='BACKLOG_SUB8_YEAR_APPEARED', max_length=300, blank=True, null=True)  # Field name made lowercase.
    backlog_sub8_year_cleared = models.CharField(db_column='BACKLOG_SUB8_YEAR_CLEARED', max_length=300, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='CLASS', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    skill1_name = models.CharField(db_column='SKILL1_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    skill2_name = models.CharField(db_column='SKILL2_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    skill3_name = models.CharField(db_column='SKILL3_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    skill1_desc = models.CharField(db_column='SKILL1_DESC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    skill2_desc = models.CharField(db_column='SKILL2_DESC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    skill3_desc = models.CharField(db_column='SKILL3_DESC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    skill1_level = models.CharField(db_column='SKILL1_LEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    skill2_level = models.CharField(db_column='SKILL2_LEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    skill3_level = models.CharField(db_column='SKILL3_LEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language1_name = models.CharField(db_column='LANGUAGE1_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language2_name = models.CharField(db_column='LANGUAGE2_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language3_name = models.CharField(db_column='LANGUAGE3_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language4_name = models.CharField(db_column='LANGUAGE4_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language5_name = models.CharField(db_column='LANGUAGE5_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language1_read = models.CharField(db_column='LANGUAGE1_READ', max_length=5, blank=True, null=True)  # Field name made lowercase.
    language2_read = models.CharField(db_column='LANGUAGE2_READ', max_length=5, blank=True, null=True)  # Field name made lowercase.
    language3_read = models.CharField(db_column='LANGUAGE3_READ', max_length=5, blank=True, null=True)  # Field name made lowercase.
    language4_read = models.CharField(db_column='LANGUAGE4_READ', max_length=5, blank=True, null=True)  # Field name made lowercase.
    language5_read = models.CharField(db_column='LANGUAGE5_READ', max_length=5, blank=True, null=True)  # Field name made lowercase.
    language1_write = models.CharField(db_column='LANGUAGE1_WRITE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    language2_write = models.CharField(db_column='LANGUAGE2_WRITE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    language3_write = models.CharField(db_column='LANGUAGE3_WRITE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    language4_write = models.CharField(db_column='LANGUAGE4_WRITE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    language5_write = models.CharField(db_column='LANGUAGE5_WRITE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    language1_speak = models.CharField(db_column='LANGUAGE1_SPEAK', max_length=5, blank=True, null=True)  # Field name made lowercase.
    language2_speak = models.CharField(db_column='LANGUAGE2_SPEAK', max_length=5, blank=True, null=True)  # Field name made lowercase.
    language3_speak = models.CharField(db_column='LANGUAGE3_SPEAK', max_length=5, blank=True, null=True)  # Field name made lowercase.
    language4_speak = models.CharField(db_column='LANGUAGE4_SPEAK', max_length=5, blank=True, null=True)  # Field name made lowercase.
    language5_speak = models.CharField(db_column='LANGUAGE5_SPEAK', max_length=5, blank=True, null=True)  # Field name made lowercase.
    language1_rlevel = models.CharField(db_column='LANGUAGE1_RLEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language2_rlevel = models.CharField(db_column='LANGUAGE2_RLEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language3_rlevel = models.CharField(db_column='LANGUAGE3_RLEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language4_rlevel = models.CharField(db_column='LANGUAGE4_RLEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language5_rlevel = models.CharField(db_column='LANGUAGE5_RLEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language1_wlevel = models.CharField(db_column='LANGUAGE1_WLEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language2_wlevel = models.CharField(db_column='LANGUAGE2_WLEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language3_wlevel = models.CharField(db_column='LANGUAGE3_WLEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language4_wlevel = models.CharField(db_column='LANGUAGE4_WLEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language5_wlevel = models.CharField(db_column='LANGUAGE5_WLEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language1_slevel = models.CharField(db_column='LANGUAGE1_SLEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language2_slevel = models.CharField(db_column='LANGUAGE2_SLEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language3_slevel = models.CharField(db_column='LANGUAGE3_SLEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language4_slevel = models.CharField(db_column='LANGUAGE4_SLEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language5_slevel = models.CharField(db_column='LANGUAGE5_SLEVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    yeargap_flag = models.CharField(db_column='YEARGAP_FLAG', max_length=5, blank=True, null=True)  # Field name made lowercase.
    yeargap1_years = models.CharField(db_column='YEARGAP1_YEARS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    yeargaps1_from = models.CharField(db_column='YEARGAPS1_FROM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    yeargaps1_to = models.CharField(db_column='YEARGAPS1_TO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    yeargap1_after_course = models.CharField(db_column='YEARGAP1_AFTER_COURSE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    yeargap1_reason = models.CharField(db_column='YEARGAP1_REASON', max_length=200, blank=True, null=True)  # Field name made lowercase.
    yeargap2_years = models.CharField(db_column='YEARGAP2_YEARS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    yeargaps2_from = models.CharField(db_column='YEARGAPS2_FROM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    yeargaps2_to = models.CharField(db_column='YEARGAPS2_TO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    yeargap2_after_course = models.CharField(db_column='YEARGAP2_AFTER_COURSE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    yeargap2_reason = models.CharField(db_column='YEARGAP2_REASON', max_length=200, blank=True, null=True)  # Field name made lowercase.
    backlog_flag = models.CharField(db_column='BACKLOG_FLAG', max_length=5, blank=True, null=True)  # Field name made lowercase.
    backlog_semesters = models.CharField(db_column='BACKLOG_SEMESTERS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    backlog_sem1 = models.CharField(db_column='BACKLOG_SEM1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    backlog_sem2 = models.CharField(db_column='BACKLOG_SEM2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    backlog_sem3 = models.CharField(db_column='BACKLOG_SEM3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    backlog_sem4 = models.CharField(db_column='BACKLOG_SEM4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    backlog_sem5 = models.CharField(db_column='BACKLOG_SEM5', max_length=5, blank=True, null=True)  # Field name made lowercase.
    backlog_sem6 = models.CharField(db_column='BACKLOG_SEM6', max_length=5, blank=True, null=True)  # Field name made lowercase.
    backlog_sem7 = models.CharField(db_column='BACKLOG_SEM7', max_length=5, blank=True, null=True)  # Field name made lowercase.
    backlog_sem8 = models.CharField(db_column='BACKLOG_SEM8', max_length=5, blank=True, null=True)  # Field name made lowercase.
    backlog_reason = models.CharField(db_column='BACKLOG_REASON', max_length=400, blank=True, null=True)  # Field name made lowercase.
    experience_flag = models.CharField(db_column='EXPERIENCE_FLAG', max_length=5, blank=True, null=True)  # Field name made lowercase.
    job1_years = models.CharField(db_column='JOB1_YEARS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    job1_designation = models.CharField(db_column='JOB1_DESIGNATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    job1_org = models.CharField(db_column='JOB1_ORG', max_length=200, blank=True, null=True)  # Field name made lowercase.
    job1_city = models.CharField(db_column='JOB1_CITY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    job1_role = models.CharField(db_column='JOB1_ROLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    job2_years = models.CharField(db_column='JOB2_YEARS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    job2_designation = models.CharField(db_column='JOB2_DESIGNATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    job2_org = models.CharField(db_column='JOB2_ORG', max_length=200, blank=True, null=True)  # Field name made lowercase.
    job2_city = models.CharField(db_column='JOB2_CITY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    job2_role = models.CharField(db_column='JOB2_ROLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    placement_status = models.CharField(db_column='PLACEMENT_STATUS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    slno = models.CharField(db_column='SLNO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    application_no = models.CharField(db_column='APPLICATION_NO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nativity = models.CharField(db_column='Nativity', max_length=500, blank=True, null=True)  # Field name made lowercase.
    if_physically_handicapped = models.CharField(db_column='If_Physically_Handicapped', max_length=500, blank=True, null=True)  # Field name made lowercase.
    in_case_of_emergency = models.CharField(db_column='In_Case_Of_Emergency', max_length=500, blank=True, null=True)  # Field name made lowercase.
    type_of_vechicle = models.CharField(db_column='Type_Of_Vechicle', max_length=500, blank=True, null=True)  # Field name made lowercase.
    name_of_vechicle = models.CharField(db_column='Name_Of_Vechicle', max_length=500, blank=True, null=True)  # Field name made lowercase.
    date_of_payment = models.CharField(db_column='Date_Of_Payment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mode_of_payment = models.CharField(db_column='Mode_Of_Payment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    challan_number = models.CharField(db_column='Challan_Number', max_length=500, blank=True, null=True)  # Field name made lowercase.
    professional_societies_meberships = models.CharField(db_column='professional_Societies_Meberships', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sports = models.CharField(db_column='Sports', max_length=500, blank=True, null=True)  # Field name made lowercase.
    social_service = models.CharField(db_column='Social_Service', max_length=500, blank=True, null=True)  # Field name made lowercase.
    international_national_state_university_awards = models.CharField(db_column='International_National_State_University_Awards', max_length=500, blank=True, null=True)  # Field name made lowercase.
    height = models.CharField(db_column='Height', max_length=500, blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=500, blank=True, null=True)  # Field name made lowercase.
    handicapped_reason = models.CharField(db_column='Handicapped_Reason', max_length=500, blank=True, null=True)  # Field name made lowercase.
    matregdno = models.CharField(db_column='MATREGDNO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    matscore = models.CharField(db_column='MATSCORE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    get10_applied = models.CharField(db_column='GET10_APPLIED', max_length=500, blank=True, null=True)  # Field name made lowercase.
    marital_status = models.CharField(db_column='MARITAL_STATUS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    temp_drno = models.CharField(db_column='TEMP_DRNO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    temp_area = models.CharField(db_column='TEMP_AREA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    temp_city = models.CharField(db_column='TEMP_CITY', max_length=500, blank=True, null=True)  # Field name made lowercase.
    temp_state = models.CharField(db_column='TEMP_STATE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    temp_pin = models.CharField(db_column='TEMP_PIN', max_length=500, blank=True, null=True)  # Field name made lowercase.
    temp_mobile = models.CharField(db_column='TEMP_MOBILE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    temp_telephone = models.CharField(db_column='TEMP_TELEPHONE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    temp_email = models.CharField(db_column='TEMP_EMAIL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    gd_pi_centre1 = models.CharField(db_column='GD_PI_CENTRE1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    gd_pi_centre2 = models.CharField(db_column='GD_PI_CENTRE2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    gd_pi_centre3 = models.CharField(db_column='GD_PI_CENTRE3', max_length=500, blank=True, null=True)  # Field name made lowercase.
    gd_pi_centre4 = models.CharField(db_column='GD_PI_CENTRE4', max_length=500, blank=True, null=True)  # Field name made lowercase.
    gd_pi_centre5 = models.CharField(db_column='GD_PI_CENTRE5', max_length=500, blank=True, null=True)  # Field name made lowercase.
    final_gd_pi_centre = models.CharField(db_column='FINAL_GD_PI_CENTRE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ssc_certificate = models.CharField(db_column='SSC_CERTIFICATE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    inter_certificate = models.CharField(db_column='INTER_CERTIFICATE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    graduation_certificate = models.CharField(db_column='GRADUATION_CERTIFICATE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pg_certificate = models.CharField(db_column='PG_CERTIFICATE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    from_date1 = models.CharField(db_column='FROM_DATE1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    to_date1 = models.CharField(db_column='TO_DATE1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    from_date2 = models.CharField(db_column='FROM_DATE2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    to_date2 = models.CharField(db_column='TO_DATE2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    organisation3 = models.CharField(db_column='ORGANISATION3', max_length=500, blank=True, null=True)  # Field name made lowercase.
    designation3 = models.CharField(db_column='DESIGNATION3', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nature_of_work3 = models.CharField(db_column='NATURE_OF_WORK3', max_length=500, blank=True, null=True)  # Field name made lowercase.
    from_date3 = models.CharField(db_column='FROM_DATE3', max_length=500, blank=True, null=True)  # Field name made lowercase.
    to_date3 = models.CharField(db_column='TO_DATE3', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dd_challan_cash_receipt_no = models.CharField(db_column='DD_CHALLAN_CASH_RECEIPT_NO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    date_of_issue = models.CharField(db_column='DATE_OF_ISSUE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(db_column='AMOUNT', max_length=500, blank=True, null=True)  # Field name made lowercase.
    writtentest_date = models.CharField(db_column='WRITTENTEST_DATE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    writtentest_marks = models.CharField(db_column='WRITTENTEST_MARKS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    written_qualified = models.CharField(db_column='WRITTEN_QUALIFIED', max_length=500, blank=True, null=True)  # Field name made lowercase.
    gd_marks = models.CharField(db_column='GD_MARKS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    gd_date = models.CharField(db_column='GD_DATE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pi_makrs = models.CharField(db_column='PI_MAKRS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pi_date = models.CharField(db_column='PI_DATE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    gd_qualified = models.CharField(db_column='GD_QUALIFIED', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pi_qualified = models.CharField(db_column='PI_QUALIFIED', max_length=500, blank=True, null=True)  # Field name made lowercase.
    seat_confirmed = models.CharField(db_column='SEAT_CONFIRMED', max_length=500, blank=True, null=True)  # Field name made lowercase.
    seat_confirmed_course = models.CharField(db_column='SEAT_CONFIRMED_COURSE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    seat_confirmed_date = models.CharField(db_column='SEAT_CONFIRMED_DATE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    self_add_envelops = models.CharField(db_column='SELF_ADD_ENVELOPS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    app_type = models.CharField(db_column='APP_TYPE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    medium = models.CharField(db_column='MEDIUM', max_length=500, blank=True, null=True)  # Field name made lowercase.
    cdl_elective = models.CharField(db_column='CDL_ELECTIVE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='SURNAME', max_length=500, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    social_status = models.CharField(db_column='SOCIAL_STATUS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='AREA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    salary = models.CharField(db_column='SALARY', max_length=500, blank=True, null=True)  # Field name made lowercase.
    total_service = models.CharField(db_column='TOTAL_SERVICE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ssc_regdno = models.CharField(db_column='SSC_REGDNO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    inter_regdno = models.CharField(db_column='INTER_REGDNO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    graduation_regdno = models.CharField(db_column='GRADUATION_REGDNO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pg_regdno = models.CharField(db_column='PG_REGDNO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    phd_regdno = models.CharField(db_column='PHD_REGDNO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ssc_elective = models.CharField(db_column='SSC_ELECTIVE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    inter_elective = models.CharField(db_column='INTER_ELECTIVE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    graduation_elective = models.CharField(db_column='GRADUATION_ELECTIVE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pg_elective = models.CharField(db_column='PG_ELECTIVE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    phd_elective = models.CharField(db_column='PHD_ELECTIVE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    phd_year = models.CharField(db_column='PHD_YEAR', max_length=500, blank=True, null=True)  # Field name made lowercase.
    phd_certificate = models.CharField(db_column='PHD_CERTIFICATE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    phd_board = models.CharField(db_column='PHD_BOARD', max_length=500, blank=True, null=True)  # Field name made lowercase.
    phd_class = models.CharField(db_column='PHD_CLASS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    phd_percentage = models.CharField(db_column='PHD_PERCENTAGE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    cdl_programme = models.CharField(db_column='CDL_PROGRAMME', max_length=500, blank=True, null=True)  # Field name made lowercase.
    cdl_feeyear = models.CharField(db_column='CDL_FEEYEAR', max_length=500, blank=True, null=True)  # Field name made lowercase.
    cdl_feebal = models.CharField(db_column='CDL_FEEBAL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    second_language = models.CharField(db_column='SECOND_LANGUAGE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    institute_last_studied = models.CharField(db_column='INSTITUTE_LAST_STUDIED', max_length=500, blank=True, null=True)  # Field name made lowercase.
    date_of_admission = models.DateTimeField(db_column='DATE_OF_ADMISSION', blank=True, null=True)  # Field name made lowercase.
    date_of_leaving = models.DateTimeField(db_column='DATE_OF_LEAVING', blank=True, null=True)  # Field name made lowercase.
    study_centre_opted = models.CharField(db_column='STUDY_CENTRE_OPTED', max_length=500, blank=True, null=True)  # Field name made lowercase.
    declaration = models.CharField(db_column='DECLARATION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(max_length=200, blank=True, null=True)
    experience = models.CharField(db_column='EXPERIENCE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    organisation1 = models.CharField(db_column='ORGANISATION1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    designation1 = models.CharField(db_column='DESIGNATION1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    exam_centre = models.CharField(db_column='EXAM_CENTRE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    fee_demand1 = models.IntegerField(db_column='FEE_DEMAND1', blank=True, null=True)  # Field name made lowercase.
    fee_demand2 = models.IntegerField(db_column='FEE_DEMAND2', blank=True, null=True)  # Field name made lowercase.
    fee_demand3 = models.IntegerField(db_column='FEE_DEMAND3', blank=True, null=True)  # Field name made lowercase.
    fee_demand4 = models.IntegerField(db_column='FEE_DEMAND4', blank=True, null=True)  # Field name made lowercase.
    fee_demand5 = models.IntegerField(db_column='FEE_DEMAND5', blank=True, null=True)  # Field name made lowercase.
    fee_demand6 = models.IntegerField(db_column='FEE_DEMAND6', blank=True, null=True)  # Field name made lowercase.
    entrance_year = models.CharField(db_column='ENTRANCE_YEAR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entrance_regdno = models.CharField(db_column='ENTRANCE_REGDNO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entrance_rank = models.CharField(db_column='ENTRANCE_RANK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entrance_marks = models.CharField(db_column='ENTRANCE_MARKS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entrance_board = models.CharField(db_column='ENTRANCE_BOARD', max_length=500, blank=True, null=True)  # Field name made lowercase.
    entrance_elective = models.CharField(db_column='ENTRANCE_ELECTIVE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    specialization1_code = models.CharField(max_length=500, blank=True, null=True)
    specialization1_desc = models.CharField(max_length=500, blank=True, null=True)
    sem1_year = models.CharField(max_length=50, blank=True, null=True)
    sem2_year = models.CharField(max_length=50, blank=True, null=True)
    sem3_year = models.CharField(max_length=50, blank=True, null=True)
    sem4_year = models.CharField(max_length=50, blank=True, null=True)
    sem5_year = models.CharField(max_length=50, blank=True, null=True)
    sem6_year = models.CharField(max_length=50, blank=True, null=True)
    sem7_year = models.CharField(max_length=50, blank=True, null=True)
    sem8_year = models.CharField(max_length=50, blank=True, null=True)
    pg_sem1_year = models.CharField(max_length=50, blank=True, null=True)
    pg_sem2_year = models.CharField(max_length=50, blank=True, null=True)
    pg_sem3_year = models.CharField(max_length=50, blank=True, null=True)
    pg_sem4_year = models.CharField(max_length=50, blank=True, null=True)
    pg_sem5_year = models.CharField(max_length=50, blank=True, null=True)
    pg_sem6_year = models.CharField(max_length=50, blank=True, null=True)
    pg_sem1_sgpa = models.CharField(max_length=50, blank=True, null=True)
    pg_sem2_sgpa = models.CharField(max_length=50, blank=True, null=True)
    pg_sem3_sgpa = models.CharField(max_length=50, blank=True, null=True)
    pg_sem4_sgpa = models.CharField(max_length=50, blank=True, null=True)
    pg_sem5_sgpa = models.CharField(max_length=50, blank=True, null=True)
    pg_sem6_sgpa = models.CharField(max_length=50, blank=True, null=True)
    pg_cgpa = models.CharField(max_length=50, blank=True, null=True)
    pg_year_from = models.CharField(max_length=5, blank=True, null=True)
    pg_course = models.CharField(max_length=50, blank=True, null=True)
    pg_specialization1 = models.CharField(max_length=50, blank=True, null=True)
    pg_specialization2 = models.CharField(max_length=50, blank=True, null=True)
    pg_institute = models.CharField(max_length=500, blank=True, null=True)
    pg_university = models.CharField(max_length=200, blank=True, null=True)
    pg_location = models.CharField(max_length=50, blank=True, null=True)
    ug_course = models.CharField(max_length=50, blank=True, null=True)
    ug_specialization1 = models.CharField(max_length=50, blank=True, null=True)
    ug_specialization2 = models.CharField(max_length=50, blank=True, null=True)
    ug_institute = models.CharField(max_length=500, blank=True, null=True)
    ug_university = models.CharField(max_length=200, blank=True, null=True)
    ug_location = models.CharField(max_length=50, blank=True, null=True)
    other1_course = models.CharField(max_length=50, blank=True, null=True)
    other1_specialization1 = models.CharField(max_length=50, blank=True, null=True)
    other1_specialization2 = models.CharField(max_length=50, blank=True, null=True)
    other1_institute = models.CharField(max_length=50, blank=True, null=True)
    other1_university = models.CharField(max_length=200, blank=True, null=True)
    other1_location = models.CharField(max_length=50, blank=True, null=True)
    other2_course = models.CharField(max_length=50, blank=True, null=True)
    other2_specialization1 = models.CharField(max_length=50, blank=True, null=True)
    other2_specialization2 = models.CharField(max_length=50, blank=True, null=True)
    other2_institute = models.CharField(max_length=50, blank=True, null=True)
    other2_university = models.CharField(max_length=200, blank=True, null=True)
    othe2r_location = models.CharField(max_length=50, blank=True, null=True)
    other1_joining_year = models.CharField(max_length=50, blank=True, null=True)
    other1_passed_year = models.CharField(max_length=50, blank=True, null=True)
    other1_cgpa = models.CharField(max_length=50, blank=True, null=True)
    other2_joining_year = models.CharField(max_length=50, blank=True, null=True)
    other2_passed_year = models.CharField(max_length=50, blank=True, null=True)
    other2_cgpa = models.CharField(max_length=50, blank=True, null=True)
    project1_title = models.CharField(max_length=150, blank=True, null=True)
    project1_org = models.CharField(max_length=150, blank=True, null=True)
    project1_duration = models.CharField(max_length=150, blank=True, null=True)
    project1_location = models.CharField(max_length=150, blank=True, null=True)
    project2_title = models.CharField(max_length=150, blank=True, null=True)
    project2_org = models.CharField(max_length=150, blank=True, null=True)
    project2_duration = models.CharField(max_length=50, blank=True, null=True)
    project2_location = models.CharField(max_length=150, blank=True, null=True)
    project3_title = models.CharField(max_length=150, blank=True, null=True)
    project3_org = models.CharField(max_length=150, blank=True, null=True)
    project3_duration = models.CharField(max_length=50, blank=True, null=True)
    project3_location = models.CharField(max_length=150, blank=True, null=True)
    ssc_class = models.CharField(db_column='SSC_CLASS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inter_class = models.CharField(db_column='INTER_CLASS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ug_class = models.CharField(db_column='UG_CLASS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pg_class = models.CharField(db_column='PG_CLASS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    placement_category = models.CharField(db_column='PLACEMENT_CATEGORY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    no_of_backlogs = models.CharField(db_column='NO_OF_BACKLOGS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    placement_grade = models.CharField(db_column='PLACEMENT_GRADE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(max_length=100, blank=True, null=True)
    student_opinion = models.CharField(max_length=1000, blank=True, null=True)
    higher_qualification = models.CharField(max_length=100, blank=True, null=True)
    feedback = models.CharField(max_length=500, blank=True, null=True)
    placement_percentage = models.FloatField(db_column='PLACEMENT_PERCENTAGE', blank=True, null=True)  # Field name made lowercase.
    previous_regdno = models.CharField(max_length=50, blank=True, null=True)
    biometric_id = models.CharField(max_length=25, blank=True, null=True)
    feedback_flag = models.CharField(db_column='FEEDBACK_FLAG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fee_demand_code = models.CharField(max_length=25, blank=True, null=True)
    part_payment_flag = models.CharField(db_column='PART_PAYMENT_FLAG', max_length=10, blank=True, null=True)  # Field name made lowercase.
    promoter_code = models.CharField(db_column='PROMOTER_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    exam_centre2 = models.CharField(db_column='EXAM_CENTRE2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    promoter_name = models.CharField(db_column='PROMOTER_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    promoter_mobile = models.CharField(db_column='PROMOTER_MOBILE', max_length=125, blank=True, null=True)  # Field name made lowercase.
    tally_flag = models.CharField(db_column='TALLY_FLAG', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tally_date = models.DateTimeField(db_column='TALLY_DATE', blank=True, null=True)  # Field name made lowercase.
    txn_flag = models.CharField(max_length=10, blank=True, null=True)
    txn_date = models.DateTimeField(blank=True, null=True)
    bec_score = models.CharField(db_column='BEC_Score', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tally_status = models.CharField(db_column='TALLY_STATUS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    parent_mobile = models.CharField(max_length=150, blank=True, null=True)
    tution_fee_arrears = models.FloatField(blank=True, null=True)
    tuition_fee = models.IntegerField(db_column='TUITION_FEE', blank=True, null=True)  # Field name made lowercase.
    lab_fee = models.IntegerField(db_column='LAB_FEE', blank=True, null=True)  # Field name made lowercase.
    special_fee = models.IntegerField(db_column='SPECIAL_FEE', blank=True, null=True)  # Field name made lowercase.
    internet_fee = models.IntegerField(db_column='INTERNET_FEE', blank=True, null=True)  # Field name made lowercase.
    dental_batch = models.CharField(db_column='DENTAL_BATCH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dental_student_type = models.CharField(db_column='DENTAL_STUDENT_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    sur_name = models.CharField(max_length=75, blank=True, null=True)
    first_name = models.CharField(max_length=75, blank=True, null=True)
    middle_name = models.CharField(max_length=75, blank=True, null=True)
    study_flag = models.CharField(db_column='STUDY_FLAG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tution_fee_arrears_due = models.CharField(max_length=50, blank=True, null=True)
    htno = models.CharField(db_column='HTNO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    previous_year = models.CharField(db_column='PREVIOUS_YEAR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tally_tution_fee_arrears = models.CharField(db_column='Tally_tution_fee_arrears', max_length=50, blank=True, null=True)  # Field name made lowercase.
    txn_flag1 = models.CharField(max_length=50, blank=True, null=True)
    txn_date1 = models.DateTimeField(blank=True, null=True)
    name_update_flag = models.CharField(db_column='NAME_UPDATE_FLAG', max_length=20, blank=True, null=True)  # Field name made lowercase.
    job_interest = models.CharField(db_column='JOB_INTEREST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    profile = models.CharField(db_column='PROFILE', max_length=510, blank=True, null=True)  # Field name made lowercase.
    file_type = models.CharField(db_column='FILE_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    preference_course_1 = models.CharField(db_column='PREFERENCE_COURSE_1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    preference_course_2 = models.CharField(db_column='PREFERENCE_COURSE_2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    preference_course_3 = models.CharField(db_column='PREFERENCE_COURSE_3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    preference_course_4 = models.CharField(db_column='PREFERENCE_COURSE_4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    preference_course_5 = models.CharField(db_column='PREFERENCE_COURSE_5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cattest = models.CharField(db_column='CATTEST', max_length=50, blank=True, null=True)  # Field name made lowercase.
    catregdno = models.CharField(db_column='CATREGDNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    catscore = models.CharField(db_column='CATSCORE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xattest = models.CharField(db_column='XATTEST', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xatregdno = models.CharField(db_column='XATREGDNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xatscore = models.CharField(db_column='XATSCORE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iifttest = models.CharField(db_column='IIFTTEST', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iiftregdno = models.CharField(db_column='IIFTREGDNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iiftscore = models.CharField(db_column='IIFTSCORE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mattest = models.CharField(db_column='MATTEST', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vehicle_number = models.CharField(db_column='Vehicle_Number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ug_percentage = models.CharField(db_column='UG_PERCENTAGE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    caste = models.CharField(db_column='Caste', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ssc_institute = models.CharField(db_column='SSC_INSTITUTE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inter_institute = models.CharField(db_column='INTER_INSTITUTE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sem_flag = models.CharField(max_length=10, blank=True, null=True)
    doj = models.DateTimeField(db_column='DOJ', blank=True, null=True)  # Field name made lowercase.
    feedback_branch = models.CharField(db_column='Feedback_Branch', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fine = models.IntegerField(db_column='FINE', blank=True, null=True)  # Field name made lowercase.
    color_blind = models.CharField(db_column='Color_Blind', max_length=20, blank=True, null=True)  # Field name made lowercase.
    eye_sight = models.CharField(db_column='Eye_sight', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date_crt = models.CharField(db_column='DATE_CRT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mode_payment_crt = models.CharField(db_column='MODE_PAYMENT_CRT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    amount_crt = models.CharField(db_column='AMOUNT_CRT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    payment_status = models.CharField(db_column='Payment_Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    course_name = models.CharField(db_column='COURSE_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branch_name = models.CharField(db_column='BRANCH_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    master_flag = models.CharField(db_column='MASTER_FLAG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    master_date = models.DateTimeField(db_column='MASTER_DATE', blank=True, null=True)  # Field name made lowercase.
    journal_flag = models.CharField(db_column='JOURNAL_FLAG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    journal_date = models.DateTimeField(db_column='JOURNAL_DATE', blank=True, null=True)  # Field name made lowercase.
    group_code = models.CharField(db_column='GROUP_CODE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fee_demand7 = models.IntegerField(db_column='FEE_DEMAND7', blank=True, null=True)  # Field name made lowercase.
    opening_balance = models.CharField(db_column='OPENING_BALANCE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    auditorium = models.CharField(db_column='AUDITORIUM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    seat = models.CharField(db_column='SEAT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    row = models.CharField(db_column='ROW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    doe_status = models.CharField(db_column='DOE_STATUS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    new_arrears = models.CharField(max_length=10, blank=True, null=True)
    virtualacno = models.CharField(max_length=16, blank=True, null=True)
    ibifsccode = models.CharField(max_length=16, blank=True, null=True)
    hostel_group = models.CharField(db_column='HOSTEL_GROUP', max_length=150, blank=True, null=True)  # Field name made lowercase.
    hostel_demand = models.FloatField(blank=True, null=True)
    notice_count = models.IntegerField(blank=True, null=True)
    parentnotice_count = models.IntegerField(blank=True, null=True)
    aadhar_no = models.CharField(db_column='AADHAR_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    int_status = models.CharField(max_length=1, blank=True, null=True)
    pan_card = models.CharField(db_column='Pan_Card', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STUDENT_MASTER'

class EmployeeMaster(models.Model):
    empid = models.CharField(db_column='EMPID', primary_key=True, max_length=25)  # Field name made lowercase.
    emp_name = models.CharField(db_column='EMP_NAME', max_length=500, blank=True,
                                null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(db_column='DESIGNATION', max_length=500, blank=True,
                                   null=True)  # Field name made lowercase.
    job_description = models.CharField(db_column='JOB_DESCRIPTION', max_length=500, blank=True,
                                       null=True)  # Field name made lowercase.
    father_name = models.CharField(db_column='FATHER_NAME', max_length=500, blank=True,
                                   null=True)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    doorno = models.CharField(db_column='DOORNO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=500, blank=True,
                                null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=500, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nation = models.CharField(db_column='NATION', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pincode = models.CharField(db_column='PINCODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='PHONE1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='PHONE2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=120, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    doj = models.DateTimeField(db_column='DOJ', blank=True, null=True)  # Field name made lowercase.
    exp_details = models.CharField(db_column='EXP_DETAILS', max_length=5000, blank=True,
                                   null=True)  # Field name made lowercase.
    phd_description = models.CharField(db_column='PHD_DESCRIPTION', max_length=5000, blank=True,
                                       null=True)  # Field name made lowercase.
    achievements = models.CharField(db_column='ACHIEVEMENTS', max_length=5000, blank=True,
                                    null=True)  # Field name made lowercase.
    specialization = models.CharField(db_column='SPECIALIZATION', max_length=5000, blank=True,
                                      null=True)  # Field name made lowercase.
    emp_type = models.CharField(db_column='EMP_TYPE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    panno = models.CharField(db_column='PANNO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pfno = models.CharField(db_column='PFNO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dept_name = models.CharField(db_column='DEPT_NAME', max_length=300, blank=True,
                                 null=True)  # Field name made lowercase.
    dept_code = models.CharField(db_column='DEPT_CODE', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    emp_status = models.CharField(db_column='EMP_STATUS', max_length=1, blank=True,
                                  null=True)  # Field name made lowercase.
    incharge_code = models.CharField(db_column='INCHARGE_CODE', max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.
    ssc_year = models.CharField(db_column='SSC_YEAR', max_length=15, blank=True,
                                null=True)  # Field name made lowercase.
    ssc_marks = models.CharField(db_column='SSC_MARKS', max_length=15, blank=True,
                                 null=True)  # Field name made lowercase.
    ssc_percentage = models.CharField(db_column='SSC_PERCENTAGE', max_length=15, blank=True,
                                      null=True)  # Field name made lowercase.
    ssc_board = models.CharField(db_column='SSC_BOARD', max_length=1000, blank=True,
                                 null=True)  # Field name made lowercase.
    inter_year = models.CharField(db_column='INTER_YEAR', max_length=15, blank=True,
                                  null=True)  # Field name made lowercase.
    inter_marks = models.CharField(db_column='INTER_MARKS', max_length=15, blank=True,
                                   null=True)  # Field name made lowercase.
    inter_percentage = models.CharField(db_column='INTER_PERCENTAGE', max_length=15, blank=True,
                                        null=True)  # Field name made lowercase.
    inter_board = models.CharField(db_column='INTER_BOARD', max_length=1000, blank=True,
                                   null=True)  # Field name made lowercase.
    degree_year = models.CharField(db_column='DEGREE_YEAR', max_length=15, blank=True,
                                   null=True)  # Field name made lowercase.
    degree_marks = models.CharField(db_column='DEGREE_MARKS', max_length=15, blank=True,
                                    null=True)  # Field name made lowercase.
    degree_percentage = models.CharField(db_column='DEGREE_PERCENTAGE', max_length=15, blank=True,
                                         null=True)  # Field name made lowercase.
    degree_university = models.CharField(db_column='DEGREE_UNIVERSITY', max_length=1000, blank=True,
                                         null=True)  # Field name made lowercase.
    pg_year = models.CharField(db_column='PG_YEAR', max_length=15, blank=True, null=True)  # Field name made lowercase.
    pg_marks = models.CharField(db_column='PG_MARKS', max_length=15, blank=True,
                                null=True)  # Field name made lowercase.
    pg_percentage = models.CharField(db_column='PG_PERCENTAGE', max_length=15, blank=True,
                                     null=True)  # Field name made lowercase.
    pg_university = models.CharField(db_column='PG_UNIVERSITY', max_length=1000, blank=True,
                                     null=True)  # Field name made lowercase.
    college_code = models.CharField(db_column='COLLEGE_CODE', max_length=25, blank=True,
                                    null=True)  # Field name made lowercase.
    campus = models.CharField(db_column='CAMPUS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    experience = models.CharField(max_length=5000, blank=True, null=True)
    bank_acno = models.CharField(db_column='BANK_ACNO', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    bank_name = models.CharField(db_column='BANK_NAME', max_length=500, blank=True,
                                 null=True)  # Field name made lowercase.
    job_status = models.CharField(db_column='JOB_STATUS', max_length=1, blank=True,
                                  null=True)  # Field name made lowercase.
    mgr_id = models.CharField(db_column='MGR_ID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    retired_flag = models.CharField(db_column='RETIRED_FLAG', max_length=1, blank=True,
                                    null=True)  # Field name made lowercase.
    retired_date = models.DateTimeField(db_column='RETIRED_DATE', blank=True, null=True)  # Field name made lowercase.
    emp_age = models.CharField(db_column='EMP_AGE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    gratuity_flag = models.CharField(db_column='GRATUITY_FLAG', max_length=1, blank=True,
                                     null=True)  # Field name made lowercase.
    gratuity_id = models.CharField(db_column='GRATUITY_ID', max_length=250, blank=True,
                                   null=True)  # Field name made lowercase.
    pfno_order = models.IntegerField(blank=True, null=True)
    marital_status = models.CharField(db_column='MARITAL_STATUS', max_length=500, blank=True,
                                      null=True)  # Field name made lowercase.
    father_occupation = models.CharField(db_column='FATHER_OCCUPATION', max_length=500, blank=True,
                                         null=True)  # Field name made lowercase.
    present_doorno = models.CharField(db_column='PRESENT_DOORNO', max_length=500, blank=True,
                                      null=True)  # Field name made lowercase.
    present_location = models.CharField(db_column='PRESENT_LOCATION', max_length=500, blank=True,
                                        null=True)  # Field name made lowercase.
    present_city = models.CharField(db_column='PRESENT_CITY', max_length=200, blank=True,
                                    null=True)  # Field name made lowercase.
    present_state = models.CharField(db_column='PRESENT_STATE', max_length=200, blank=True,
                                     null=True)  # Field name made lowercase.
    present_nation = models.CharField(db_column='PRESENT_NATION', max_length=200, blank=True,
                                      null=True)  # Field name made lowercase.
    present_pincode = models.CharField(db_column='PRESENT_PINCODE', max_length=150, blank=True,
                                       null=True)  # Field name made lowercase.
    phd_title = models.CharField(db_column='PHD_TITLE', max_length=550, blank=True,
                                 null=True)  # Field name made lowercase.
    phd_university = models.CharField(db_column='PHD_UNIVERSITY', max_length=150, blank=True,
                                      null=True)  # Field name made lowercase.
    phd_year = models.CharField(db_column='PHD_YEAR', max_length=150, blank=True,
                                null=True)  # Field name made lowercase.
    phd_percentage = models.CharField(db_column='PHD_PERCENTAGE', max_length=150, blank=True,
                                      null=True)  # Field name made lowercase.
    additional_qual_title = models.CharField(db_column='ADDITIONAL_QUAL_TITLE', max_length=150, blank=True,
                                             null=True)  # Field name made lowercase.
    additional_qual_university = models.CharField(db_column='ADDITIONAL_QUAL_UNIVERSITY', max_length=150, blank=True,
                                                  null=True)  # Field name made lowercase.
    additional_qual_year = models.CharField(db_column='ADDITIONAL_QUAL_YEAR', max_length=150, blank=True,
                                            null=True)  # Field name made lowercase.
    additional_qual_percentage = models.CharField(db_column='ADDITIONAL_QUAL_PERCENTAGE', max_length=150, blank=True,
                                                  null=True)  # Field name made lowercase.
    transport_vehicle = models.CharField(db_column='TRANSPORT_VEHICLE', max_length=150, blank=True,
                                         null=True)  # Field name made lowercase.
    transport_type = models.CharField(db_column='TRANSPORT_TYPE', max_length=150, blank=True,
                                      null=True)  # Field name made lowercase.
    transport_no = models.CharField(db_column='TRANSPORT_NO', max_length=150, blank=True,
                                    null=True)  # Field name made lowercase.
    service_in_gitam = models.CharField(db_column='SERVICE_IN_GITAM', max_length=150, blank=True,
                                        null=True)  # Field name made lowercase.
    outside_service = models.CharField(db_column='OUTSIDE_SERVICE', max_length=150, blank=True,
                                       null=True)  # Field name made lowercase.
    present_scale = models.CharField(db_column='PRESENT_SCALE', max_length=150, blank=True,
                                     null=True)  # Field name made lowercase.
    increment_date = models.DateTimeField(db_column='INCREMENT_DATE', blank=True,
                                          null=True)  # Field name made lowercase.
    promotion_date = models.DateTimeField(db_column='PROMOTION_DATE', blank=True,
                                          null=True)  # Field name made lowercase.
    desgn_before_promotion = models.CharField(db_column='DESGN_BEFORE_PROMOTION', max_length=150, blank=True,
                                              null=True)  # Field name made lowercase.
    desgn_after_promotion = models.CharField(db_column='DESGN_AFTER_PROMOTION', max_length=150, blank=True,
                                             null=True)  # Field name made lowercase.
    curr_post_totservice = models.CharField(db_column='CURR_POST_TOTSERVICE', max_length=150, blank=True,
                                            null=True)  # Field name made lowercase.
    transfer_date = models.DateTimeField(db_column='TRANSFER_DATE', blank=True, null=True)  # Field name made lowercase.
    from_establishment = models.CharField(db_column='FROM_ESTABLISHMENT', max_length=150, blank=True,
                                          null=True)  # Field name made lowercase.
    to_establishment = models.CharField(db_column='TO_ESTABLISHMENT', max_length=150, blank=True,
                                        null=True)  # Field name made lowercase.
    curr_establishment_totservice = models.CharField(db_column='CURR_ESTABLISHMENT_TOTSERVICE', max_length=150,
                                                     blank=True, null=True)  # Field name made lowercase.
    displinary_action_taken = models.CharField(db_column='DISPLINARY_ACTION_TAKEN', max_length=150, blank=True,
                                               null=True)  # Field name made lowercase.
    training_program1 = models.CharField(db_column='TRAINING_PROGRAM1', max_length=200, blank=True,
                                         null=True)  # Field name made lowercase.
    training_program2 = models.CharField(db_column='TRAINING_PROGRAM2', max_length=200, blank=True,
                                         null=True)  # Field name made lowercase.
    training_program3 = models.CharField(db_column='TRAINING_PROGRAM3', max_length=200, blank=True,
                                         null=True)  # Field name made lowercase.
    curriculam_activity1 = models.CharField(db_column='CURRICULAM_ACTIVITY1', max_length=200, blank=True,
                                            null=True)  # Field name made lowercase.
    curriculam_activity2 = models.CharField(db_column='CURRICULAM_ACTIVITY2', max_length=200, blank=True,
                                            null=True)  # Field name made lowercase.
    curriculam_activity3 = models.CharField(db_column='CURRICULAM_ACTIVITY3', max_length=200, blank=True,
                                            null=True)  # Field name made lowercase.
    health_problem = models.CharField(db_column='HEALTH_PROBLEM', max_length=300, blank=True,
                                      null=True)  # Field name made lowercase.
    strengths = models.CharField(db_column='STRENGTHS', max_length=300, blank=True,
                                 null=True)  # Field name made lowercase.
    weaknesses = models.CharField(db_column='WEAKNESSES', max_length=300, blank=True,
                                  null=True)  # Field name made lowercase.
    additional_info = models.TextField(db_column='ADDITIONAL_INFO', blank=True, null=True)  # Field name made lowercase.
    other_info = models.CharField(db_column='OTHER_INFO', max_length=500, blank=True,
                                  null=True)  # Field name made lowercase.
    subject = models.CharField(db_column='SUBJECT', max_length=500, blank=True, null=True)  # Field name made lowercase.
    incr_due_date = models.DateTimeField(db_column='INCR_DUE_DATE', blank=True, null=True)  # Field name made lowercase.
    service_ext_date = models.DateTimeField(db_column='SERVICE_EXT_DATE', blank=True,
                                            null=True)  # Field name made lowercase.
    desig_order = models.IntegerField(db_column='DESIG_ORDER', blank=True, null=True)  # Field name made lowercase.
    pf_flag = models.CharField(db_column='PF_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dt_time = models.DateTimeField(db_column='DT_TIME', blank=True, null=True)  # Field name made lowercase.
    nominee = models.CharField(db_column='NOMINEE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    nominee_relation = models.CharField(db_column='NOMINEE_RELATION', max_length=300, blank=True,
                                        null=True)  # Field name made lowercase.
    program_type = models.CharField(db_column='PROGRAM_TYPE', max_length=200, blank=True,
                                    null=True)  # Field name made lowercase.
    old_pfno = models.CharField(db_column='OLD_PFNO', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    qualification = models.CharField(db_column='QUALIFICATION', max_length=500, blank=True,
                                     null=True)  # Field name made lowercase.
    research = models.CharField(db_column='RESEARCH', max_length=5000, blank=True,
                                null=True)  # Field name made lowercase.
    email1 = models.CharField(db_column='EMAIL1', max_length=350, blank=True, null=True)  # Field name made lowercase.
    email2 = models.CharField(db_column='EMAIL2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    profile = models.CharField(db_column='PROFILE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    web_order = models.IntegerField(db_column='WEB_ORDER', blank=True, null=True)  # Field name made lowercase.
    imp_phone_flag = models.CharField(db_column='IMP_PHONE_FLAG', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    top_mgmt_flag = models.CharField(db_column='TOP_MGMT_FLAG', max_length=5, blank=True,
                                     null=True)  # Field name made lowercase.
    bom_web_order = models.IntegerField(db_column='BOM_WEB_ORDER', blank=True, null=True)  # Field name made lowercase.
    director_web_order = models.IntegerField(db_column='DIRECTOR_WEB_ORDER', blank=True,
                                             null=True)  # Field name made lowercase.
    emp_photo_path = models.CharField(db_column='EMP_PHOTO_PATH', max_length=350, blank=True,
                                      null=True)  # Field name made lowercase.
    emp_job_role = models.CharField(db_column='EMP_JOB_ROLE', max_length=500, blank=True,
                                    null=True)  # Field name made lowercase.
    content_type = models.CharField(db_column='CONTENT_TYPE', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    subjects_taught = models.CharField(max_length=1000, blank=True, null=True)
    web_dept_code = models.CharField(max_length=150, blank=True, null=True)
    web_dept_name = models.CharField(max_length=150, blank=True, null=True)
    web_college_code = models.CharField(max_length=25, blank=True, null=True)
    web_campus = models.CharField(max_length=25, blank=True, null=True)
    area_of_interest = models.CharField(max_length=2000, blank=True, null=True)
    placement_role = models.CharField(max_length=1, blank=True, null=True)
    placement_web_order = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    permanent_address = models.CharField(db_column='PERMANENT_ADDRESS', max_length=5000, blank=True,
                                         null=True)  # Field name made lowercase.
    present_address = models.CharField(db_column='PRESENT_ADDRESS', max_length=5000, blank=True,
                                       null=True)  # Field name made lowercase.
    religion = models.CharField(db_column='RELIGION', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    web_designation1 = models.CharField(db_column='WEB_DESIGNATION1', max_length=100, blank=True,
                                        null=True)  # Field name made lowercase.
    web_status = models.CharField(db_column='WEB_STATUS', max_length=10, blank=True,
                                  null=True)  # Field name made lowercase.
    ug_degree = models.CharField(db_column='UG_DEGREE', max_length=150, blank=True,
                                 null=True)  # Field name made lowercase.
    pg_degree = models.CharField(db_column='PG_DEGREE', max_length=150, blank=True,
                                 null=True)  # Field name made lowercase.
    phd_degree = models.CharField(db_column='PHD_DEGREE', max_length=150, blank=True,
                                  null=True)  # Field name made lowercase.
    mphil_degree = models.CharField(max_length=150, blank=True, null=True)
    mphil_year = models.CharField(max_length=150, blank=True, null=True)
    mphil_equivalent_university = models.CharField(max_length=150, blank=True, null=True)
    web_designation2 = models.CharField(db_column='WEB_DESIGNATION2', max_length=100, blank=True,
                                        null=True)  # Field name made lowercase.
    courses_taught_curr_yr = models.CharField(db_column='COURSES_TAUGHT_CURR_YR', max_length=500, blank=True,
                                              null=True)  # Field name made lowercase.
    nature_work = models.CharField(max_length=500, blank=True, null=True)
    post_doctoral_exp = models.CharField(db_column='POST_DOCTORAL_EXP', max_length=500, blank=True,
                                         null=True)  # Field name made lowercase.
    previous_experience_industrial = models.CharField(db_column='PREVIOUS_EXPERIENCE_INDUSTRIAL', max_length=500,
                                                      blank=True, null=True)  # Field name made lowercase.
    previous_experience_research = models.CharField(db_column='PREVIOUS_EXPERIENCE_RESEARCH', max_length=500,
                                                    blank=True, null=True)  # Field name made lowercase.
    previous_exp_teaching = models.CharField(db_column='PREVIOUS_EXP_TEACHING', max_length=500, blank=True,
                                             null=True)  # Field name made lowercase.
    membership_professional_societies = models.CharField(db_column='MEMBERSHIP_PROFESSIONAL_SOCIETIES', max_length=500,
                                                         blank=True, null=True)  # Field name made lowercase.
    additional_job_role = models.CharField(db_column='ADDITIONAL_JOB_ROLE', max_length=500, blank=True,
                                           null=True)  # Field name made lowercase.
    gitam_expirence = models.CharField(db_column='GITAM_EXPIRENCE', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.
    total_expirence = models.CharField(db_column='TOTAL_EXPIRENCE', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.
    pdf = models.CharField(max_length=50, blank=True, null=True)
    pdf_field = models.CharField(max_length=100, blank=True, null=True)
    pdf_university = models.CharField(max_length=50, blank=True, null=True)
    weekoff = models.CharField(db_column='WEEKOFF', max_length=5, blank=True, null=True)  # Field name made lowercase.
    aadhar_no = models.CharField(db_column='AADHAR_NO', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    last_update = models.DateTimeField(db_column='LAST_UPDATE', blank=True, null=True)  # Field name made lowercase.
    hit_count = models.IntegerField(db_column='HIT_COUNT', blank=True, null=True)  # Field name made lowercase.
    uan = models.CharField(db_column='UAN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fpf_flag = models.CharField(db_column='FPF_FLAG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ifsc_code = models.CharField(db_column='IFSC_CODE', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    job_type = models.CharField(db_column='JOB_TYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    aadhar_name = models.CharField(db_column='AADHAR_NAME', max_length=300, blank=True,
                                   null=True)  # Field name made lowercase.
    esi_no = models.CharField(db_column='ESI_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dor = models.DateTimeField(db_column='DOR', blank=True, null=True)  # Field name made lowercase.
    pwd = models.CharField(db_column='PWD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    selection_mode = models.CharField(db_column='SELECTION_MODE', max_length=25, blank=True,
                                      null=True)  # Field name made lowercase.
    additional_qualification = models.CharField(db_column='ADDITIONAL_QUALIFICATION', max_length=25, blank=True,
                                                null=True)  # Field name made lowercase.
    highest_qualification = models.CharField(db_column='Highest_Qualification', max_length=25, blank=True,
                                             null=True)  # Field name made lowercase.
    nature_appointment = models.CharField(db_column='Nature_Appointment', max_length=25, blank=True,
                                          null=True)  # Field name made lowercase.
    dojtp = models.CharField(db_column='DOJTP', max_length=25, blank=True, null=True)  # Field name made lowercase.
    resignation_flag = models.CharField(db_column='RESIGNATION_FLAG', max_length=5, blank=True,
                                        null=True)  # Field name made lowercase.
    hod_flag = models.CharField(db_column='HOD_FLAG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    web_job_description = models.CharField(db_column='WEB_JOB_DESCRIPTION', max_length=500, blank=True,
                                           null=True)  # Field name made lowercase.
    salutation = models.CharField(db_column='SALUTATION', max_length=10, blank=True,
                                  null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=150, blank=True,
                                  null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    web_designation3 = models.CharField(db_column='WEB_DESIGNATION3', max_length=100, blank=True,
                                        null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLOYEE_MASTER'


class GroupList(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    group_name = models.CharField(max_length=500, null=True, blank=True)
    group_email = models.CharField(max_length=500, null=True, blank=True)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(null=True, blank=True)


class WebApplication(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    application_name = models.CharField(max_length=500,null=True,blank=True)


class MobileApplication(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    application_name = models.CharField(max_length=500, null=True, blank=True)

class UploadImage(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    image = models.FileField('images/', blank=True, null=True)

class Dean(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    college = models.CharField(max_length=500, blank=True, null=True)
    stream = models.CharField(max_length=500, blank=True, null=True)

class PushNotification(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    role = models.CharField(max_length=20, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    data = models.TextField(null=True, blank=True)
    campus = models.TextField(null=True, blank=True)
    institute = models.TextField(null=True, blank=True)
    department = models.TextField(null=True, blank=True)
    group = models.TextField(null=True, blank=True)
    sent_by = models.CharField(max_length=10, null=True, blank=True)
    type = models.CharField(max_length=10, null=True, blank=True)
    is_web = models.BooleanField(default=False,null=True,blank=True)
    is_schedule = models.BooleanField(default=False,null=True,blank=True)
    attachments = models.FileField('attachments/',blank=True,null=True)
    scheduled_time = models.DateTimeField(null=True, blank=True)
    repeat_message = models.IntegerField(default=0, null=True, blank=True)
    dt_time = models.DateTimeField(null=True, blank=True, auto_now_add=True)


class PushNotificationStatus(models.Model):
    notification = models.ForeignKey(PushNotification, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    sub_category = models.CharField(max_length=20, blank=True, null=True)
    userid = models.CharField(max_length=16, null=True, blank=True)
    status = models.IntegerField(default=0,null=True,blank=True)
    dt_time = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    visibility = models.CharField(max_length=3,null=True, blank=True)
    visible_flag = models.BooleanField(default=True)
    role = models.CharField(max_length=2, null=True, blank=True)


class WebNotificationStatus(models.Model):
    notification = models.ForeignKey(PushNotification, on_delete=models.CASCADE, null=True, blank=True,related_name="web_notification")
    userid = models.CharField(max_length=500, null=True, blank=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    sub_category = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=False)
    dt_time = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    visibility = models.CharField(max_length=10,null=True, blank=True)
    visible_flag = models.BooleanField(default=True)
    role = models.CharField(max_length=2, null=True, blank=True)



class PushToken(models.Model):
    token = models.CharField(max_length=500, null=True, blank=True)
    userid = models.CharField(max_length=500, null=True, blank=True)
    role = models.CharField(max_length=1, null=True, blank=True)
    is_active = models.BooleanField(default=False)

class Directors(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
