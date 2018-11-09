#coding:utf-8
#将表单全部封装成class放在此处
from django import forms

#登录表单
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"输入用户名","required":"required",}),
                               max_length=50,error_messages={"required":"用户名不能为空",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"输入密码","required":"required",}),
                               max_length=20,error_messages={"required":"密码不能为空",})
    captcha = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"输入验证码","required":"required",}),
                               max_length=20,error_messages={"required":"验证码不能为空",})

#注册表单
class RegForm(forms.Form):                  #placeholder输入字段预期值的提示信息
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"用户名","required":"required",}),
                               max_length=50,error_messages={"required":"用户名不能为空",})
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"邮箱","required":"required",}),
                            max_length=50,error_messages={"required":"邮箱不能为空",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"密码","required":"required",}),
                               max_length=20,error_messages={"required":"密码不能为空",})
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"确认密码","required":"required",}),
                                       max_length=20,error_messages={"required":"密码不能为空",})
    address = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"地址","required":"required",}),
                              max_length=200,error_messages={"required":"地址不能为空",})
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"联系电话","required":"required",}),
                            max_length=50,error_messages={"required":"联系电话不能为空",})
    def clean(self):   #自定义form的校验规则
        if not self.is_valid():  #required的字段有没有填写的is_valid()返回值就是false
            raise forms.ValidationError('所有项都必须填写')
        elif self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise forms.ValidationError('两次输入的密码不一致')
        else:
            cleaned_data = super(RegForm,self).clean()
        return cleaned_data   #clean()或clean_field()最后都必须返回验证完毕或者修改后的值

