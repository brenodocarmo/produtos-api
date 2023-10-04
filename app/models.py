from django.db import models

class Group(models.Model):
    cod_status = [
        ("A", "Ativo"),
        ("I", "Inativo")
    ]

    cod_gpr = models.CharField(max_length=3, primary_key=True)
    desc_gpr = models.TextField()
    situ_gpr = models.CharField(max_length=1, choices=cod_status, default="A")
class SubGroup(models.Model):
    cod_status = [
        ("A", "Ativo"),
        ("I", "Inativo")
    ]
    
    cod_sbg = models.CharField(max_length=3, primary_key=True)
    desc_sbg = models.TextField()
    situ_sgb = models.CharField(max_length=1,choices=cod_status, default="A")
    group_f = models.ForeignKey(Group, on_delete=models.PROTECT)

class Product(models.Model):
    cod_status = [
        ("A", "Ativo"),
        ("I", "Inativo")
    ]

    cod_psv = models.CharField(max_length=5, primary_key=True)
    desc_psv = models.TextField()
    group_f = models.ForeignKey(Group, on_delete=models.PROTECT)
    sub_group_f = models.ForeignKey(SubGroup, on_delete=models.PROTECT)
    situ_psv = models.CharField(max_length=1, choices=cod_status, default="A")


