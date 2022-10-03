from tortoise import fields, models 
from tortoise.contrib.pydantic import pydantic_model_creator

class Users(models.Model):
  id             = fields.IntField(pk=True)
  username       = fields.CharField(max_length=20, unique=True)
  name           = fields.CharField(max_length=50, null=True)
  family_name    = fields.CharField(max_length=50, null=True)
  category       = fields.CharField(max_length=30, default="misc")
  ppassword_hash = fields.CharField(max_length=128, null=True)
  created_at     = fields.DatetimeField(auto_now_add=True)
  modified_at    = fields.DatetimeField(auto_now=True)

  def full_name(self) -> str: 
    """
    returns best name 
    """
    if self.name or self.family_name:
      return f"{self.name or ''} {self.family_name or ''}".strip()
    else:
      return self.username

User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)
