class Clock:
    def __init__(self, hours: int, minutes: int):
        """
        Constructor to create a Clock instance with normalized time.
        """
        total_minutes = hours * 60 + minutes
        self.hours = (total_minutes // 60) % 24
        self.minutes = total_minutes % 60

    def __eq__(self, other: object) -> bool:
        """
        Check if two Clock objects represent the same time.
        """
        if not isinstance(other, Clock):
            return NotImplemented
        return self.hours == other.hours and self.minutes == other.minutes

    def __add__(self, other: "Clock") -> "Clock":
        """
        Add two Clock objects and return a new Clock instance.
        """
        total_minutes = self.hours * 60 + self.minutes + other.hours * 60 + other.minutes
        return Clock(total_minutes // 60, total_minutes % 60)

    def add_minutes(self, minutes: int) -> "Clock":
        """
        Add minutes to the current Clock object and return a new Clock instance.
        """
        total_minutes = self.hours * 60 + self.minutes + minutes
        return Clock(total_minutes // 60, total_minutes % 60)

    def __str__(self) -> str:
        """
        Convert the Clock object to a string in HH:MM format.
        """
        return f"{self.hours:02}:{self.minutes:02}"


# Example usage:
if __name__ == "__main__":
    # Test normalization
    clock1 = Clock(6, 62)  # Should normalize to 07:02
    clock2 = Clock(25, 0)  # Should normalize to 01:00
    print(clock1)  # Output: 07:02
    print(clock2)  # Output: 01:00

    # Test equality
    print(clock1 == clock2)  # Output: False

    # Test addition
    clock3 = clock1 + clock2
    print(clock3)  # Output: 08:02

    # Test add_minutes
    clock4 = clock1.add_minutes(120)
    print(clock4)  # Output: 09:02
