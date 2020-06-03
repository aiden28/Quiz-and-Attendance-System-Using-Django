from django.urls import path
from owner import views

urlpatterns = [
    path('manage/',views.manage,name="manage"),
    path('addManageQuestion/', views.addManageQuestion,name='addManageQuestion'),
    path('addManageTest/',views.addManageTest,name='addManageTest'),
    path('addQuestion/',views.addQuestion,name='addQuestion'),
    path('doCreateTestPaper/',views.doCreateTestPaper,name='doCreateTestPapaer'),
    path('viewQuestion/', views.viewQuestion, name='viewQuestion'),
    path('viewTestPaper/',views.viewTestPaper,name='viewTestPaper'),
    path('user/',views.user,name='user'),
    path('userTest/',views.userTest,name="userTest"),
    path('description', views.description, name="description"),
    path('testResult/',views.testResult,name='testResult'),
    path('quizResult1/', views.quizResult1, name='quizResult1'),

]