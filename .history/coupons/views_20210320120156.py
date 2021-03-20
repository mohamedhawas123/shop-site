from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.utils import timezone
from .form import CouponApplyForm
from .models import Coupon


def couponApply(request):
    now  = timezone.now()
    fromm = CouponApplyForm(request.POST):
    if fromm.is_valid():
        code = fromm.cleaned_data.get("code")
        try:
            coupon = Coupon.objects.get(code__iexact=code, )
        
        except:

