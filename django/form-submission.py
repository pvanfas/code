
def registration(request):
    if request.method:

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        education = request.POST.get('education')
        message = request.POST.get('message')

        Registration.objects.create(
            name = name,
            email = email,
            phone = phone,
            dob = dob,
            education = education,
            message = message
        )

        return HttpResponse("Form Submitted")
    else:
        return HttpResponse("Invalid Request")
