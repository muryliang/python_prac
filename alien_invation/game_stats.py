class GameStats():
    """track game stats"""

    def __init__(self, ai_settings):
        """initialize status"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.shift_down = False
        self.high_score = 0


    def reset_stats(self):
        """reset"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
