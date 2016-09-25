import django
django.setup()

from seating.models import Person

p1 = Person(first_name="Sahil", last_name="Kemkar", likes=[])
p1.save()
p2 = Person(first_name="Ashay", last_name="Sheth", likes=[])
p2.save()
p3 = Person(first_name="Justin", last_name="Williams", likes=[])
p3.save()
p4 = Person(first_name="Nick", last_name="Fahrenkrog", likes=[])
p4.save()
p5 = Person(first_name="Pear", last_name="Varin", likes=[])
p5.save()
p6 = Person(first_name="Carina", last_name="Claassen", likes=[])
p6.save()
p7 = Person(first_name="Sidney", last_name="Durant", likes=[])
p7.save()
p8 = Person(first_name="Kyle", last_name="Murray", likes=[])
p8.save()