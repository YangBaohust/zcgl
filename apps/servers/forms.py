from django import forms

from .models import Server, ServerType


# 定义资产表单验证
class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = ['zctype', 'ipaddress', 'description', 'brand', 'zcmodel', 'zcnumber', 'zcpz', 'undernet', 'guartime',
                  'comment']


# 定义资产类型表单验证
class ServerTypeForm(forms.ModelForm):
    class Meta:
        model = ServerType
        fields = ['zctype']

