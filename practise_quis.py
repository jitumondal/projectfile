


from typing import NoReturn


class Electric_gaget:
    defination = "for machine"


class pocket_gaget(Electric_gaget):
    hight = "33mm"
    pass

class phone(pocket_gaget,Electric_gaget):
    
    @staticmethod
    def feature():
        return "It's made to silvar"

nokia = phone()

print(nokia.feature())