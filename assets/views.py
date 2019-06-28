from django.shortcuts import render
import sqlite3
from assets import models


# Create your views here.
def get_data(sql):#获取数据库的数据
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall() # 搜取所有结果
    cur.close()
    conn.close()
    return results

def server(request):

    sql = "select hostname,ip_addr from assets_server"      # t为表名
    m_data = get_data(sql)
    return render(request, 'assets/server.html', {'server':m_data})

def show(request):

    if request.method == 'POST':
        hostname = request.POST['a_hostname']
        ip_addr = request.POST['a_ip_addr']
        models.Server.objects.create(hostname=hostname, ip_addr=ip_addr)

    server_list = models.Server.objects.all()

    return render(request, 'assets/show.html', {'server_list':server_list})