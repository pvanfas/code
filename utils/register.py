import requests


def send_sms(number,message):
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=IMPSMS&message={}&language=english&route=p&numbers={}".format(message, number)
    headers = {
        'authorization': "API_KEY",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)



def register(request):
    if request.method == "POST":
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            if User.objects.filter(username=reg_form.cleaned_data.get('phone_number')).exists():
                response_data = {
                    "status": "false",
                    "title": "Already Registered",
                    "message": "Mobile number is already in use.",
                }
            else:
                reg_form.save()
                new_user = User.objects.create_user(
                    username=reg_form.cleaned_data.get('phone_number'),
                    password=reg_form.cleaned_data.get('password')
                )
                new_user.first_name = reg_form.cleaned_data.get('full_name')
                new_user.save()
                user = authenticate(request, username=reg_form.cleaned_data.get(
                    'phone_number'), password=reg_form.cleaned_data.get('password'))
                if user is not None:
                    login(request, user)
                message = "Thank you for registering for MSM HIGHSEC 2020.\nYour Login credentials are:\nUsername:{}\nPassword:{}\nContact: 8129206576\nTeam highsec 2k20".format(
                    reg_form.cleaned_data.get('phone_number'), reg_form.cleaned_data.get('password'))
                send_sms(reg_form.cleaned_data.get('phone_number'), message)

                response_data = {
                    "status": "true",
                    "title": "Success",
                    "message": "You have been successfully registered.",
                }
        else:
            print(reg_form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        reg_form = RegistrationForm()
        context = {
            "reg_form": reg_form,
        }
        return render(request, 'registration/registration.html', context)


def resend_password(request):
    if request.method == "POST":
        username = request.POST.get('phone_number')
        active_user = Registration.objects.get(phone_number=username)
        message = "\nYour username is {} and \npassword is {}. \n\n - Highsec Malappuram East".format(
            active_user.phone_number, active_user.password)
        send_sms(active_user.phone_number, message)
        response_data = {
            "status": "true",
            "title": "Success",
            "message": "Password instructions sent to your mobile.",
        }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {}
        return render(request, 'registration/resend_password.html', context)

