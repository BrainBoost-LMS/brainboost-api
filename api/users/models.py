import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, name, password):
        if not email:
            raise ValueError("The Email field must be set")
        uuid = str(uuid.uuid4())
        email = self.normalize_email(email)
        user = self.model(email=email, uuid=uuid, name=name, roleId=1)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    roleId = models.IntegerField(default=1)
    createdAt = models.DateTimeField(auto_now_add=True)
    deletedAt = models.DateTimeField(null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["uuid", "name", "roleId"]
    objects = UserManager()

    def __str__(self) -> str:
        return {"email": self.email, "name": self.name, "roleId":self.roleId}