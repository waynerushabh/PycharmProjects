from decimal import *

# Decimal() or Decimal( tuple ) where tuple->(0(+sign) or 1(-sign), (tuple of all digits in order), decimal-place/exponent)
# from float (still not accurate)
print(Decimal(1.2))
print(Decimal(1.1))
# Tuple style
x = decimal.Decimal((0, (1, 2, 3, 2), 0))

# Decimal.Adjusted()
print(decimal.Decimal(x).adjusted())

# as_integer_ratio()