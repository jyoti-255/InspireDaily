from django.shortcuts import render
from requests import get

def home(request):
    if request.GET.get("btn"):
        try:
            url = "https://zenquotes.io/api/random"
            res = get(url)
            data = res.json()
            quote = data[0]["q"]
            author = data[0]["a"]
            
            return render(request, "home.html", {"msg": quote, "aut": author})
        except Exception as e:
            msg = "Issue: " + str(e)
            return render(request, "home.html", {"msg": msg, "aut": ""})
    else:
        return render(request, "home.html")


