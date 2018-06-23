from Super_users.models import Iran_city

class city_Adder:
    def __init__(self):
        iraninan_city = ["تهران", "اصفهان", "شیراز", "تبریز", "مشهد", "اراک", "بندرعباس", "زاهدان", "رشت", "بیرجند", "بجنورد", "کاشمر"]
        for i in iraninan_city:
            city = Iran_city(city_name=i)
            city.save()