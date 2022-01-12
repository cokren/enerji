from django.db.models.sql.query import Query
from django.http import request
from django.shortcuts import render,HttpResponse,redirect
import pandas as pd
from .models import Arizalar, Jeneratorler, Tesisler, Periyodik, FiltreliBakim, Personel
import json
import plotly
import plotly.express as px


# JENERATÖR VE ARIZA TABLOSU
def jenerator(request):
    arizaicerik = Arizalar.objects.all()
    jenicerik = Tesisler.objects.raw('SELECT * FROM "jenerator_tesisler" LEFT OUTER JOIN "jenerator_jeneratorler" ON ("jenerator_tesisler"."id" = "jenerator_jeneratorler"."TESIS_id")')
    periyodikicerik = Periyodik.objects.all()
    filtreliicerik = FiltreliBakim.objects.all()
    personelicerik = Personel.objects.all()
    return render(request,"jenerator.html",{"jeneratorler":jenicerik, 
                                            "arizalar":arizaicerik, 
                                            "periyodik":periyodikicerik,
                                            "filtreli":filtreliicerik,
                                            "personel":personelicerik })
    

    

# JENERATÖR GRAFİK
def jengraph1(request):
    df1 = pd.DataFrame(list(Jeneratorler.objects.all().values("GUC")))
    df2 = pd.DataFrame(list(Tesisler.objects.all().values("TESIS_ADI")))
    frames = [df2,df1]
    df = pd.concat(frames,axis=1)
    df.sort_values(by=["GUC"],inplace=True,ascending=False)
    fig = px.bar(df, x="TESIS_ADI", y="GUC", color="TESIS_ADI", height=500, width=500, labels={"TESIS_ADI":"Tesisler","GUC":"Gücü"} )
    fig.update_layout(showlegend=False, 
                    paper_bgcolor="rgba(0, 0, 0, 0)",
                    margin_r=0,margin_t=5,margin_b=0,margin_l=0)    
    plot_div = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render(request, "jengraph1.html",{"plot_div":plot_div})



  