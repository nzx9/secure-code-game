'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stucked then read the hint                   ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_TOTAL = 1e6
MIN_TOTAL = 0
MAX_QUANTITY = 10

def validorder(order: Order):
    net =  0
    for item in order.items:
        if item.amount < MAX_TOTAL and item.amount > -1 * MAX_TOTAL:
            if item.type == 'payment':
                net += item.amount
            elif item.type == 'product':
                if item.quantity < MAX_QUANTITY:
                    net -= item.amount * item.quantity
                else:
                    return("Max quantity exceeded!: %s" %item.quantity)
            else:
                return("Invalid item type: %s::%s" % (item.type, item.description))

    if net != 0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
