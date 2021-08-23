from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    A1 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    A2 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    A3 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    A4 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    A5 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    A6 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    A7 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    A8 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    A9 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    P1 = models.StringField(
        label='¿...?',
        choices=[['1', '1'], ['2', '2']]
    )
    P2 = models.StringField(
        label='¿...?',
        choices=[['1', '1'], ['2', '2']]
    )
    P3 = models.StringField(
        label='¿...?',
        choices=[['1', '1'], ['2', '2']]
    )


# FUNCTIONS
# PAGES
class Instructions(Page):
    pass


class Articulos(Page):
    form_model = 'player'
    form_fields = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']


class Preguntas(Page):
    form_model = 'player'
    form_fields = ['P1', 'P2', 'P3']


page_sequence = [Instructions, Articulos, Preguntas]
