class Xorshift:
    def __init__(self, seed: int):
        self.state = seed if seed != 0 else 1  # Нулевой seed недопустим
