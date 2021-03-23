from django import forms

class CouponApplyForm(forms.Form):
    code = forms.CharField()


    
class CouponApplyForm(forms.Form):
    code = forms.CharField(label=_('Coupon'))