from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'public_goods_simple'
    players_per_group = 3
    num_rounds = 1
    endowment = cu(100)
    multiplier = 1.8


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=Constants.endowment, label="¿Cuánto contribuye usted a la generación futura?"
    )


# PAGES
class Instructions(Page):
    pass


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


page_sequence = [Instructions, Contribute]
