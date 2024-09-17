from django.urls import path
from .views import (
    home,
    create_contact,
    get_all_contacts,
    contact_details,
    update_contact,
    delete_contact
)

urlpatterns = [
    path("", home, name="home"),
    path("create/", create_contact, name="create_contact"),
    path("all/", get_all_contacts, name="get_all_contacts"),
    path("details/<int:pk>", contact_details, name="contact_details"),
    path("update/<int:pk>", update_contact, name="update_contact"),
    path("delete/<int:pk>", delete_contact, name="delete_contact"),
]
