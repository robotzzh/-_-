from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import pymysql
import random
from .models import sc
# Create your views here.


def menu(request):
    template = "menu.html"
    # render(request,tempalate_name) 返回静态网页
    return render(request,'polls/menu.html',)


def insert_student(request):
    if request.method == 'GET':
        return render(request, 'polls/insert.html', )
    if request.method == 'POST':
        try:
            sno = request.POST['sc_sno']
            cno = request.POST['sc_cno']
            credit = request.POST['sc_credit']
            check_1 = int(sno)
            check_2 = int(cno)
            check_3 = int(credit)
            if check_1 < 0 or check_2 < 0 or check_3 < 0 or check_3 > 100:
                return render(request, "polls/e_insert.html", {'error': "range error"})
            # 名字对应前端form当中的name
            sc1 = sc(no=random.randint(0, 100000), sno=sno, cno=cno, credit=credit)
            sc1.save()
            # 保存来自前端的数据
            return render(request, "polls/s_insert.html")
        except Exception as e:
            # 任何问题都重新输入
            return render(request, "polls/e_insert.html", {'error': e})


def select_student(request):
    if request.method == 'GET':
        return render(request, 'polls/select.html',)
    if request.method == 'POST':
        try:
            str1 = ""
            sno = request.POST['sc_sno']
            data = sc.objects.filter(sno=sno)
            sum1 = 0
            for i in range(len(data)):
                str1 = str1 + "sno: "+str(data[i].sno)
                str1 = str1 + "cno: "+str(data[i].cno)
                str1 = str1 + "credit: "+str(data[i].credit)+"\n"
                sum1 += data[i].credit
            dict1 ={"show": str1, "average": sum1/len(data)}
            return render(request, 'polls/select_show.html', context=dict1)
        except Exception as e:
            return render(request, 'polls/e_select.html', {'error': e})


def delete_student(request):
    if request.method == 'GET':
        return render(request, 'polls/delete.html',)
    if request.method == 'POST':
        try:
            sno = request.POST['sc_sno']
            data = sc.objects.filter(sno=sno)
            data.delete()
            return render(request, 'polls/s_delete.html')
        except Exception as e:
            return render(request, 'polls/e_delete.html', {'error': e})


def alert_student(request):
    if request.method == 'GET':
        return render(request, 'polls/alert.html')
    if request.method == 'POST':
        try:
            sno = request.POST['sc_sno']
            cno = request.POST['sc_cno']
            credit = request.POST['sc_credit']
            data = sc.objects.filter(sno=sno, cno=cno)
            for i in data:
                i.credit = credit
                i.save()
            return render(request, 'polls/s_alert.html')
        except Exception as e:
            return render(request, 'polls/e_alert.html',{'error': e})