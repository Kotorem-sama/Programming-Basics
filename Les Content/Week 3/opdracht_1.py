# Maak en test een klasse met de naam Time die een specifiek
# uur, minuut en seconde bevat. De klasse moet methoden hebben
# om de waarden van zijn attributen in te stellen en te
# verkrijgen. Zorg ervoor dat de uren tussen 0 en 23 liggen en
# de minuten en seconden tussen 0 en 59.
# a) doe dat in de eerste instantie met zichtbare
# /niet-private attributen 

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def set_time(self, hour, minute, second):
        if 0 <= hour <= 23:
            self.hour = hour
        else:
            raise ValueError("Hour must be between 0 and 23")

        if 0 <= minute <= 59:
            self.minute = minute
        else:
            raise ValueError("Minute must be between 0 and 59")

        if 0 <= second <= 59:
            self.second = second
        else:
            raise ValueError("Second must be between 0 and 59")

    def get_time(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"
        
tijd = Time()
tijd.set_time(23, 30, 45)
print(tijd.get_time())

# b) maak hetzelfde klasse met niet zichtbare / private
# attributen.

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def set_time(self, hour, minute, second):
        if 0 <= hour <= 23:
            self.hour = hour
        else:
            raise ValueError("Hour must be between 0 and 23")

        if 0 <= minute <= 59:
            self.minute = minute
        else:
            raise ValueError("Minute must be between 0 and 59")

        if 0 <= second <= 59:
            self.second = second
        else:
            raise ValueError("Second must be between 0 and 59")

    def get_time(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"
        
tijd = Time()
tijd.set_time(23, 30, 45)
print(tijd.get_time())

# c) maak hetzelfde klasse maar nu met decorators.

