from django.shortcuts import redirect, render
from myApp.models import candidateModel
def candidates(request):
    candidates=candidateModel.objects.all()
    candiDict={
        'candi':candidates,
    }
    return render(request, 'candidates.html', candiDict)

def addCandidates(request):
    if request.method=='POST':
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        address=request.POST.get('address')
        job_title=request.POST.get('job_title')
        linkedin_profile=request.POST.get('linkedin_profile')
        university=request.POST.get('university')
        degree=request.POST.get('degree')
        languages=request.POST.get('languages')
        years_of_experience=request.POST.get('years_of_experience')

        candidates=candidateModel(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            address=address,
            job_title=job_title,
            linkedin_profile=linkedin_profile,
            university=university,
            degree=degree,
            languages=languages,
            years_of_experience=years_of_experience

        )
        candidates.save()
        return redirect('candidates')
    return render(request, 'addCandidates.html')

def deleteCandi(request, myid):
    delCandi=candidateModel.objects.get(id=myid)
    delCandi.delete()
    return redirect('candidates')

def editCandi(request, myid):
    editCandi=candidateModel.objects.filter(id=myid)
    candiDict={
        'candiKey': editCandi
    }
    return render(request, 'editPage.html', candiDict)

def updateCandi(request):
    if request.method=='POST':
        myid=request.POST.get('id')
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        address=request.POST.get('address')
        job_title=request.POST.get('job_title')
        linkedin_profile=request.POST.get('linkedin_profile')
        university=request.POST.get('university')
        degree=request.POST.get('degree')
        languages=request.POST.get('languages')
        years_of_experience=request.POST.get('years_of_experience')

        candidates=candidateModel(
            id=myid,
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            address=address,
            job_title=job_title,
            linkedin_profile=linkedin_profile,
            university=university,
            degree=degree,
            languages=languages,
            years_of_experience=years_of_experience,
        )
        candidates.save()
        return redirect('candidates')

