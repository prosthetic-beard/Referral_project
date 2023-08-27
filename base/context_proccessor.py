
from django.db.models import Sum
from account.models import Transactions


def host(request):
    # print(request.__dict__)
    # print(request.environ.get("HTTP_HOST"))
    # print())
    context = {
        'host': request.environ.get("HTTP_HOST"),
        'completed': request.user.first_app and request.user.second_app and request.user.third_app and request.user.fourth_app if request.user.is_authenticated else False,
    }
    return context


def transactions(request):
    approved_withdrawals = None
    pending_withdrawals = None
    refferals_earnings = None
    if request.user.is_authenticated:
        approved_withdrawals = Transactions.objects.filter(user=request.user, type="W", status="A")
        pending_withdrawals = Transactions.objects.filter(user=request.user, type="W", status="P")
        refferals_earnings = Transactions.objects.filter(user=request.user, type="R")
        context = {
            
            "approved_withdrawals": approved_withdrawals.aggregate(Sum("amount")) if approved_withdrawals.exists() else {"amount__sum": 0.00},
            "pending_withdrawals": pending_withdrawals.aggregate(Sum("amount")) if pending_withdrawals.exists() else {"amount__sum": 0.00},
            "refferals_earnings": refferals_earnings.aggregate(Sum("amount")) if refferals_earnings.exists() else {"amount__sum": 0.00},
            
            }
        return context
    else:
        context = {
            
            "approved_withdrawals": approved_withdrawals,
            "pending_withdrawals": pending_withdrawals,
            "refferals_earnings": refferals_earnings,
            
            }
        return context