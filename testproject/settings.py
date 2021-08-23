from os import environ
import random

SESSION_CONFIGS = [
    dict(
        name='Experimentos_BEErtual_Lab',
        app_sequence=['Dictator_Dice', 'SavingsMX', 'Otras', 'Adrian', 'Pablo', 'Cooperacion', 'Sociodemo'],
        num_demo_participants=30,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=60.00, doc=""
)

PARTICIPANT_FIELDS = ['task_rounds']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'MXN'
USE_POINTS = True

ADMIN_USERNAME = 'Giuly'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('BEErtual')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '9220058014649'
