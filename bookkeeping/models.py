from django.db import models
from accont.models import UserInfo

# Create your models here.
class Ofconsumption(models.Model):
    icon = models.CharField(verbose_name='图标',max_length=32,default="shopping_basket")
    title = models.CharField(verbose_name='消费类型',max_length=10)
    income_or_outlay_choices = (
        (1, '支出'),
        (2, '收入')
    )
    income_or_outlay = models.IntegerField(verbose_name='支出或收入', choices=income_or_outlay_choices)
    def __str__(self):
        return self.title



class Charge(models.Model):
    user = models.ForeignKey(to=UserInfo,verbose_name='用户',null=True,on_delete=models.CASCADE)
    doughy = models.IntegerField(verbose_name='金额/元')
    ofconsumption = models.ForeignKey(to=Ofconsumption,on_delete=models.CASCADE)
    ofconsumption_date = models.DateField(verbose_name='时间',auto_now_add=True)


