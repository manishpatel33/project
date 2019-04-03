from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout as Logout, login as Login
from django.contrib.auth.models import User
from .models import student, teacher, teafollower, Comment, userprofile,\
    twit1, create_group, add_group_member, message, groupmessage
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.template.response import TemplateResponse


@login_required(login_url="/customapp/login/")
def index(request):
    return render(request, 'customapp/index.html')


def login(request):
    if request.session.has_key('username'):
        return redirect('/customapp/index')
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user:
            request.session['username'] = username
            Login(request, user)
            return redirect('/customapp/index')
        else:
            return HttpResponse("username or password not match")
    return render(request, "customapp/login.html")


def reg(request):
    if request.method == 'POST':
        hasher = PBKDF2PasswordHasher()
        b = User(username=request.POST['uname'],
                 email=request.POST['email'],
                 password=hasher.encode(password=request.POST['psw'],
                 salt='salt',
                 iterations=120000)
                 )

        email1 = User.objects.filter(email=b.email)
        name = User.objects.filter(username=b.username)
        if name:
            return HttpResponse("username alsready exist")
        if email1:
            return HttpResponse("email alsready exist")
        b.save()
        return redirect('/customapp/login/')
    return render(request, "customapp/reg.html")


@login_required(login_url="/customapp/login/")
def changepass(request):
    if request.method == 'POST':
        oldpass = request.POST['opsw']
        password = request.POST['psw']
        repassword = request.POST['Rpsw']
        username = request.user
        user = authenticate(username=username, password=oldpass)
        if password == repassword and user and user.username:
            user.set_password(password)
            user.save()
            return redirect('/customapp/login')
        else:
            if password == repassword:
                return HttpResponse('old password not match..')
            else:
                return HttpResponse('password and repassword not match')
    return render(request, "customapp/changepass.html")


def password_reset(request):
    if request.user.is_authenticated:
        return redirect('/customapp/index')
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['uname']
        user = User.objects.get(username=username)

        if email == user.email and username == user.username:
            send_mail(
                'Password reset on 127.0.0.1:8000',
                'http://127.0.0.1:8000/customapp/password_reset_confirm/',
                'webmaster@localhost',
                [email],
                fail_silently=False,
            )
            return redirect('/customapp/password_reset_done')
    return render(request, "customapp/password_reset.html")


def password_reset_confirm(request):
    if request.user.is_authenticated:
        return redirect('/customapp/index')
    if request.method == 'POST':
        username= request.POST['uname']
        password = request.POST['psw']
        repassword = request.POST['rpsw']
        user = User.objects.get(username=username)
        if password == repassword:
            user.set_password(password)
            user.save()
            return redirect('/customapp/password_reset_complete')
    return render(request, "customapp/password_reset_confirm.html")


def password_reset_complete(request):
    if request.user.is_authenticated:
        return redirect('/customapp/index')
    return render(request, "customapp/password_reset_complete.html")


def password_reset_done(request):
    if request.user.is_authenticated:
        return redirect('/customapp/index')
    return render(request, "customapp/password_reset_done.html")


@login_required(login_url="/customapp/login/")
def profile(request):
    return render(request, "customapp/profile.html")


def logout(request):
    if request.user.is_authenticated:
        del request.session['username']
        Logout(request)
        return redirect('/customapp/login')
    else:
        return HttpResponse("You have already logout")


@login_required(login_url="/customapp/login/")
def studentreg(request):
    if request.method == 'POST':
        b = student(Name=request.POST['uname'],
                    Email=request.POST['email'],
                    branch=request.POST['branch'])
        email1 = student.objects.filter(Email=b.Email)
        if email1:
            return HttpResponse("email allready exist")
        b.save()
        return redirect('/customapp/index')
    return render(request, "customapp/student.html")


@login_required(login_url="/customapp/login/")
def teacherreg(request):
    if request.method == 'POST':
        b = teacher(Name=request.POST['uname'],
                    Email=request.POST['email'],
                    branch=request.POST['branch'],
                    sub=request.POST['sub'])
        email1 = teacher.objects.filter(Email=b.Email)
        if email1:
            return HttpResponse("email alsready exist")
        b.save()
        return redirect('/customapp/index')
    return render(request, "customapp/teacher.html")


@login_required(login_url="/customapp/login/")
def updatestudent(request, id):
    u5 = student.objects.get(id=id)
    if request.method == 'POST':
        Name = request.POST['uname']
        Email = request.POST['email']
        branch = request.POST['branch']
        u5.Name = Name
        u5.Email = Email
        u5.branch = branch
        u5.save()
        return redirect('/customapp/index')
    return render(request, 'customapp/student.html', {'u5': u5})


@login_required(login_url="/customapp/login/")
def updateteacher(request, id):
    if not request.user.is_authenticated:
        return redirect('/customapp/login')
    else:
        u4 = teacher.objects.get(id=id)
        if request.method == 'POST':
            Name = request.POST['uname']
            Email = request.POST['email']
            sub = request.POST['branch']
            u4.Name = Name
            u4.Email = Email
            u4.sub = sub
            u4.save()
            return redirect('/customapp/index')
        return render(request, 'customapp/teacher.html', {'u4': u4})


@login_required(login_url="/customapp/login/")
def deletestudent(request, id):
    delete = student.objects.get(id=id)
    d1 = teafollower.objects.filter(student_id=id)
    delete.delete()
    for i in d1:
        i.delete()
    return redirect('/customapp/detail')


@login_required(login_url="/customapp/login/")
def deleteteacher(request, id):
    delete = teacher.objects.get(id=id)
    d1 = teafollower.objects.filter(teacher_id=id)
    delete.delete()
    for i in d1:
        i.delete()
    return redirect('/customapp/detail')


@login_required(login_url="/customapp/login/")
def detail(request):
    return render(request, "customapp/detail.html")


@login_required(login_url="/customapp/login/")
def showdata(request, id):
    event_list = student.objects.all()
    dis_stu = {'display_detail': event_list}

    event_list1 = teacher.objects.all()
    dis_tea = {'display_detail1': event_list1}
    if id == 1:
        return render(request, "customapp/detail.html", dis_stu)
    elif id == 2:
        return render(request, "customapp/detail.html", dis_tea)


@login_required(login_url="/customapp/login/")
def followpage(request, id):
    user = student.objects.get(id=id)
    student_id = id

    t2 = teafollower.objects.filter(student_id=student_id)
    t1 = teacher.objects.filter(branch=user.branch)

    list1 = []
    member_id = []

    for i in t1:
        for j in t2:
            if not i.id == j.teacher_id:
                list1.append(j.teacher_id)

        for i in t1:
            if i.id not in list1:
                member_id.append(i.id)

        return render(request, "customapp/detail.html", {'member_id': member_id, 't1': t1, 'student_id': student_id})


@login_required(login_url="/customapp/login/")
def studetails(request, id):
    u1 = student.objects.get(id=id)
    u11 = teafollower.objects.filter(student_id=id)
    u111 = Comment.objects.filter(student_id=id)
    return render(request, "customapp/detail.html", {'u1': u1, 'u11': u11, 'u111': u111})


@login_required(login_url="/customapp/login/")
def teadetails(request, id):
    u3 = teacher.objects.get(id=id)
    u33 = teafollower.objects.filter(teacher_id=id)
    u333 = student.objects.all()


def teadetail_response(request):
    response = TemplateResponse(request, "customapp/detail.html", {})
    response.add_post_render_callback(teadetails)


@login_required(login_url="/customapp/login/")
def teafollow(request, id, student_id):
    u6 = teacher.objects.get(id=id)
    b = teafollower(teacher_id=u6.id,
                    Name=u6.Name,
                    Email=u6.Email,
                    sub=u6.sub,
                    student_id=student_id
                    )
    t1 = teafollower.objects.filter(student_id=student_id)
    for i in t1:
        if i.student_id == b.student_id and i.teacher_id == b.teacher_id:
            return HttpResponse("allreadyfollow")
    b.save()
    return render(request, "customapp/detail.html", {'u6': u6})


@login_required(login_url="/customapp/login/")
def unfollow(request, id, student_id):
    delete = teafollower.objects.filter(teacher_id=id).filter(student_id=student_id)
    delete.delete()
    return redirect('/customapp/detail')


@login_required(login_url="/customapp/login/")
def comment123(request, id, student_id):
    u = teafollower.objects.filter(student_id=student_id).get(teacher_id=id)
    if request.method == 'POST':
        b = Comment(comment=request.POST['comment'],
                    student_id=u.student_id,
                    teacher_id=u.teacher_id)
        b.save()
        return redirect('/customapp/index')
    return render(request, "customapp/comment.html")


@login_required(login_url="/customapp/login/")
def showfollower(request, id):
    ufollow = User.objects.all().exclude(id=id)
    t1 = userprofile.objects.filter(user_id=id)

    list_id = []
    for i in t1:
        list_id.append(i.follower_id)

    de = {'ufollow': ufollow, 't1': t1, 'list_id': list_id}
    return render(request, 'customapp/profile.html', de)


@login_required(login_url="/customapp/login/")
def userfollow(request, id):
    u1 = User.objects.get(id=request.user.id)
    b1 = userprofile(
            Name=u1.username,
            Email=u1.email,
            user_id=request.user.id,
            requested_id=id,
            )
    b1.save()
    return redirect('/customapp/profile')


@login_required(login_url="/customapp/login/")
def userunfollow(request, id):
    delete = userprofile.objects.filter(follower_id=id).filter(user_id=request.user.id)
    delete.delete()
    return redirect('/customapp/profile')


@login_required(login_url="/customapp/login/")
def twit(request, id):
    u = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        b = twit1(
            Twit=request.POST['twit'],
            user_id=id,
            Email=u.email,
            Name=u.username
            )
        b.save()
        return redirect('/customapp/index')
    return render(request, "customapp/twit.html")


@login_required(login_url="/customapp/login/")
def selftwit(request, id):
    self2 = twit1.objects.all()
    return render(request, "customapp/profile.html", {'self2': self2})


@login_required(login_url="/customapp/login/")
def showtwit(request, id):
    record = twit1.objects.all().exclude(user_id=id)
    record2 = userprofile.objects.filter(user_id=id)
    record3 = twit1.objects.all()

    list1 = []
    for i in record2:
        list1.append(i.follower_id)

    list2 = []
    for j in record:
        if j.user_id in list1:
            list2.append(j.user_id)

    list3 = []
    for k in record3:
        if k.referenced_id == 0 and k.user_id in list2:
            list3.append(k.id)

    list4 = []
    for l in record3:
        list4.append(l.referenced_id)

    data = {'record': record, 'list3': list3, 'list2': list2, 'list4': list4}
    return render(request, "customapp/profile.html", data)


@login_required(login_url="/customapp/login/")
def followerdetail(request, id):
    user1 = User.objects.all()
    tweet1 = twit1.objects.filter(user_id=id)
    tweet2 = twit1.objects.all()
    follow = userprofile.objects.filter(user_id=id).exclude(follower_id=request.user.id)
    following = userprofile.objects.filter(user_id=request.user.id)

    list_following = []
    list_follow = []

    for i in follow:
        list_follow.append(i.follower_id)

    for j in following:
        list_following.append(j.follower_id)

    dis = {'user1': user1, 'tweet1': tweet1, 'tweet2': tweet2,
           'list_follow': list_follow, 'id': id, 'list_following': list_following}
    return render(request, "customapp/profile.html", dis)


@login_required(login_url="/customapp/login/")
def requestuser(request, id):
    r1 = userprofile.objects.filter(requested_id=id)
    msg = "NO REQUEST"
    return render(request, "customapp/profile.html", {'r1': r1, 'msg': msg})


@login_required(login_url="/customapp/login/")
def requestapprove(request, id):
    u = userprofile.objects.filter(user_id=id).get(requested_id=request.user.id)
    u.follower_id = request.user.id
    u.requested_id = 0
    u.save()
    return render(request, "customapp/profile.html")


@login_required(login_url="/customapp/login/")
def usercomment(request, Twit):
    d1 = twit1.objects.get(Twit=Twit)
    if request.method == 'POST':
        b = twit1(
            Twit=request.POST['comment'],
            user_id=request.user.id,
            Email=request.user.email,
            Name=request.user.username,
            referenced_id=d1.id,
            )
        b.save()
        return redirect('/customapp/profile')
    return render(request, "customapp/comment.html")


@login_required(login_url="/customapp/login/")
def creategroup(request, id):
    if request.method == 'POST':
        b = create_group(
                            group_name=request.POST['gn'],
                            admin_no=id,
                         )
        c1 = create_group.objects.filter(group_name=b.group_name)
        if c1:
            return HttpResponse("groupname alsready exist")
        b.save()
        return redirect('/customapp/profile/')
    return render(request, "customapp/create_group.html")


@login_required(login_url="/customapp/login/")
def add_member(request, id, group_name):
    c_g = userprofile.objects.filter(user_id=id)
    G_P = add_group_member.objects.filter(user_id=id)

    list_G_M = []
    for i in G_P:
        if i.group_name==group_name:
            list_G_M.append(i.member_no)

    user_group = User.objects.all()
    list_list = []
    for i in c_g:
        list_list.append(i.follower_id)
    d = {'user_group': user_group, 'list_list': list_list,
         'group_name': group_name, 'list_G_M': list_G_M}
    return render(request, "customapp/profile.html", d)


@login_required(login_url="/customapp/login/")
def showgroup(request, id):
    group = create_group.objects.filter(admin_no=id)
    return render(request, "customapp/profile.html", {'group': group})


@login_required(login_url="/customapp/login/")
def add_gr_member(request, mem_id, group_name):
    abc = create_group.objects.get(group_name=group_name)
    cre = add_group_member(user_id=abc.admin_no,
                           member_no=mem_id,
                           group_name=abc.group_name,
                           )
    cre.save()
    return render(request, "customapp/profile.html")


@login_required(login_url="/customapp/login/")
def message12(request, id):
    if request.method == 'POST':
        b = message(
            message=request.POST['msg'],
            mem_id=id,
            user_id=request.user.id,
        )
        b.save()
        return redirect('../../customapp/profile')
    return render(request, "customapp/message.html")


@login_required(login_url="/customapp/login/")
def showmessage(request, id):
    sm = message.objects.filter(mem_id=id)
    return render(request, "customapp/profile.html", {'sm': sm})


@login_required(login_url="/customapp/login/")
def groupmessage12(request, id):
    if request.method == 'POST':
        b = groupmessage(
            message=request.POST['gmsg'],
            user_id=request.user.id,
        )
        b.save()
        return redirect('../../customapp/profile')
    return render(request, "customapp/groupmessage.html")


@login_required(login_url="/customapp/login/")
def showgroupmessage(request, id):
    member = add_group_member.objects.filter(user_id=id)
    g_msg = groupmessage.objects.all()
    mem_list = []
    mem_list2 = []
    for i in member:
        mem_list.append(i.member_no)
        mem_list2.append(i.user_id)
    msg = {'g_msg': g_msg, 'mem_list': mem_list, 'mem_list2': mem_list2}
    return render(request, "customapp/profile.html", msg)


@login_required(login_url="/customapp/login/")
class Aboutview(TemplateView):
    template_name = "about.html"
