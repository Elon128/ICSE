import random


class University:
    def __init__(self, name: str, founding_year: int, country: str) -> None:
        """
        Represents a university with its name, founding year, and country.
        """
        self.name = name
        self.founding_year = founding_year
        self.country = country

    def __repr__(self) -> str:
        """
        Returns a string representation of the university object.
        """
        return repr((self.name, self.founding_year, self.country))


if __name__ == "__main__":
    # Familiarizing with `sort` and `sorted` methods
    random_list = list(range(1000))
    random.shuffle(random_list)

    # Using `sorted` to return a new sorted list
    sorted_list = sorted(random_list)
    print("Sorted list using `sorted()`: ", sorted_list)

    # Using `sort` to sort the list in place
    random_list.sort()
    print("Sorted list using `sort()`: ", random_list)

    # Working with a list of universities
    universities = [
        ("Otto-von-Guericke-Universität Magdeburg", 1993, "Germany"),
        ("Harvard University", 1636, "USA"),
        ("Technische Universität München", 1868, "Germany"),
        ("RWTH Aachen", 1870, "Germany"),
    ]

    # Sorting universities by founding year (age)
    universities_sorted_by_age = sorted(universities, key=lambda u: u[1])
    print("Universities sorted by age: ", universities_sorted_by_age)

    # Sorting universities alphabetically by name
    universities_sorted_by_name = sorted(universities, key=lambda u: u[0])
    print("Universities sorted by name: ", universities_sorted_by_name)

    # Creating a list of University objects
    university_objects = [University(name=u[0], founding_year=u[1], country=u[2]) for u in universities]

    # Sorting university objects by founding year
    university_objects_sorted_by_age = sorted(university_objects, key=lambda u: u.founding_year)
    print("University objects sorted by age: ", university_objects_sorted_by_age)

    # Sorting university objects by name
    university_objects_sorted_by_name = sorted(university_objects, key=lambda u: u.name)
    print("University objects sorted by name: ", university_objects_sorted_by_name)
