from django.shortcuts import render
from ipywidgets.widgets.widget import register
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.register_read_message import ReadHoldingRegistersResponse
from .models import Hatlar, Panolar
from django import template


#KATODIK Modeller
def katodik(request):
    hathtml = Hatlar.objects.all()
    panohtml = Panolar.objects.all()
    return render (request, "katodik.html" ,{"hathtml":hathtml,
                                            "panohtml":panohtml})



#KATODIK Modbus
def katodikmodbus(request):
    client = ModbusTcpClient('192.168.204.13')
    client.connect()
    rawresponse = client.read_holding_registers(address=100,count=5,unit=1)
    response = rawresponse.registers
    ANV = response[0]/10
    ANA = response[1]/10
    BZV = response[2]
    TMP = response[3]/10
    client.close()
    return render(request, "katodikmodbus.html",{"ANA":ANA,"ANV":ANV,"BZV":BZV,"TMP":TMP})

def katodikizleme(request):
    return render (request, "katodikizleme.html")