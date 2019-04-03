from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.template.response import TemplateResponse

urlpatterns = [
        path('index/', views.index, name='index'),
        path('login/', views.login, name='login'),
        path('reg/', views.reg, name='reg'),

        path('profile/', views.profile, name='profile'),

        path('student/', views.studentreg, name='student'),
        path('updatestudent/<int:id>', views.updatestudent, name='updatestudent'),
        path('deletestudent/<int:id>', views.deletestudent, name='deletestudent'),

        path('teacher/', views.teacherreg, name='teacher'),
        path('updateteacher/<int:id>', views.updateteacher, name='updateteacher'),
        path('deleteteacher/<int:id>', views.deleteteacher, name='deleteteacher'),

        path('detail/', views.detail, name='detail'),
        path('showdata/<int:id>', views.showdata, name='showdata'),

        path('follow/<int:id>', views.followpage, name='follow'),

        path('teadetails/<int:id>', views.teadetails, name='teadetails'),
        path('teafollow/<int:id>/<int:student_id>', views.teafollow, name='teafollow'),
        path('unfollow/<int:id>/<int:student_id>', views.unfollow, name='unfollow'),
        path('comment/<int:id>/<int:student_id>', views.comment123, name='comment'),

        path('showfollower/<int:id>', views.showfollower, name='showfollower'),
        path('userfollow/<int:id>', views.userfollow, name='userfollow'),
        path('userunfollow/<int:id>', views.userunfollow, name='userunfollow'),
        path('twit/<int:id>', views.twit, name='twit'),
        path('showtwit/<int:id>', views.showtwit, name='showtwit'),
        path('followerdetail/<int:id>', views.followerdetail, name="followerdetail"),
        path('requestuser/<int:id>', views.requestuser, name="requestuser"),
        path('requestapprove/<int:id>', views.requestapprove, name="requestapprove"),
        path('selftwit/<int:id>', views.selftwit, name="selftwit"),
        path('usercomment/<str:Twit>', views.usercomment, name="usercomment"),

        path('creategroup/<int:id>', views.creategroup, name='creategroup'),
        path('showgroup/<int:id>', views.showgroup, name='showgroup'),
        path('add_member/<int:id>/<str:group_name>', views.add_member, name='add_member'),
        path('add_group_member/<int:mem_id>/<str:group_name>', views.add_gr_member, name='add_group_member'),
        path('message/<int:id>', views.message12, name='message'),
        path('showmsg/<int:id>', views.showmessage, name='showmessage'),
        path('showgmsg/<int:id>', views.showgroupmessage, name='showgroupmessage'),
        path('groupmessage12/<int:id>', views.groupmessage12, name='groupmessage12'),

        path('about/', TemplateView.as_view(template_name="customapp/about.html")),
        path('studetails', TemplateView.as_view(template_name="customapp/detail.html")),
        path('logout/', views.logout, name='logout'),
]
