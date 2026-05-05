from django.shortcuts import render, redirect, get_object_or_404
from RegistrationApp.models import RecordsLength

# Create your views here.


def Registration(request):

    if "submit" in request.POST:
        candi_name = request.POST["CandidateName"]
        ages = request.POST["Age"]
        emails = request.POST["Email"]
        passwords = request.POST["Password"]
        conf_password = request.POST["ConfirmPassword"]

        # print(candi_name)
        # print(ages)
        # print(emails)
        # print(passwords)
        # print(conf_password)

        CivilianceInfo = RecordsLength(
            candidate_name=candi_name,
            age=ages,
            email=emails,
            password=passwords,
            confirm_password=conf_password,
        )
        CivilianceInfo.save()
        # print(">> Candidate Info Inserted Successfully..")

    return render(request, "registration.html")


def ShowData(request):
    CivilianceInfoShow = RecordsLength.objects.all()
    print(CivilianceInfoShow)

    return render(request, "viewdata.html", {"CivilianceInfoShow": CivilianceInfoShow})


def DeleteRecords(request, id):
    RecordsLength.objects.get(id=id).delete()
    return redirect("/ShowInfo/")


def EditRecords(request, id):
    record = get_object_or_404(RecordsLength, id=id)

    # print(record)

    if request.method == "POST":
        record.candidate_name = request.POST.get("CandidateName")
        record.age = request.POST.get("Age")
        record.email = request.POST.get("Email")

        record.password = request.POST.get("Password")
        record.confirm_password = request.POST.get("ConfirmPassword")

        record.save()
        return redirect("/ShowInfo/")

    return render(request, "registration.html", {"record": record})


# def ShowTables(request):
#     if request.method == "POST" and "ShowTable" in request.POST:
#         return redirect("/ShowInfo/")
