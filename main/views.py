import datetime
from django.shortcuts import render

from .models import Bimbo


def home_page_view(request):
    nickname = request.GET.get("name")
    if nickname is not None:
        if nickname == "all":
            bimbi = Bimbo.objects.all()
            context = {
                "bimbi": bimbi
            }
            return render(request, "main/timbroCartelliniAll.html", context)

        else:
            print("Nome: " + str(nickname))
            today = datetime.datetime.now()
            print("Oggi: " + str(today))
            context = {
                "nickname": nickname,
                "today": today,
            }

            qs = Bimbo.objects.filter(nickname__icontains=nickname)
            print(qs)
            if qs.count() == 1:
                bimbo = qs.first()
                bimbo.num_incontri += 1
                bimbo.save()
                print(bimbo.nome, bimbo.nickname, bimbo.aggiunto, bimbo.num_incontri)
                context["bimbo"] = bimbo

            return render(request, "main/timbroCartelliniMod.html", context)
    return render(request, "main/timbroCartellini.html", {})
