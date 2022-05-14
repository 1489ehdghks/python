# import theater_module
# theater_module.price(3)
# theater_module.price_morning

import theater_module as mv
from theater_module import price_morning
from theater_module import price_soldier #theater_module 을 mv로 바꿈.
mv.price(3)

from theater_module import* # theater module을 전부 다 사용.
price(3)
price_morning(4)
price_soldier(5)