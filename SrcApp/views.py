from django.shortcuts import render
import json
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    context = {}

    return render(request, 'index.html', context)


def send_get_quote_email(request):
    message = None
    request_body = json.loads(request.body)
    contact = request_body.get('contact')
    customer_name = request_body.get('name')

    if customer_name == None:
        customer_name = 'Name Not Specified'

    tv_size = request_body.get('tv_size')
    mount_type = request_body.get('mount_type')
    add_ons = request_body.get('add_ons')
    wires_condition = request_body.get('wires')
    wall_type = request_body.get('wall_type')

    if contact is not None and contact != '':
        subject = f"Quote Request"
        message = f"You have a Quote request from {customer_name}, phone number: {contact},  TV Size : {tv_size},  Mount Type : {mount_type},  Wiring Treatment  : {wires_condition},  Wall Type  : {wall_type}. Add-Ons :  {add_ons}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['pacoqara@gmail.com']

        send_mail(subject, message, from_email, recipient_list)

        message = 'success'
    if contact is None:
        message = 'error'

    return JsonResponse({'message': message})


def send_phone_number_email(request):
    message = None
    try:
        request_body = json.loads(request.boyd)
        phone = request_body.get('phone')
        name = request_body.get('name')

        if name is None:
            name = 'Name Not Specified'
        subject = f"Quote Request"
        message = f"You have a Quote request from {name}, phone number: {phone}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['pacoqara@gmail.com']

        send_mail(subject, message, from_email, recipient_list)
        message = 'success'


    except Exception as e:
        print(e)
        message = 'error'

    return JsonResponse({'message': message})