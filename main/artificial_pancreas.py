class ArtificialPancreasSystem:
    """A simplified model for data-driven glucose regulation."""

    GLUCOSE_PER_CARB = 0.5       # each carb raises glucose by this amount
    GLUCOSE_BURN_PER_MIN = 0.3   # each minute of exercise lowers glucose by this amount
    MIN_GLUCOSE = 50             # safety floor

    def __init__(self, glucose_level, insulin_sensitivity=1.0, target_glucose=100, tolerance=10):
        self.glucose_level = glucose_level
        self.insulin_sensitivity = insulin_sensitivity
        self.target_glucose = target_glucose
        self.tolerance = tolerance
        self.total_insulin_delivered = 0.0

    def meal(self, carbs: float):
        """Simulate a meal event (carbs eaten)."""
        if carbs < 0:
            raise ValueError("Carb value cannot be negative")

        increase = carbs * self.GLUCOSE_PER_CARB
        self.glucose_level += increase
        return self.glucose_level

    def exercise(self, duration: float):
        """Simulate exercise (in minutes)."""
        if duration < 0:
            raise ValueError("Exercise duration cannot be negative")

        burn = duration * self.GLUCOSE_BURN_PER_MIN
        self.glucose_level -= burn

        # Prevent unrealistically low glucose
        if self.glucose_level < self.MIN_GLUCOSE:
            self.glucose_level = self.MIN_GLUCOSE

        return self.glucose_level

    def predict_action(self):
        """
        Decide what action to take:
        - deliver_insulin (if too high)
        - warn_low_glucose (if too low)
        - maintain (if stable)
        """
        upper_limit = self.target_glucose + self.tolerance
        lower_limit = self.target_glucose - self.tolerance

        if self.glucose_level > upper_limit:
            # too high → deliver insulin
            excess = self.glucose_level - self.target_glucose
            dose = excess * 0.1 * self.insulin_sensitivity  # simple insulin rule
            self.total_insulin_delivered += dose
            self.glucose_level -= dose
            return "deliver_insulin", self.glucose_level

        elif self.glucose_level < lower_limit:
            # too low → warn
            return "warn_low_glucose", self.glucose_level

        else:
            # within range → maintain
            return "maintain", self.glucose_level