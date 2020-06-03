from django.urls import path
from college import views

urlpatterns=[
    path('signup1/',views.signup1,name='signup1'),
    path('stdLogin/', views.stdLogin, name='stdLogin'),
    path('registration/',views.registration,name='registration'),
    path('teacherRegistration/',views.teacherRegistration,name='registration'),
    path('teacherLogin/',views.teacherLogin,name='login'),
    path('tDashboard/',views.tDashBoard,name='dashboard'),
    path('quiz/',views.quiz,name='quiz'),
    path('selectClass/',views.selectClass,name='selectClass'),
    path('attendanceForm/',views.attendanceForm,name='attendanceForm'),
    path('submitAttendance/',views.submitAttendance,name='submitAttendance'),
    path('payFee/',views.payFee,name='payFee'),
    path('handleRequest/', views.handleRequest, name='handleRequest'),
    #path('showAttendance/',views.showAttendance, name='showAttendance'),
    path('report/',views.report,name='report'),
    path('attendanceReport/',views.attendanceReport,name='attendanceReport'),
    path('quizResult/',views.quizResult,name='quizResult'),
    path('payFee1',views.payFee1,name='payFee1'),
    path('tLogout/',views.tLogout,name='tLogout'),
    path('stdLogout/', views.stdLogout, name='stdLogout'),
    path('stdAttend/', views.stdAttend, name='stdAttend'),
    path('viewStdAttend/', views.viewStdAttend, name='viewStdAttend'),
    path('change/', views.change, name='change'),
    path('forgotPassword/',views.forgotPassword,name='forgotPassword'),

]