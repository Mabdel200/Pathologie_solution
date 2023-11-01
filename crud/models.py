from django.db import models


# Create your models here.

# class Member(models.Model):
#     attrite = models.CharField(max_length=2, default='0')  # select
#     name = models.CharField(max_length=30, default='toto')
#     age = models.IntegerField(default=0)
#     gender = models.CharField(max_length=2,default='0')
#     children = models.CharField(max_length=2, default='0')
#     edu = models.CharField(max_length=2, default='0')  # select
#     marital = models.CharField(max_length=2, default='0')  # select
#     income = models.CharField(max_length=2, default='0')  # select
#     monthOnBooks = models.FloatField(default=0)
#     totalRelationshipCount = models.FloatField(default=0)
#     monthsInactive12mon = models.FloatField(default=0)
#     contactsCount12mon = models.FloatField(default=0)
#     creditLimit = models.FloatField(default=0)
#     totalRevolvingBal = models.FloatField(default=0)
#     avgOpenToBuy = models.FloatField(default=0)
#     totalAmtChngQ4Q1 = models.FloatField(default=0)
#     totalTransAmt = models.FloatField(default=0)
#     totalTransCt = models.FloatField(default=0)
#     totalCtChngQ4Q1 = models.FloatField(default=0)
#     avgUtilizationRatio = models.FloatField(default=0)

class Member(models.Model):
    name = models.CharField(max_length=20, default='incognito')
    age = models.IntegerField(default=0 )
    sex = models.CharField(max_length=1, default=0, )  # select
    cp = models.IntegerField(default=0, )
    trtbps = models.IntegerField(default=0,)
    chol = models.IntegerField(default=0, )
    fbs = models.IntegerField(default=0, )
    restecg = models.IntegerField(default=0, )
    thalachh = models.IntegerField(default=0, )
    exng = models.IntegerField(default=0, )
    caa = models.IntegerField(default=0, )

    def __str__(self):
        members = self.name + " " + self.age + " " + self.sex + " " + self.sex + " " + self.cp \
                  + " " + self.trtbps + " " + self.chol + " " + self.fbs + " " + self.restecg + " " + self.thalachh \
                  + " " + self.exng + " " + self.caa + " "
        return members
