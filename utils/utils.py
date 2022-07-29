class BalconyResolver:

    @staticmethod
    def __check_slash(value):
        return '/' in value

    @staticmethod
    def __check_dashes(value):
        return '-' in value

    @staticmethod
    def __check_space(value: str) -> bool:
        return ' ' in value

    @staticmethod
    def __check_backslash(value: str) -> bool:
        return '\\' in value

    @staticmethod
    def __check_plus(value: str) -> bool:
        return '+' in value

    @staticmethod
    def __check_words(value: str) -> bool:
        return value.isalpha()

    @staticmethod
    def __normal(value: str) -> bool:
        try:
            value = value.replace(',', '.')
        except AttributeError:
            if any([type(value) == float, type(value) == int]):
                return True
        try:
            value = float(value)
            return True
        except ValueError:
            return False

    def decide(self, value: str) -> float:
        if self.__normal(value):
            return float(value.replace(',', '.')) if type(value) is not float else value
        elif value == 'да':
            return 1.0
        elif value == 'нет':
            return 0.0
        elif self.__check_slash(value):
            return self.__slash(value)
        elif self.__check_dashes(value):
            return self.__dash(value)
        elif self.__check_backslash(value):
            return self.__backslash(value)
        elif self.__check_space(value):
            return self.__space(value)
        elif self.__check_plus(value):
            return self.__plus(value)
        elif self.__check_words(value):
            return self.__words(value)

    def __words(self, value: str):
        value_l = value.split()
        return self.__count(value_l)

    def __slash(self, value: str):
        value_l = value.split('/')
        return self.__count(value_l)

    def __backslash(self, value: str):
        value_l = value.split('\\')
        return self.__count(value_l)

    def __space(self, value: str):
        value_l = value.split(' ')
        return self.__count(value_l)

    def __plus(self, value: str):
        value_l = value.split('+')
        return self.__count(value_l)

    def __count(self, value_list):
        _sum = 0.0
        for v in value_list:
            if self.__normal(v):
                _sum += float(v.replace(',', '.'))
            else:
                pass
        return _sum

    def __dash(self, value):
        value_l = value.split('-')
        return self.__count(value_l)


class KommunalResolver:

    def __init__(self):
        self.costs = [-1.0,]

    @staticmethod
    def __check_slash(value):
        return '/' in value

    @staticmethod
    def __check_dashes(value):
        return '-' in value

    @staticmethod
    def __check_space(value: str) -> bool:
        return ' ' in value

    @staticmethod
    def __check_backslash(value: str) -> bool:
        return '\\' in value

    @staticmethod
    def __check_plus(value: str) -> bool:
        return '+' in value

    @staticmethod
    def __check_words(value: str) -> bool:
        return value.isalpha()

    @staticmethod
    def __normal(value: str) -> bool:
        try:
            value = value.replace(',', '.')
        except AttributeError:
            if any([type(value) == float, type(value) == int]):
                return True
        try:
            value = float(value)
            return True
        except ValueError:
            return False

    def decide(self, value: str) -> list:
        if self.__normal(value):
            return [float(value.replace(',', '')), -1.0, -1.0] if type(value) is not float else [value, -1.0, -1.0]
        elif value == ' ':
            return [-1.0, -1.0, -1.0]
        elif self.__check_slash(value):
            return self.__slash(value)
        elif self.__check_space(value):
            return self.__space(value)
        elif self.__check_dashes(value):
            return self.__dash(value)
        elif self.__check_backslash(value):
            return self.__backslash(value)
        elif self.__check_plus(value):
            return self.__plus(value)
        elif self.__check_words(value):
            return self.__words(value)
        else:
            return [-1.0, -1.0, -1.0]

    def __words(self, value: str):
        value_l = value.split()
        return self.__count(value_l)

    def __slash(self, value: str):
        value_l = value.split('/')
        return self.__count(value_l)

    def __backslash(self, value: str):
        value_l = value.split('\\')
        return self.__count(value_l)

    def __space(self, value: str):
        value_l = value.split(' ')
        return self.__count(value_l)

    def __plus(self, value: str):
        value_l = value.split('+')
        return self.__count(value_l)

    def __dash(self, value):
        value_l = value.split('-')
        return self.__count(value_l)

    def __count(self, value_list) -> list:
        for v in value_list:
            if self.__normal(v):
                if len(v) < 3:
                    pw = 10**(4-len(v))
                    v = float(v.replace(',', '.'))*pw
                else:
                    v = float(v.replace(',', '.'))
                self.costs.append(v)
        if len(self.costs) == 1:
            self.costs *= 3
        elif len(self.costs) == 2:
            self.costs.append(-1)
        costs = self.costs.copy()
        self.costs = [-1.0,]
        return costs


class MainResolver:

    enc = {}

    def decide(self, value):
        if value in self.enc.keys():
            return float(self.enc[value])


class TypeResolver(MainResolver):
    enc = {
        'flat': 1,
        'malosem': 2,
        'pansion': 3,
        'obshaga': 4,
        'room': 5,
        'gost': 6,
    }


class TwoLevelsResolver(MainResolver):
    enc = {
        'no': 1,
        'yes': 2,
    }


class WindowsResolver(MainResolver):
    enc = {
        'plastic': 1,
        'wood': 2,
        'allum': 3,
        'plastic_wood': 4,
    }


class KeepResolver(MainResolver):
    enc = {
        'cosmetic': 1,
        'well_black': 2,
        'need': 3,
        'good': 4,
        'design': 5,
        'black': 6,
        'usual': 7,
    }


class BalconTypeResolver(MainResolver):
    enc = {
        'yes_balcon': 1,
        'no_balcon': 2,
        'loggia': 3,
        'balcon': 4,
        'more_loggia': 5,
        'balcon_loggia': 6,
        'more_balcon': 7,
        'erker': 8,
        'balcon_erker': 9,
        'more_erker': 10,
    }


class BathroomsResolver(MainResolver):

    enc = {
        'unite': 1,
        'separate': 2,
        'separate,shower': 3,
        'separate,unite': 4,
        'unite,bath': 5,
        'unite,shower': 6,
        'separate,bath': 7,
        'unite,shower,bath': 8,
        'shower': 9,
        'bath': 10,
        'separate,shower,bath': 11,
        'one_on_floor': 12,
        'unite,sit_bath': 13,
        'unite,bath,sit_bath': 14,
        'separate,unite,shower': 15,
    }


class PlatesResolver(MainResolver):

    enc = {
        'no_plate': 1,
        'gas': 2,
        'no_plate,gas': 3,
        'no_plate,electric': 4,
        'gas,electric': 5,
        'no_plate,gas,electric': 6,
        'convective': 7,
    }


class ClosedYardResolver(MainResolver):
    enc = {
        'no': 1,
        'yes': 2,
    }


if __name__ == '__main__':
    c = KommunalResolver()
    s = 'летом-2500, зима-4500.'
    print(c.decide(s))