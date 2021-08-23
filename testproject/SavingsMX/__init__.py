import random
from otree.api import *

doc = """
Each player decides how much to save each period for their retirement for the first six periods, 
the last two every player will live from their savings.
"""


# CONSTANTS

class Constants(BaseConstants):
    name_in_url = 'Tarea_de_Ahorro'
    players_per_group = 2
    num_rounds = 1
    fixed_income = 60
    min_consumption = 30
    lab_period = 6
    ret_period = 4
    esquemas = ['high', 'low', 'none']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    CP1 = models.IntegerField(
        label='¿De cuántos tokens es la penalización por consumir menos del mínimo en un periodo?', blank=True
    )
    CP2 = models.StringField(
        label='¿Cuántas rondas en total se juegan de la actividad de ahorro? ',
        choices=[["1", "Una ronda"], ["2", "Dos rondas"], ["3", "Tres rondas"]]
    )
    CP3 = models.StringField(
        label='¿Qué ronda se elige para el pago por tu desempeño?',
        choices=[["1", "La primera"], ["2", "La segunda"], ["3", "Aleatoriamente se elige una"]]
    )
    Cond1 = models.StringField(
        label='¿Qué condición te gusta más?',
        choices=[["high", "Modalidad 1"], ["low", "Modalidad 2"], ["none", "Modalidad 3"]]
    )
    Cond2 = models.StringField(
        label='¿Qué condición te gusta en segundo lugar?',
        choices=[["high", "Modalidad 1"], ["low", "Modalidad 2"], ["none", "Modalidad 3"]]
    )
    AFORE1 = models.IntegerField(
        blank=True, initial=0, min=0, max=Constants.fixed_income
    )
    AFORE2 = models.IntegerField(
        blank=True, initial=0, min=0, max=Constants.fixed_income
    )
    AFORE3 = models.IntegerField(
        blank=True, initial=0, min=0, max=Constants.fixed_income
    )
    AFORE4 = models.IntegerField(
        blank=True, initial=0, min=0, max=Constants.fixed_income
    )
    AFORE5 = models.IntegerField(
        blank=True, initial=0, min=0, max=Constants.fixed_income
    )
    AFORE6 = models.IntegerField(
        blank=True, initial=0, min=0, max=Constants.fixed_income
    )
    AFORE7 = models.IntegerField(
        blank=True, initial=0, min=0, max=Constants.fixed_income
    )
    AFORE8 = models.IntegerField(
        blank=True, initial=0, min=0, max=Constants.fixed_income
    )
    AFORE9 = models.IntegerField(
        blank=True, initial=0, min=0, max=Constants.fixed_income
    )
    AFORE10 = models.IntegerField(
        blank=True, initial=0, min=0, max=Constants.fixed_income
    )
    AFORE11 = models.IntegerField(
        blank=True, initial=0, min=0, max=Constants.fixed_income
    )
    AFORE12 = models.IntegerField(
        blank=True, initial=0, min=0, max=Constants.fixed_income
    )


# FUNCTIONS


def CP1_error_message(Player, value):
    print('value is', value)
    if value != 10:
        return "Incorrecto, intenta de nuevo"


def CP2_error_message(Player, value):
    print('value is', value)
    if value != "2":
        return "Incorrecto, intenta de nuevo. Recuerda que vas a jugar dos veces todo."


def CP3_error_message(Player, value):
    print('value is', value)
    if value != "3":
        return "Incorrecto, intenta de nuevo. Tu desempeño puede variar en las dos rondas, por lo cual se eligirá aleatoriamente."


class Instructions(Page):
    pass


class TaskQuestions(Page):
    form_model = Player
    form_fields = ['CP1', 'CP2', 'CP3']


class Ronda1(Page):
    pass


class Preference(Page):
    form_model = Player
    form_fields = ['Cond1', 'Cond2']

    def is_displayed(self):
        return self.id_in_group == 1


class FirstTask(Page):
    form_model = Player
    form_fields = ['AFORE1', 'AFORE2', 'AFORE3', 'AFORE4', 'AFORE5', 'AFORE6']

    def vars_for_template(self):
        if self.id_in_group == 1:
            grupo = 1
            esq_1_display = self.Cond1
            # Esq_1 se refiere al esquema que juega el grupo 1. En la primera tarea será su decisión, en la segunda aleatorio.
            return dict(
                esq_1=esq_1_display,
                grupo=grupo
            )
        else:
            grupo = 2
            esq_2 = random.choice(Constants.esquemas)
            return dict(
                esq_2=esq_2,
                grupo=grupo
            )


class JubFirstTask(Page):
    def vars_for_template(self):
        Ahorro_acumulado_display = self.AFORE1 + self.AFORE2 + self.AFORE3 + self.AFORE4 + self.AFORE5 + self.AFORE6
        Consumo_medio = Ahorro_acumulado_display / Constants.ret_period
        if self.id_in_group == 1:
            grupo = 1
            esq_1_display = self.Cond1
            return dict(
                esq_1=esq_1_display,
                grupo=grupo,
                Consumo_medio=Consumo_medio,
                Ahorro_acumulado_display=Ahorro_acumulado_display
            )
        else:
            grupo = 2
            esq_2 = random.choice(Constants.esquemas)
            return dict(
                esq_2=esq_2,
                grupo=grupo,
                Consumo_medio=Consumo_medio,
                Ahorro_acumulado_display=Ahorro_acumulado_display
            )


class Ronda2(Page):
    pass


class Preference2(Page):
    form_model = Player
    form_fields = ['Cond1_2', 'Cond2_2']

    def is_displayed(self):
        return self.id_in_group == 2
        print('Grupo 1')


class SecTask(Page):
    form_model = Player
    form_fields = ['AFORE7', 'AFORE8', 'AFORE9', 'AFORE10', 'AFORE11', 'AFORE12']

    def vars_for_template(self):
        if self.id_in_group == 2:
            grupo = 2
            esq_2 = self.Cond1
            return dict(
                esq_2=esq_2,
                grupo=grupo
            )
        else:
            grupo = 1
            esq_1 = random.choice(Constants.esquemas)
            return dict(
                esq_1=esq_1,
                grupo=grupo
            )


class JubSecTask(Page):
    def vars_for_template(self):
        Ahorro_acumulado_display = self.AFORE7 + self.AFORE8 + self.AFORE9 + self.AFORE10 + self.AFORE11 + self.AFORE12
        Consumo_medio = Ahorro_acumulado_display / Constants.ret_period
        if self.id_in_group == 2:
            grupo = 2
            esq_2_display = self.Cond1
            return dict(
                esq_2=esq_2_display,
                grupo=grupo,
                Consumo_medio=Consumo_medio,
                Ahorro_acumulado_display=Ahorro_acumulado_display
            )
        else:
            grupo = 1
            esq_1 = random.choice(Constants.esquemas)
            return dict(
                esq_1=esq_1,
                grupo=grupo,
                Consumo_medio=Consumo_medio,
                Ahorro_acumulado_display=Ahorro_acumulado_display
            )


page_sequence = [Instructions, TaskQuestions, Ronda1, Preference, FirstTask, JubFirstTask, Ronda2, Preference2, SecTask, JubSecTask]
