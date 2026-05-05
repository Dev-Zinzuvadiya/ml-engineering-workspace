from django.shortcuts import render, redirect, get_object_or_404
from ContactBookApp.models import DataBases
from django.core.paginator import Paginator

# Create your views here.


def RegisterPage(request):
    if request.method == "POST":
        regi_names = request.POST["Name"]
        regi_emails = request.POST["Email"]
        regi_pass = request.POST["Password"]
        regi_contact = request.POST["ContactNumber"]

        Informations = DataBases(
            names=regi_names,
            emails=regi_emails,
            passwords=regi_pass,
            contact_numbers=regi_contact,
        )
        Informations.save()
        return redirect("/login/")

    return render(request, "index1.html")


def LoginPage(request):
    if "login" in request.POST and request.method == "POST":
        email = request.POST.get("Email")
        password = request.POST.get("Password")

        user = DataBases.objects.filter(emails=email, passwords=password).first()
        if user:
            request.session["user_id"] = user.id
            return redirect("/oprator/")
        elif not user:
            return redirect("/login/")
    return render(request, "index2.html")


def OpratorPage(request):
    user_id = request.session.get("user_id")
    if user_id:
        logged_user = DataBases.objects.get(id=user_id)
    return render(request, "index3.html", {"logged_user": logged_user})


def ViewPage(request):
    user_id = request.session.get("user_id")
    logged_user = get_object_or_404(DataBases, id=user_id)

    RegisterDataBases = DataBases.objects.filter(owner=logged_user)

    return render(
        request,
        "index4.html",
        {"RegisterDataBases": RegisterDataBases, "logged_user": logged_user},
    )


def DeleteRecord(request, id):
    DataBases.objects.get(id=id).delete()
    return redirect("/view/")


def EditRecord(request, id):
    Record = get_object_or_404(DataBases, id=id)

    if request.method == "POST":
        Record.names = request.POST.get("Name")
        Record.emails = request.POST.get("Email")
        Record.passwords = request.POST.get("Password")
        Record.contact_numbers = request.POST.get("ContactNumber")

        Record.save()
        return redirect("/view/")

    return render(request, "index1.html", {"Record": Record})


def InsertRecords(request):
    user_id = request.session.get("user_id")
    logged_user = DataBases.objects.get(id=user_id)

    if request.method == "POST":
        DataBases.objects.create(
            owner=logged_user,
            names=request.POST["Name"],
            emails=request.POST["Email"],
            passwords=request.POST["Password"],
            contact_numbers=request.POST["ContactNumber"],
        )
        return redirect("/adminregister/")

    return render(request, "index5.html", {"logged_user": logged_user})
