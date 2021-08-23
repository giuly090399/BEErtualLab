from otree.api import *
import random


class Constants(BaseConstants):
    name_in_url = 'demographics'
    players_per_group = 10
    tasks = ['A', 'B', 'C']
    num_rounds = 1


class Subsession(BaseSubsession):
    # def creating_session(self):
    #     if self.round_number == 1:
    #         for p in self.get_players():
    #             round_numbers = list(range(1, Constants.num_rounds + 1))
    #             random.shuffle(round_numbers)
    #             p.participant.task_rounds = dict(zip(Constants.tasks, round_numbers))
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    RP1 = models.StringField(
        label='¿En qué momento pasas de elegir la Opción A a la Opción B?',
        choices=[["1", "1"], ["2", "2"], ["3", "3"], ["4", "4"], ["5", "5"],
                 ["6", "6"], ["7", "7"], ["8", "8"], ["9", "9"], ["10", "10"]],
        widget=widgets.RadioSelectHorizontal
    )
    RP2 = models.StringField(
        label='¿En qué momento pasas de elegir la Opción A a la Opción B?',
        choices=[["1", "1"], ["2", "2"], ["3", "3"], ["4", "4"], ["5", "5"],
                 ["6", "6"], ["7", "7"], ["8", "8"], ["9", "9"], ["10", "10"]],
        widget=widgets.RadioSelectHorizontal
    )
    RP3 = models.StringField(
        label='¿En qué momento pasas de elegir la Opción A a la Opción B?',
        choices=[["1", "1"], ["2", "2"], ["3", "3"], ["4", "4"], ["5", "5"],
                 ["6", "6"], ["7", "7"], ["8", "8"], ["9", "9"], ["10", "10"]],
        widget=widgets.RadioSelectHorizontal
    )
    RP4 = models.StringField(
        label='¿En qué momento pasas de elegir la Opción A a la Opción B?',
        choices=[["1", "1"], ["2", "2"], ["3", "3"], ["4", "4"], ["5", "5"],
                 ["6", "6"], ["7", "7"], ["8", "8"], ["9", "9"], ["10", "10"]],
        widget=widgets.RadioSelectHorizontal
    )
    Edad = models.IntegerField(
        blank=True, label='¿Qué edad tienes?'
    )
    Nivel_Educativo = models.StringField(
        label='¿En qué nivel educativo estás?',
        choices=[["1", "Preparatoria"], ["2", "Profesional"], ["3", "Posgrado"], ["4", "No aplica"]]
    )
    Ingreso = models.IntegerField(
        blank=True, label='¿Cuál es el ingreso aproximado del hogar?'
    )
    FK1 = models.StringField(
        label='¿...?',
        choices=[['1', '1'], ['2', '2']]
    )
    FK2 = models.StringField(
        label='¿...?',
        choices=[['1', '1'], ['2', '2']]
    )
    FK3 = models.StringField(
        label='¿...?',
        choices=[['1', '1'], ['2', '2']]
    )


class TaskA(Page):
    form_model = Player
    form_fields = ['RP1', 'RP2', 'RP3', 'RP4']

    # @staticmethod
    # def is_displayed(player: Player):
    #     participant = player.participant
    #
    #     return player.round_number == participant.task_rounds


class TaskB(Page):
    form_model = Player
    form_fields = ['Edad', 'Nivel_Educativo', 'Ingreso']

    # @staticmethod
    # def is_displayed(player: Player):
    #     participant = player.participant
    #
    #     return player.round_number == participant.task_rounds
    #

class TaskC(Page):
    form_model = Player
    form_fields = ['FK1', 'FK2', 'FK3']

    # @staticmethod
    # def is_displayed(player: Player):
    #     participant = player.participant
    #
    #     return player.round_number == participant.task_rounds


page_sequence = [TaskA, TaskC, TaskB]
