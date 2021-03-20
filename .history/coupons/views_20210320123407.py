from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from .form import CouponApplyForm
from .models import Coupon


def couponApply(request):
    now  = timezone.now()
    fromm = CouponApplyForm(request.POST)
    if fromm.is_valid():
        code = fromm.cleaned_data.get("code")
        try:
            coupon = Coupon.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gte= now , active=True)
            
            request.session['coupon_id']=coupon.id  
        
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    
    return redirect('cart:cart_detail')

