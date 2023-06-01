from django.contrib import admin
from .models import Pool, Game, Pick, GameCard, League, UserLeague

admin.site.register(Pool)
admin.site.register(Game)
admin.site.register(Pick)
admin.site.register(GameCard)
admin.site.register(League)
admin.site.register(UserLeague)
