import theater_module
theater_module.price(3)
theater_module.price_moning(3)
theater_module.price_solidier(3)

import theater_module as kello# klello라는 별칭을 사용하여 theater_module 사용

kello.price(3)
kello.price_moning(3)
kello.price_solidier(3)

from theater_module import * 
price(3)
price_moning(3)
price_solidier(3)

from theater_module  import price,price_moning 

price(3)
price_moning(3)


from theater_module import price_solidier

price(3)


from theater_module import price_solidier as price

price(3)
