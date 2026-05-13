from django.shortcuts import render, redirect, get_object_or_404
from ProjectOneApp.models import CandidateDataBases
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.


# This Functions for RegisterPage
def RegisterForm(request):
    if request.method == "POST":
        # if "submit" in request.POST:
        candi_name = request.POST["CandidateName"]
        email = request.POST["Email"]
        password = request.POST["Password"]
        conf_password = request.POST["ConfirmPassword"]
        con_number = request.POST["ContactNumber"]

        CandidatesInfo = CandidateDataBases(
            candidate_name=candi_name,
            email=email,
            password=password,
            confirm_password=conf_password,
            contact_number=con_number,
        )
        CandidatesInfo.save()
        return redirect("/loginpage/")

    # return to register page
    return render(request, "register.html")


# This Functions for LoginPage
def LoginData(request):
    if "login" in request.POST and request.method == "POST":
        email = request.POST.get("Email")
        password = request.POST.get("Password")

        user = CandidateDataBases.objects.filter(email=email, password=password).first()
        if user:
            request.session["user_id"] = user.id
            return redirect("/viewpage/")
        elif not user:
            return redirect("/loginpage/")
    # return to login page
    return render(request, "login.html")


# This Functions for Shows All Stored Data
def ViewAllData(request):
    search = request.GET.get("search")

    Civils = CandidateDataBases.objects.all()

    # 🔍 SEARCH LOGIC
    if search:
        Civils = Civils.filter(
            Q(candidate_name__icontains=search)
            | Q(email__icontains=search)
            | Q(contact_number__icontains=search)
        )

    # 📄 PAGINATION
    Pegi = Paginator(Civils, 5)
    Pages = request.GET.get("page")
    page_objects = Pegi.get_page(Pages)

    # 👤 LOGGED USER
    logged_user = None
    user_id = request.session.get("user_id")

    if user_id:
        logged_user = CandidateDataBases.objects.get(id=user_id)

    return render(
        request,
        "viewdata.html",
        {"Civils": page_objects, "logged_user": logged_user, "search": search},
    )


# Delete Data from Stored DataBases and Redirect to ViewPage
def DeleteData(request, id):
    CandidateDataBases.objects.get(id=id).delete()
    return redirect("/viewpage/")


# Edit Data from Existing DataBases and Redirect to RegisterPage for Editing
def EditData(request, id):
    Record = get_object_or_404(CandidateDataBases, id=id)

    if request.method == "POST":
        Record.candidate_name = request.POST.get("CandidateName")
        Record.email = request.POST.get("Email")
        Record.password = request.POST.get("Password")
        Record.confirm_password = request.POST.get("ConfirmPassword")
        Record.contact_number = request.POST.get("ContactNumber")
        Record.save()

        return redirect("/viewpage/")
    return render(request, "register.html", {"Record": Record})
