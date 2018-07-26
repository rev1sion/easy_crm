from django import forms
from django.contrib.auth.models import User
from firstapp.models import Company, CommentCompany, CompanyContact, CompanyObject
from firstapp.models import ObjectContact, CommentObject, CompanyObjectWork
from firstapp.models import ContactWork, CommentWork, DocumentWork

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['owner']

class CommentCompanyForm(forms.ModelForm):
    class Meta:
        model = CommentCompany
        fields = ('text',)
    
    prefix = 'comment'

class CompanyContactForm(forms.ModelForm):
    class Meta:
        model = CompanyContact
        exclude = ['company_contact', 'company_object_contact']
    
    prefix = 'contact'

class CompanyObjectForm(forms.ModelForm):
    class Meta:
        model = CompanyObject
        exclude = ['owner_obj', 'company']

    prefix = 'company_object'

class ObjectContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        object_id = kwargs.pop('object_id')
        super().__init__(*args, **kwargs)
        self.fields['object_contact'].queryset = CompanyContact.objects.filter(
            company_contact=CompanyObject.objects.get(id=object_id).company
        )
    class Meta:
        model = ObjectContact
        exclude = ['company_object']

    prefix = 'object_contact'

class CommentObjectForm(forms.ModelForm):
    class Meta:
        model = CommentObject
        fields = ('text',)

    prefix = 'object_comments'

class CompanyObjectWorkForm(forms.ModelForm):
    class Meta:
        model = CompanyObjectWork
        fields = ('user_work', 'work', 'status',)
    
    prefix = 'object_work'

class ContactWorkForm(forms.ModelForm):
    class Meta:
        model = ContactWork
        exclude = ['work']
    
    prefix = 'contact_work'

class CommentWorkForm(forms.ModelForm):
    class Meta:
        model = CommentWork
        fields = ('text',)

    prefix = 'comment_work'

class DocumentWorkForm(forms.ModelForm):
    class Meta:
        model = DocumentWork
        exclude = ['owner', 'work']

    prefix = 'document_work'

class CompanyObjectWorkStatusForm(forms.ModelForm):
    class Meta:
        model = CompanyObjectWork
        fields = ('status',)
    
    prefix = 'object_work'
