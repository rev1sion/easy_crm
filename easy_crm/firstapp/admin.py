from django.contrib import admin
from firstapp.models import Company, CompanyObject, CompanyContact
from firstapp.models import CompanyObjectWork, Account, CommentCompany
from firstapp.models import CommentObject, ObjectContact, ContactWork, CommentWork
from firstapp.models import DocumentWork
# Register your models here.
admin.site.register(Company)
admin.site.register(CompanyObject)
admin.site.register(CompanyObjectWork)
admin.site.register(CompanyContact)
admin.site.register(CommentCompany)
admin.site.register(Account)
admin.site.register(CommentObject)
admin.site.register(ObjectContact)
admin.site.register(ContactWork)
admin.site.register(CommentWork)
admin.site.register(DocumentWork)