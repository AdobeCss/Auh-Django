from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from rolepermissions.roles import assign_role,get_user_roles
from .form import Form_add,Form_update
from rolepermissions.admin import roles 


def permissions_add(request):
      if request.method == 'POST':
        form = Form_add(request.POST)
        if form.is_valid():
            grupo_administrador, ContentType = Group.objects.get_or_create(name=request.POST.get('name'))
            return redirect(permissions_list)
        else:
            return HttpResponse('ouve um erro ao criar Permissão!')
    
      form = Form_add()
      return render(request, "permissions_add.html",{"form":form})
    
def permissions_rem(request,id):
        permission = roles.Group.objects.get(id=id)
        permission.delete()
        permissions = roles.Group.objects.all()
        return render(request, "permissions_index.html",{"permissions":permissions})


def permissions_update(request,id):
    permission = roles.Group.objects.get(id=id)
    if request.method == 'POST':
        form = Form_update(request.POST)
        if form.is_valid():
            grupo_administrador, ContentType = Group.objects.update_or_create(id=id, defaults={'name': request.POST.get('name')} )
            return redirect(permissions_list)
        else:
            return HttpResponse('ouve um erro ao criar Permissão!')
        
    form = Form_update(initial={'name':permission.name})
    return render(request, "permissions_update.html",{"form":form})
    

def permissions_list(request):
        permissions = roles.Group.objects.all()
        return render(request, "permissions_index.html",{"permissions":permissions})
