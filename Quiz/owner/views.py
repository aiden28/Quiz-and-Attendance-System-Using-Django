from django.shortcuts import render, redirect
import random
from .forms import QuestionForm
from .models import ManageQuestion,TestQuestion,Test,QuizResult3,QuizResult
from django.db import connection
from django.contrib import messages


# Create your views here.
def manage(request):
    if request.session.has_key('teacher'):
        return render(request, "test.html")
    else:
        return render(request,'teacherLogin.html')


def addManageQuestion(request):
    if request.session.has_key('teacher'):

        if request.method == "POST":
            ca=request.POST.get('correct_answer')
            ca='option_'+ca
            mq=ManageQuestion()
            mq.question=request.POST.get('question')
            mq.option_a = request.POST.get('option_a')

            mq.option_b = request.POST.get('option_b')
            mq.option_c=request.POST.get('option_c')
            mq.option_d=request.POST.get('option_d')
            mq.subject = request.POST.get('subject')
            mq.correct_answer = request.POST.get(ca)
            mq.save()
            return redirect('manage')
        else:
            form=QuestionForm()
            return render(request,'manage.html',{'form':form})
    else:
        return render(request,'teacherLogin.html')




def addQuestion(request):
    subject1=request.GET['subject']
    obj = ManageQuestion.objects.filter(subject=subject1)
    que=[]
    id=[]
    for i in obj:
        id.append(i.id)
        que.append(i.question)
    n=range(len(obj))
    data=zip(id,que,n)


    return render(request,'addQuestion.html',{'data':data,'postLen':len(que)})


def coloumnExist(today):
    for field in QuizResult3._meta.get_fields(include_hidden=True):
        print(field)
        if field.name == today:
            return True
    return False
def addManageTest(request):
    if request.session.has_key('teacher'):

        #subject=ManageQuestion.AsEnumrable().Select(s = >s.Field<string>("subject"))
        subject1=ManageQuestion.objects.values_list('subject',flat=True).distinct()

        cursor = connection.cursor()
        #a="2012"
        #cursor.execute('ALTER TABLE owner_quizResult3 add %s varchar(3)' %a)

        #cursor.execute("insert into owner_quizResult3 (rollno,%s) values('14cs2628','2230')"%a)
        #people = QuizResult3.objects.raw('select id,%s from owner_quizResult3' %a)
        #print(people)
        #for p in people:


            #print(p.rollno)
            #print(p.b2012)
           # print(getattr(p,a,'jjj'))
        a=coloumnExist('today')
        print(a)
        return render(request,'manageTest.html',{'subject':subject1})
    else:
        render(request,'teacherLogin.hml')



def doCreateTestPaper(request):
    li=[]

    n=int(request.POST.get('postLen'))
    timer1=int(request.POST.get("timer"))
    password1=request.POST.get("password")
    id=request.POST.get("id")


    for i in range(n):
        index="ques"+str(i)
        print(index)
        print(request.POST.get(index))
        print(request.POST.get("ques1"))
        if request.POST.get(index)!=None:
            print(request.POST.get(index))
            li.append(request.POST.get(index))
    obj = ManageQuestion.objects.get(id=li[0])
    subject1 = obj.subject


    print(type(li[0]))
    q=Test(id=id,subject=subject1,timer=timer1,password=password1)
    q.save()
    maxId=Test.objects.all().order_by("-id")[0]
    for i in li:
        q1=TestQuestion(queId=ManageQuestion.objects.get(id=int(i)),testId=maxId)
        q1.save()

    return render(request, 'test.html')

def viewQuestion(request):
    if request.session.has_key('teacher'):

        obj=ManageQuestion.objects.all()
        return render(request, 'viewQuestion.html',{'obj':obj})
    else:
        render(request,'teacherLogin.html')

def viewTestPaper(request):
    if request.session.has_key('teacher'):

        l1=[]
        l2=[]
        l3=[]
        obj=Test.objects.all()

        for i in obj:
            l1.append(i.id)
            l2.append(i.subject)
            obj1=TestQuestion.objects.filter(testId=i.id)
            l3.append(len(obj1))
        print(l1)
        print(l2)
        print(l3)
        data=zip(l1,l2,l3)
        return render(request,'testPaper.html',{'data':data})

    else:
        render(request,'teacherLogin.html')

def user(request):
    if request.session.has_key('student'):
        return render(request,'testLogin.html')
    else:
        return render(request,'stdLogin.html')

def userTest(request):
    if request.session.has_key('student'):

        id=[]
        q=[]
        a=[]
        b=[]
        c=[]
        d=[]
        l=[]
        id1=request.POST.get('paperId')
        print(id1)
        obj0=Test.objects.get(id=id1)
        t=int(obj0.timer)
        print(type(t))
        obj=TestQuestion.objects.filter(testId=id1)
        obj=list(obj)
        random.shuffle(obj)
        for i in obj:
            qu=ManageQuestion.objects.get(id=(i.queId).id)   #queId is foreignkey objectof question.
            id.append(qu.id)
            q.append(qu.question)
            l.append(qu.option_a)
            l.append(qu.option_b)
            l.append(qu.option_c)
            l.append(qu.option_d)

            random.shuffle(l)

            a.append(l[0])
            b.append(l[1])
            c.append(l[2])
            d.append(l[3])
            l.clear()

        n=range(1,len(obj)+1)
        for i in n:
            print(i)
        data=zip(n,id,q,a,b,c,d)
        print(data)
        return render(request,'userTest.html',{'data':data,'n':len(obj),'paperId':id1,'t':t})
    else:
        return render(request,'stdLogin.html')



def description(request):
    if request.session.has_key('student'):
        paperId=request.POST.get('id')
        password1=request.POST.get('password')
        try:
            obj=Test.objects.get(id=paperId,password=password1)
        except:

            a = '*Your Password Or TestId did not match'
            return render(request, 'testLogin.html', {'a': a})


        return render(request, 'description.html',{'id':paperId})
    else:
        return render(request,'stdLogin.html')

def testResult(request):
    if request.session.has_key('student'):
        n = int(request.POST.get('x'))
        paperId = request.POST.get('paperId')
        rollno = request.session['student']
        r=0
        na=0
        for i in range(1,n+1):
            id1= int(request.POST.get('que'+str(i)))
            option = request.POST.get('option' + str(i))
            obj = ManageQuestion.objects.get(id=id1)

            if option==None:
                na+=1

            if option==obj.correct_answer:
                r+=1
        print(paperId)

        obj=QuizResult()
        obj.rollno=rollno
        obj.testId=paperId
        obj.marks=r
        obj.save()
        return render(request,'thanku.html',{'a':n-na,'na':na,'r':r})
    else:
        return render(request,'stdLogin.html')




def quizResult1(request):
    testId=request.GET['class']
    print(testId)
    ob=QuizResult.objects.filter(testId=testId)
    s=range(1,len(ob)+1)
    r=[]
    m=[]
    for i in ob:
        r.append(i.rollno)
        m.append(i.marks)
    data=zip(s,r,m)
    print(ob)
    return render(request,'quizResultProcess.html',{'data':data,'testId':testId})