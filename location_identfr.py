import phonenumbers
from phonenumbers import geocoder,carrier

ph1 = phonenumbers.parse("+918378040004")
ph2 = phonenumbers.parse("+919404993984")

c = carrier.name_for_number(ph2,"en")

print(c)
print(geocoder.description_for_number(ph1,"en"));
print(geocoder.description_for_number(ph2,"en"));
