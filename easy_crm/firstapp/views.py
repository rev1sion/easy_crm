from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from firstapp.models import Company, CommentCompany, Account, CompanyContact, CompanyObject
from firstapp.models import ObjectContact, CommentObject, CompanyObjectWork
from firstapp.models import ContactWork, CommentWork, DocumentWork
from firstapp.forms import CompanyForm, CommentCompanyForm, CompanyContactForm, CompanyObjectForm
from firstapp.forms import ObjectContactForm, CommentObjectForm, CompanyObjectWorkForm, ContactWorkForm
from firstapp.forms import CommentWorkForm, DocumentWorkForm, CompanyObjectWorkStatusForm


# Create your views here.

def home(request):
    return redirect(izotoprk_account)

def izotoprk(request):
    return redirect(izotoprk_account)

@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_companys_detail(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    contact = CompanyContact.objects.filter(company_contact=company)
    comment = CommentCompany.objects.filter(company=company).order_by("-id")
    objects = CompanyObject.objects.filter(company=company)
    com_objects = CompanyObject.objects.filter(company=company).order_by("-id")

    if request.method == 'POST':
        form = CommentCompanyForm(request.POST, prefix='comment')
        contact_form = CompanyContactForm(request.POST, prefix='contact')
        objects_form = CompanyObjectForm(request.POST, prefix='company_object')

        if form.is_valid():
            comm = form.save(commit=False)
            comm.owner = request.user
            comm.company = company
            comm.save()
            return redirect('izotoprk-companys-detail', company_id=company.id)        

        if contact_form.is_valid():
            cont = contact_form.save(commit=False)
            cont.company_contact = company
            cont.save()
            return redirect('izotoprk-companys-detail', company_id=company.id)

        if objects_form.is_valid():
            obj = objects_form.save(commit=False)
            obj.owner_obj = request.user
            obj.company = company
            obj.save()
            return redirect('izotoprk-companys-detail', company_id=company.id)
    
    else:
        form = CommentCompanyForm()
        contact_form = CompanyContactForm()
        objects_form = CompanyObjectForm()
    
    return render(request, 'izotoprk/companys_detail.html', {
        'company': company, 'form': form, 
        'comment': comment, 'contact': contact, 
        'contact_form': contact_form,
        'objects':objects, 'objects_form': objects_form,
        'com_objects': com_objects
    })

@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_object_detail(request, object_id):
    objects = get_object_or_404(CompanyObject, id=object_id)
    comments = CommentObject.objects.filter(company_object=objects).order_by("-id")
    works = CompanyObjectWork.objects.filter(company_object=objects).order_by("-id")
    contacts_object = ObjectContact.objects.filter(company_object=objects).order_by("-id")
    if request.method == 'POST':
        object_contact_form = ObjectContactForm(request.POST, object_id=objects.id, prefix="object_contact")
        comment_form = CommentObjectForm(request.POST, prefix="object_comments")
        work_form = CompanyObjectWorkForm(request.POST, prefix="object_work")
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.owner = request.user
            comment.company_object = objects
            comment.save()
            

        if work_form.is_valid():
            work = work_form.save(commit=False)
            work.company_object = objects
            work.save()
            
        
        if object_contact_form.is_valid():
            cont = object_contact_form.save(commit=False)
            cont.company_object = objects
            cont.save()
        
        return redirect('izotoprk-object-detail', object_id=objects.id)

    else:
        comment_form = CommentObjectForm()
        work_form = CompanyObjectWorkForm()
        object_contact_form = ObjectContactForm(object_id=objects.id)

 
    return render(request, 'izotoprk/companys_objects_detail.html', {
        'objects': objects, 'comments': comments, 'comment_form': comment_form,
        'works': works, 'work_form': work_form, 'object_contact_form': object_contact_form,
        'contacts_object': contacts_object
    })

@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_work(request, work_id):
    work_detail = get_object_or_404(CompanyObjectWork, id=work_id)
    contacts = ContactWork.objects.filter(work=work_detail).order_by("-id")
    comments = CommentWork.objects.filter(work=work_detail).order_by("-id")
    documents = DocumentWork.objects.filter(work=work_detail).order_by("-id")
    
    if request.method == 'POST':
        contact_work_form = ContactWorkForm(request.POST, prefix='contact_work')
        comment_work_form = CommentWorkForm(request.POST, prefix='comment_work')
        documents_work_form = DocumentWorkForm(request.POST, request.FILES, prefix='document_work') 

        if contact_work_form.is_valid():
            contact_work = contact_work_form.save(commit=False)
            contact_work.work = work_detail
            contact_work.save()

        if comment_work_form.is_valid():
            comment_work = comment_work_form.save(commit=False)
            comment_work.owner = request.user
            comment_work.work = work_detail
            comment_work.save()
        
        if documents_work_form.is_valid():
            doc = documents_work_form.save(commit=False)
            doc.owner = request.user
            doc.work = work_detail
            doc.save()    

        return redirect('izotoprk-work', work_id=work_detail.id)    
        
     

    else:
        contact_work_form = ContactWorkForm()
        comment_work_form = CommentWorkForm()
        documents_work_form = DocumentWorkForm()

    return render(request, 'izotoprk/work.html', {
        'work_detail': work_detail, 'contacts': contacts, 
        'contact_work_form': contact_work_form,
        'comments': comments, 'comment_work_form': comment_work_form,
        'documents_work_form': documents_work_form, 'documents': documents
})    

@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_account(request):
    tasks = CompanyObjectWork.objects.filter(user_work=request.user).order_by("-id")
    zavershon = CompanyObjectWork.objects.filter(status='завершен')
    if zavershon:
        return render(request, 'izotoprk/account.html', {
    })
    return render(request, 'izotoprk/account.html', {
        'tasks':tasks
    })
    
    

@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_companys(request):
    companys = Company.objects.all().order_by("-id")
    form = CompanyForm()
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                company = form.save(commit=False)
                company.owner = request.user
                company.save()
                return redirect(izotoprk_companys)
    return render(request, 'izotoprk/companys.html', {
        'companys': companys, 'form': form
        })

@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_companys_edit(request, company_id):
    companys = get_object_or_404(Company, id=company_id)
    form = CompanyForm(instance = get_object_or_404(Company, id=company_id))
    if request.method == "POST":
        form = CompanyForm(request.POST, instance = get_object_or_404(Company, id=company_id))
        if form.is_valid():
            if request.user.is_authenticated():
                company = form.save()
                return redirect('izotoprk-companys-detail', company_id=companys.id)
    return render(request, 'izotoprk/companys_edit.html', {
        'form': form
        })

@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_object_edit(request, object_id):
    company_objects = get_object_or_404(CompanyObject, id=object_id)
    form = CompanyObjectForm(instance = get_object_or_404(CompanyObject, id=object_id))
    if request.method == "POST":
        form = CompanyObjectForm(request.POST, instance = get_object_or_404(CompanyObject, id=object_id))
        if form.is_valid():
            if request.user.is_authenticated():
                company_object = form.save()
                return redirect('izotoprk-object-detail', object_id=company_objects.id)
    return render(request, 'izotoprk/object_edit.html', {
        'form': form
        })

@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_work_edit(request, work_id):
    work_detail = get_object_or_404(CompanyObjectWork, id=work_id)
    form = CompanyObjectWorkForm(instance = get_object_or_404(CompanyObjectWork, id=work_id))
    if request.method == "POST":
        form = CompanyObjectWorkForm(request.POST, instance = get_object_or_404(CompanyObjectWork, id=work_id))
        if form.is_valid():
            if request.user.is_authenticated():
                object_work = form.save()
                return redirect('izotoprk-work', work_id=work_detail.id)
    return render(request, 'izotoprk/work_edit.html', {
        'form': form
        })

def izotoprk_contact_edit(request, contact_id):
    company_contact_edit = get_object_or_404(CompanyContact, id=contact_id)
    company_contact_form = CompanyContactForm(instance = get_object_or_404(CompanyContact, id=contact_id))
    if request.method == "POST":
        company_contact_form = CompanyContactForm(request.POST, instance = get_object_or_404(CompanyContact, id=contact_id))
        if company_contact_form.is_valid():
            if request.user.is_authenticated():
                object_work = company_contact_form.save()
                return redirect('izotoprk-companys-detail', company_id=company_contact_edit.company_contact.id)
    return render(request, 'izotoprk/company_contact_edit.html', {
        'company_contact_form': company_contact_form
        })

def izotoprk_contact_work_edit(request, contact_work_id):
    contact_work_edit = get_object_or_404(ContactWork, id=contact_work_id)
    contact_work_form = ContactWorkForm(instance = get_object_or_404(ContactWork, id=contact_work_id))
    if request.method == "POST":
        contact_work_form = ContactWorkForm(request.POST, instance = get_object_or_404(ContactWork, id=contact_work_id))
        if contact_work_form.is_valid():
            if request.user.is_authenticated():
                object_work = contact_work_form.save()
                return redirect('izotoprk-work', work_id=contact_work_edit.work.id)
    return render(request, 'izotoprk/contact_work_edit.html', {
        'contact_work_form': contact_work_form
        })

@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_work_status(request, work_id):
    work_detail = get_object_or_404(CompanyObjectWork, id=work_id)
    form = CompanyObjectWorkStatusForm(instance = get_object_or_404(CompanyObjectWork, id=work_id))
    if request.method == "POST":
        form = CompanyObjectWorkStatusForm(request.POST, instance = get_object_or_404(CompanyObjectWork, id=work_id))
        if form.is_valid():
            if request.user.is_authenticated():
                object_work = form.save()
                return redirect('izotoprk-work', work_id=work_detail.id)
    return render(request, 'izotoprk/work_status.html', {
        'form': form
        })


@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_companys_delete(request, company_id):
    try:
        company = get_object_or_404(Company, id=company_id)
        company.delete()
        return redirect(izotoprk_companys)
    except company.DoesNotExist:
        return redirect(izotoprk_companys)

@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_document_delete(request, doc_id):
    try:
        doc = get_object_or_404(DocumentWork, id=doc_id)
        doc.delete()
        return redirect('izotoprk-work', work_id=doc.work.id)
    except company.DoesNotExist:
        return redirect('izotoprk-work', work_id=doc.work.id)

@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_companys_objects(request):
    company_objects = CompanyObject.objects.all().order_by("-id")
    return render(request, 'izotoprk/companys_objects.html', {
        'company_objects': company_objects
    })

@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_in_work(request):
    in_work = CompanyObjectWork.objects.filter(status='в работе')
    return render(request, 'izotoprk/in_work.html', {
        'in_work': in_work
    })

@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_on_payment(request):
    on_payment = CompanyObjectWork.objects.filter(status='оплата')
    return render(request, 'izotoprk/on_payment.html', {
        'on_payment': on_payment
    })

@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_co_workers(request):
    accounts = Account.objects.all().order_by("-id")
    return render(request, 'izotoprk/co_workers.html', {
        'accounts':accounts
    })

@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_documents(request):
    documents = DocumentWork.objects.all().order_by("-id")
    return render(request, 'izotoprk/documents.html', {
        'documents': documents
    })

@login_required(login_url='/izotoprk/sign_in/')
def izotoprk_worker(request, worker_id):
    worker = get_object_or_404(Account, id=worker_id)
    tasks = CompanyObjectWork.objects.filter(user_work=worker.account_user).order_by("-id")
    zavershon = CompanyObjectWork.objects.filter(status='завершен')
    if zavershon:
        return render(request, 'izotoprk/account.html', {
    })
    return render(request, 'izotoprk/worker.html', {
        'worker': worker, 'tasks':tasks
    })
    
