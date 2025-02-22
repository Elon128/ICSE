class Food:
    def __init__(self, quantifier):
        self.quantifier = quantifier

    def calories(self):
        raise NotImplementedError("This method should be implemented by subclasses!")

    def get_weight(self):
        raise NotImplementedError("This method should be implemented by subclasses!")

    def __eq__(self, other):
        return self.calories() == other.calories()

    def __lt__(self, other):
        return self.calories() < other.calories()


class Apples(Food):
    def calories(self):
        return 102 * self.quantifier

    def get_weight(self):
        return 200 * self.quantifier


class Oranges(Food):
    def calories(self):
        return 94 * self.quantifier

    def get_weight(self):
        return 200 * self.quantifier


class CookieDough(Food):
    def calories(self):
        return int(2.44 * self.quantifier)

    def get_weight(self):
        return self.quantifier  # Weight is already given in grams


class Bananas(Food):  # New Food
    def calories(self):
        return 89 * self.quantifier

    def get_weight(self):
        return 180 * self.quantifier


class Strawberries(Food):  # New Food
    def calories(self):
        return 32 * self.quantifier

    def get_weight(self):
        return 100 * self.quantifier


# Example Usage
if __name__ == "__main__":
    apple = Apples(3)  # 3 apples
    orange = Oranges(2)  # 2 oranges
    cookie_dough = CookieDough(100)  # 100g cookie dough
    banana = Bananas(2)  # 2 bananas
    strawberry = Strawberries(5)  # 5 portions of strawberries

    print(f"Apple calories: {apple.calories()} kcal, weight: {apple.get_weight()} g")
    print(f"Orange calories: {orange.calories()} kcal, weight: {orange.get_weight()} g")
    print(f"Cookie Dough calories: {cookie_dough.calories()} kcal, weight: {cookie_dough.get_weight()} g")

    # Compare foods
    print(f"Do apples and oranges have the same calories? {apple == orange}")
    print(f"Is cookie dough lighter than 2 bananas? {cookie_dough < banana}")

    # More comparisons
    print(f"Strawberries vs. bananas by calories: {strawberry.calories()} vs. {banana.calories()}")
