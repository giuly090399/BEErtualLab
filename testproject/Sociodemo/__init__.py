from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'demographics'
    players_per_group = 10
    tasks = ['A', 'B', 'C']
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Edad = models.IntegerField(
        blank=True, label='¿Qué edad tienes?'
    )
    Genero = models.StringField(
        label='¿Con qué género te identificas?',
        choices=[["F", "Femenino"], ["M", "Masculino"], ["O", "Otro"], ["N", "Prefiero no contestar"]]
    )
    Estado_Civil = models.StringField(
        blank=True, label='¿Cuál es tu estado civil?',
        choices=[["1", "Soltero"], ["2", "Casado"], ["3", "Divorciado"], ["4", "Viudo"]]
    )
    Nivel_Educativo = models.StringField(
        label='¿Cuál es tu máximo nivel educativo alcanzado?',
        choices=[["1", "Preparatoria"], ["2", "Profesional"], ["3", "Posgrado"], ["4", "No aplica"]]
    )
    Personas_dependientes = models.StringField(
            label='¿Cuántas personas dependen de ti económicamente?',
        choices=[["1", "Ninguna"], ["2", "1"], ["3", "2"], ["4", "Más de 2"]]
    )
    Habitantes = models.StringField(
        label='¿Cuántas personas habitan en tu casa incluyéndote?',
        choices=[["1", "1"], ["2", "2"], ["3", "3"], ["4", "4 o más"]]
    )
    Ingreso = models.IntegerField(
        label='¿Cuál es el ingreso mensual aproximado del hogar en pesos mexicanos?',
        choices=[["1", "menos de 17,000 pesos"], ["2", "Entre 17,000 y 28,000 pesos"], ["3", "Entre 28,000 y 40,000"], ["4", "Entre 40,000 y 60,000"],
                 ["5", "60,000 o más pesos"]]
    )
    Fijo = models.StringField(
        label='¿El ingreso anterior es fijo o variable?',
        choices=[["1", "Fijo"], ["2", "variable"]]
    )


class Preguntas(Page):
    form_model = Player
    form_fields = ['Edad', 'Genero', 'Estado_Civil', 'Nivel_Educativo', 'Personas_dependientes', 'Habitantes', 'Ingreso', 'Fijo']


class Agradecimiento(Page):
    pass


page_sequence = [Preguntas, Agradecimiento]
