from otree.api import *
import random


class Constants(BaseConstants):
    name_in_url = 'other'
    players_per_group = 10
    tasks = ['A', 'B', 'C']
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                round_numbers = list(range(1, Constants.num_rounds + 1))
                random.shuffle(round_numbers)
                p.participant.task_rounds = dict(zip(Constants.tasks, round_numbers))


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
    PT1 = models.StringField(
        label='...a veces es ruda con los demás',
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        widget=widgets.RadioSelectHorizontal
    )
    PT2 = models.StringField(
        label='...es tolerante por naturaleza',
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        widget=widgets.RadioSelectHorizontal
    )
    PT3 = models.StringField(
        label='...es considerada y amable',
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        widget=widgets.RadioSelectHorizontal
    )
    PT4 = models.StringField(
        label='...realiza un trabajo minucioso',
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        widget=widgets.RadioSelectHorizontal
    )
    PT5 = models.StringField(
        label='...tiende a ser floja',
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        widget=widgets.RadioSelectHorizontal
    )
    PT6 = models.StringField(
        label='...realiza actividades eficientemente',
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        widget=widgets.RadioSelectHorizontal
    )
    PT7 = models.StringField(
        label='...es habladora',
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        widget=widgets.RadioSelectHorizontal
    )
    PT8 = models.StringField(
        label='...es sociable',
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        widget=widgets.RadioSelectHorizontal
    )
    PT9 = models.StringField(
        label='...es reservada',
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        widget=widgets.RadioSelectHorizontal
    )
    PT10 = models.StringField(
        label='...se pone nerviosa con facilidad',
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        widget=widgets.RadioSelectHorizontal
    )
    PT11 = models.StringField(
        label='...se preocupa mucho',
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        widget=widgets.RadioSelectHorizontal
    )
    PT12 = models.StringField(
        label='...maneja con facilidad el estrés',
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        widget=widgets.RadioSelectHorizontal
    )
    PT13 = models.StringField(
        label='...es original, propone ideas',
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        widget=widgets.RadioSelectHorizontal
    )
    PT14 = models.StringField(
        label='...valora experiencias artísticas y estéticas',
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        widget=widgets.RadioSelectHorizontal
    )
    PT15 = models.StringField(
        label='...tiene una imaginación activa',
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7']],
        widget=widgets.RadioSelectHorizontal
    )
    FK1 = models.StringField(
        label='Si usted le presta 25 pesos a un amigo y a la siguiente semana le regresa los 25 pesos, ¿cuánto le pagó de interés?',
        choices=[['Nada', 'Nada'], ['Otro valor', 'Otro valor'], ['No sabe', 'No sé']]
    )
    FK2 = models.StringField(
        label='Supongamos que deposita 100 pesos en una cuenta de ahorro que le da una ganancia de 2% al año. Si no realiza depósitos ni retiros,'
              '¿incluyendo los intereses, usted tendría al final de año...',
        choices=[['1', 'más de 102 pesos?'], ['2', 'exactamente 102 pesos?'], ['3', 'menos de 102 pesos?'], ['4', 'No sé']]
    )
    FK3 = models.StringField(
        label='Supongamos que deposita 100 pesos en una cuenta de ahorro que le da una ganancia de 2% al año. Si no realiza depósitos ni retiros,'
              '¿incluyendo los intereses, usted tendría al final de cinco años...?',
        choices=[['1', 'más de 110 pesos'], ['2', 'exactamente 110 pesos'], ['3', 'menos de 110 pesos'], ['4', 'No sé']]
    )
    FK4 = models.StringField(
        label='Si le regalan 1,000 pesos, pero tiene que esperar un año para gastarlos y ese año la inflación es del 5%, ¿usted podría comprar...?',
        choices=[['1', 'más de lo que puede comprar hoy'], ['2', 'los mismo'], ['3', 'menos de lo que puede comprar hoy'], ['4', 'No sabe']]
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
    form_fields = ['PT1', 'PT2', 'PT3', 'PT4', 'PT5', 'PT6', 'PT7', 'PT8', 'PT9', 'PT10', 'PT11', 'PT12', 'PT13', 'PT14', 'PT15']

    # @staticmethod
    # def is_displayed(player: Player):
    #     participant = player.participant
    #
    #     return player.round_number == participant.task_rounds


class TaskC(Page):
    form_model = Player
    form_fields = ['FK1', 'FK2', 'FK3', 'FK4']

    # @staticmethod
    # def is_displayed(player: Player):
    #     participant = player.participant
    #
    #     return player.round_number == participant.task_rounds


page_sequence = [TaskA, TaskB, TaskC]
