
from django.db.models import Sum
from account.models import Transactions


def host(request):
    # print(request.__dict__)
    # print(request.environ.get("HTTP_HOST"))
    # print())
    context = {
        'host': request.environ.get("HTTP_REFERER"),
    }
    return context


def transactions(request):
    approved_withdrawals = None
    pending_withdrawals = None
    refferals_earnings = None
    if request.user.is_authenticated:
        approved_withdrawals = Transactions.objects.filter(user=request.user, type="W", status="A").aggregate(Sum("amount"))
        pending_withdrawals = Transactions.objects.filter(user=request.user, type="W", status="P").aggregate(Sum("amount"))
        refferals_earnings = Transactions.objects.filter(user=request.user, type="R").aggregate(Sum("amount"))
    context = {
        "approved_withdrawals": approved_withdrawals,
        "pending_withdrawals": pending_withdrawals,
        "refferals_earnings": refferals_earnings,
        
        }
    return context