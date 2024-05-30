from django.contrib.auth.models import BaseUserManager

class DoctorManager(BaseUserManager):

    def create_user(self, iin, phone_number, position, password):
        if not iin:
            raise ValueError('ИИН обязательное поле')
        if not phone_number:
            raise ValueError('Телефон обязательное поле')
        if not password:
            raise ValueError('Код обязательное поле')
        user = self.model(
            iin=iin,
            phone_number=phone_number,
            position=position,
            password=password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, iin, password, phone_number, position):
        user = self.create_user(
            iin=iin,
            phone_number= phone_number,
            position=position,
            password=password,
            
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        print(user)
  