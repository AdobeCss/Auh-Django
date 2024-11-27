from rolepermissions.roles import AbstractUserRole

class Administrador(AbstractUserRole):
    avaliable_permissions = {'add_user':True,'read_user':True,'rem_user':True,'update_user':True}

class Funcionario(AbstractUserRole):
    avaliable_permissions = {'read_user':True,'rem_user':True}


