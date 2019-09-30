from django import forms

from .models import UserProfile


# 定义登录时表单验证
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


# 定义用户修改密码时表单验证
class UserPwdModifyForm(forms.Form):
    pwd1 = forms.CharField(required=True)
    pwd2 = forms.CharField(required=True)


# 定义添加，修改用户时表单验证
class UserInfoForm(forms.ModelForm):
    username = forms.CharField(required=True)

    class Meta:
        model = UserProfile
        fields = ['staff_no', 'department', 'isadmin', 'bg_telephone', 'mobile']
