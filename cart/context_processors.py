from . models import cart,cart_items
from . views import cart_id

def counter(request):
    item_count=0
    if 'admin'in request.path:
        return{}
    else:
        try:
            Cart=cart.objects.filter(cart_id=cart_id(request))
            cart_item=cart_items.objects.all().filter(cart=Cart[:1])
            for i in cart_item:
                item_count += i.quantity
        except cart.DoesNotExist:
            item_count = 0
        return dict(item_count=item_count)
        
