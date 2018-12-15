class GameStats():
    def __init__(self,aliens_settings):
        self.aliens_settings=aliens_settings
        self.reset_stats()
        self.game_active=False
        self.score=0

    def reset_stats(self):
         self.ships_left=self.aliens_settings.ship_limit
