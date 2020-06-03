from django.shortcuts import render,HttpResponse,redirect
from .models import Class,Student,Stream,Teacher,Attendance,Class,Fee
from owner.models import QuizResult
from django.core.mail import send_mail
import math,random
from datetime import date
from django.db.models import Max
from django.db import connection
from django.contrib import messages
#form django.contrib.sessions.models import Sessions
from django.views.decorators.csrf import csrf_exempt
from paytm import checksum
import uuid
MERCHANT_KEY='MI@S@raWJ@XK0UUw'


# Create your views here.
def signup1(request):
    dep=Stream.objects.all()
    return render(request,'index.html',{'obj':dep})
def quiz(request):
    if request.session.has_key('teacher'):
        return render(request,'test.html')
    else:
        return render(request, 'teacherLogin.html')


def registration(request):
    if request.method=='POST':

        obj=Student()
        x = date.today().year
        print(x)
        s=x%100
        a=request.POST.get('Class')
        b=request.POST.get('section')
        c_id=a+b+str(s)
        print(c_id)
        ob = Class.objects.get(id=c_id)
        print(ob.id)
        obj.class_id=ob

        obj.name=request.POST.get('name')
        obj.fatherName=request.POST.get('father_name')
        obj.motherName=request.POST.get('motherName')
        obj.address=request.POST.get('address')
        obj.Class=request.POST.get('Class')
        obj.section=request.POST.get('section')
        obj.prevClass=request.POST.get('prevClass')
        obj.prevClassMark=request.POST.get('prevClassMark')
        obj.prevResult=request.POST.get('prevResult')
        obj.gender=request.POST.get('gender')
        obj.image=request.POST.get('image')
        obj.stream=request.POST.get('stream')
        obj.dob=request.POST.get('dob')
        obj.department=request.POST.get('department')
        obj.rollno=request.POST.get('rollno')
        obj.password=request.POST.get('password')
        obj.save()

    return render(request, 'teacherLogin.html')

def viewStdAttend(request):
    if request.session.has_key('student'):
        return render(request,'viewStdAttend.html')
    else:
        return render(request,'stdLogin.html')






def teacherRegistration(request):
    return render(request,'techerRegestration.html')
def teacherLogin(request):
    if request.session.has_key('teacher'):
        return render(request,'tDashboard.html')
    else:
        return render(request,'teacherLogin.html')

def tDashBoard(request):
        id1=request.POST.get('id')
        pass1=request.POST.get('password')
        print(id1)
        print(pass1)
        try:
            obj=Teacher.objects.get(id=id1,password=pass1)
        except:
            a = '*Your Password Or User Id did not match'
            return render(request,'teacherLogin.html', {'a': a})
        #print(obj)
        #print(obj.password)
        request.session['teacher']=True
        return render(request,'tDashboard.html')


def selectClass(request):
    if request.session.has_key('teacher'):

        obj=Class.objects.all().aggregate(Max('id'))
        k=list(obj['id__max'])
        k.reverse()
        c=k[1]+k[0]
        ob=Class.objects.filter(id__contains=c).order_by('name')

        return render(request,'selectClass.html',{'ob':ob})
    else:
        return render(request,'teacherLogin.html')

def attendanceForm(request):
    classId=request.GET['class']
    #print(classId)
    obj=Student.objects.filter(class_id=classId)
    n=len(obj)
    l=range(n)
    data=zip(l,obj)
    #print(obj)
    return render(request,'attendanceForm.html',{'data':data,'n':n,'classId':classId})


def submitAttendance(request):
    n=request.POST.get('n')
    classId=request.POST.get('classId')

    #print(request.POST.get('absent0'))
    #print(classId)
    today=date.today()
    obj=Attendance()

    i=0
    while i < int(n):
        t = i
        k = 'roll' + str(t)
        z='absent' + str(t)
        roll = request.POST.get(k)
        ob1=Student.objects.get(rollno=roll)
        attn=request.POST.get(z)
        print(roll)
        print(attn)
        obj = Attendance()
        obj.rollno=ob1
        obj.status=attn
        obj.class_id=Class.objects.get(id=classId)
        obj.date=today
        obj.save()
        i += 1
    people = Attendance.objects.raw("select * from college_attendance")
    for p in people:
            print(p.rollno)
            print(p.date)
            print(p.status)
            print(p.class_id)


    return render(request, 'attendanceForm.html')


def report(request):
    if request.session.has_key('teacher'):
        obj=Class.objects.all().aggregate(Max('id'))
        k=list(obj['id__max'])
        k.reverse()
        c=k[1]+k[0]
        ob=Class.objects.filter(id__contains=c).order_by('name')
        return render(request,'showAttendance.html',{'ob':ob})
    else:
        return render(request,'teacherLogin.html')
#def report(request):



def attendanceReport(request):
    classId=request.GET['class']
    #print(classId)
    obj=Attendance.objects.filter(class_id=classId)
    #obj1 = Attendance.objects.filter(class_id=classId).values_list('rollno').distinct()
    print(obj)
    roll=[]
    name=[]
    for i in obj:
        if i.rollno.rollno not in roll:
            roll.append(i.rollno.rollno)

    k=[]
    roll.sort()
    print(roll)
    for i in roll:
        name.append(Student.objects.get(rollno=i).name)

        p=0
        a=0
        for j in obj:
            if j.rollno.rollno==i:
                if j.status=="Present":

                    p+=1
                else:
                    a+=1

        t=round(p*100/(p+a),2)
        k.append(t)
    print(k)
    print(name)
    data=zip(roll,name,k)
    print(data)
    #print(obj)
    return render(request,'attendanceReport.html',{'data':data})
###paytm:
a=''
rollno=''
def payFee(request):
    global a,rollno
    rollno=request.POST.get('rollno').upper()
    ab=request.POST.get('class_id')
    a=Class.objects.get(id=ab)
    print(request.session['class_id'])
    amt=request.POST.get('amt')
    x=uuid.uuid4().int
    print(rollno)
    print(amt)
    data_dict = {
        'MID': 'kyARft72081708900887',
        'ORDER_ID': str(x),
        #'rollno':rollno,
        #'Class':Class,
        'TXN_AMOUNT': amt,
        'CUST_ID': 'hasan',
        'INDUSTRY_TYPE_ID': 'Retail',
        'WEBSITE': 'WEBSTAGING',
        'CHANNEL_ID': 'WEB',
        'CALLBACK_URL':'http://127.0.0.1:8000/handleRequest/'
    }
    data_dict['CHECKSUMHASH']=checksum.generate_checksum(data_dict,MERCHANT_KEY)
    return  render(request,'paytm.html',{'data_dict':data_dict})

@csrf_exempt
def handleRequest(request):
    global a,rollno
    obj=Fee()
    #Paytm will send you post request here
    print(666)
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            Checksum = form[i]

    verify = checksum.verify_checksum(response_dict, MERCHANT_KEY, Checksum)
    if verify:

        obj.rollno=rollno
        obj.class_id=a
        obj.amount=response_dict['TXNAMOUNT']
        obj.orderId=response_dict['ORDERID']
        obj.txnId=response_dict['TXNID']
        obj.bankTxnId=response_dict['BANKTXNID']
        obj.txnDate=response_dict['TXNDATE']
        obj.mode='Online'
        obj.status=response_dict['RESPMSG']
        obj.save()
        print(response_dict['ORDERID'])
        print(a)
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})


def quizResult(request):
    if request.session.has_key('teacher'):
        return render(request,'quizResult.html')
    else:
        return render(request,'teacherLogin.html')
def payFee1(request):
    obj=Class.objects.all().aggregate(Max('id'))
    k=list(obj['id__max'])
    k.reverse()
    c=k[1]+k[0]
    ob=Class.objects.filter(id__contains=c).order_by('name')

    return render(request,'payFee.html',{'ob':ob})


def tLogout(request):
    request.session.flush()
    return redirect('home')

def stdLogin(request):
    if request.session.has_key('student'):
        return render(request, 'stdDashboard.html')

    elif request.method=='POST':
        rollno=request.POST.get('rollno').upper()
        psw=request.POST.get('password')
        print(rollno)
        print(psw)
        try:
            a=Student.objects.get(rollno=rollno,password=psw)
        except:


            m="Incorrect Credentials"
            return render(request,'stdLogin.html',{'m':m})
        request.session['student']=rollno
        return render(request, 'stdDashboard.html')



    else:

        return render(request,'stdLogin.html')

def stdLogout(request):
    print(request.session['student'])
    request.session.flush()
    return redirect('home')

def stdAttend(request):
    rollno1=request.GET['rollno'].upper()
    s=[]
    d=[]
    print(rollno1)
    ob=Student.objects.get(rollno=rollno1)
    name=ob.name
    obj=Attendance.objects.filter(rollno=ob)
    print(obj)
    p=0
    a=0
    for i in obj:
        d.append(i.date)
        s.append(i.status)
        if i.status=="Present":
            p+=1
        else:
            a+=1

    t=round(p*100/(p+a),2)
    n=range(len(obj))
    data=zip(n,s,d)
    print(d)
    return render(request,'attendance.html',{'data':data,'name':name,'p':t})

def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP
otp=''

def forgotPassword(request):
    global otp
    if request.method=='GET':
        otp = generateOTP()
        t=1
        send_mail(
            'hello hasan',
            'Otp for forgot password is '+otp+' valid for only 25 minutes',
            'raza01869@gmail.com',
            ['mohammadhasanraza128@gmail.com'],

        )

        return render(request,'forgotPassword.html')
    if request.method=='POST':
        otp1=request.POST.get('otp')
        pasw=request.POST.get('pass')
        print(otp)

        print(otp1)
        if otp==otp1:
            obj=Teacher.objects.get(id='100')
            obj.password=pasw
            obj.save()
            return redirect('change')
        else:
            m='otp is not valid'
            print(m)
            return render(request, 'forgotPassword.html',{'m':m})

def change(request):
    return render(request,'change.html')







