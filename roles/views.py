from django.shortcuts import render
from django.contrib.auth.models import Permission,Group

def role_list(request,id):
        if request.method == "POST":
                permissionID = request.POST.get('role_id')
                GroupID = id
                pemission = Permission.objects.get(id=permissionID)
                group = Group.objects.get(id=GroupID)
                
                grupo_permissions = group.permissions.all()
                
                if pemission in grupo_permissions:
                   group.permissions.remove(pemission)    
                else:
                   group.permissions.add(pemission)
                
        grupo = Group.objects.get(id=id)
        grupo_permissions = grupo.permissions.all()
        permissions = Permission.objects.all()
        return render(request, "role_index.html",{"role":permissions,"group_permissions":grupo_permissions,"ID":id})
