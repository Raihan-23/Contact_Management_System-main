from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contacts_manage
from .forms import ContactForm

# Create your views here.


def home(request):
    return HttpResponse(
        "Hello, This is the home page of the Contact Management System."
    )


# create contact


def create_contact(request):
    if request.method == "POST":
        create_form = ContactForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect("get_all_contacts")
        else:
            context = {
                "create_form": create_form,
            }
            return render(
                request, "contactsmanage/create_contact.html", context=context
            )
    else:
        create_form = ContactForm()
        context = {
            "create_form": create_form,
        }
        return render(request, "contactsmanage/create_contact.html", context=context)


# get all contact
def get_all_contacts(request):
    contacts = Contacts_manage.objects.all()
    # search for contacts by name or email
    context = {
        "contacts": contacts,
    }
    return render(request, "contactsmanage/get_all_contacts.html", context=context)


#contact details
def contact_details(request, pk):
    contact = Contacts_manage.objects.get(pk=pk)
    context = {
        "contact_details": contact,
    }
    return render(request, "contactsmanage/contact_details.html", context=context)



# update contact


def update_contact(request, pk):
    try:
        contact = Contacts_manage.objects.get(pk=pk)
        if request.method == "POST":
            update_form = ContactForm(request.POST, instance=contact)
            if update_form.is_valid():
                update_form.save()
                return redirect("get_all_contacts")
            else:
                context = {
                    "update_form": update_form,
                }
                return render(
                    request, "contactsmanage/update_contact.html", context=context
                )
        else:
            update_form = ContactForm(instance=contact)
            context = {
                "update_form": update_form,
            }
            return render(
                request, "contactsmanage/update_contact.html", context=context
            )
    except Contacts_manage.DoesNotExist:
        return redirect("get_all_contacts")
    

# delete contact 



def delete_contact(request, pk):
    try:
        contact = Contacts_manage.objects.get(pk=pk)
        contact.delete()
        return redirect("get_all_contacts")
    except Contacts_manage.DoesNotExist:
        return redirect("get_all_contacts")