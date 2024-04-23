from datetime import date

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from tsepamo.choices import SITE_CHOICES, YES_NO_CHOICES, HIV_CHOICES, \
    INFANT_STAT_CHOICES, CORD_COLOR_CHOICES, PLACENTAL_VESSELS_CHOICES, \
    CORD_APPEAR_CHOICES, YES_NO_UNKNOWN_CHOICES, CORD_INSERT_CHOICES


class TsepamoTwo(models.Model):
    record_id = models.IntegerField(validators=[MinValueValidator(100100001),
                                                MaxValueValidator(999999999)],
                                    verbose_name='Record ID'
                                    )
    site = models.CharField(max_length=100, choices=SITE_CHOICES,
                            verbose_name='Delivery Site'
                            )
    screen_cl = models.CharField(max_length=4, choices=YES_NO_CHOICES,
                                 verbose_name='Was this woman SCREEENED for the '
                                              'cervical length study? (BLUE DOT ON '
                                              'MATERNITY CARD)')
    part_cl = models.CharField(max_length=4, choices=YES_NO_CHOICES,
                               verbose_name='Was this woman ENROLLED in '
                                            'the cervical length study?')
    part_cl_bid = models.IntegerField(validators=[MinValueValidator(1),
                                                  MaxValueValidator(999)],
                                      verbose_name='What is the cervical length study '
                                                   'number'
                                      )
    placental = models.CharField(max_length=4, choices=YES_NO_CHOICES,
                                 verbose_name='Was this woman part of the placental '
                                              'sub-study?')
    placenta_icsigned = models.CharField(max_length=4, choices=YES_NO_CHOICES,
                                         verbose_name='Did this woman sign the Tsepamo '
                                                      'Placental informed consent form '
                                                      'version 1.0?')
    placenta_dattimeconsent = models.DateTimeField(verbose_name='What was the date and '
                                                                'time of the placental '
                                                                'consent?')
    placenta_iccopy = models.CharField(max_length=4, choices=YES_NO_CHOICES,
                                       verbose_name='Was this woman offered a copy of '
                                                    'the placental informed consent for '
                                                    'version 1.0?')
    placenta_consent_received = models.CharField(max_length=4, choices=YES_NO_CHOICES,
                                                 verbose_name='Was consent received by '
                                                              'the study coordinator?')
    placenta_id = models.IntegerField(validators=[MinValueValidator(100100001),
                                                  MaxValueValidator(999999999)],
                                      verbose_name='Placental ID'
                                      )
    placenta_hiv = models.CharField(max_length=20, choices=HIV_CHOICES,
                                    verbose_name='What is the HIV status of the mother '
                                                 'whose placenta was collected?')
    placenta_infantstat = models.CharField(max_length=10, choices=INFANT_STAT_CHOICES,
                                           verbose_name='What was the infant status?')
    placenta_nga = models.IntegerField(validators=[MinValueValidator(24),
                                                   MaxValueValidator(46)],
                                       verbose_name='What was the gestational age at '
                                                    'delivery?'
                                       )
    placenta_bwt = models.IntegerField(validators=[MinValueValidator(100),
                                                   MaxValueValidator(5000)],
                                       verbose_name='What was the birthweight?'
                                       )
    placenta_sga = models.CharField(max_length=10,
                                    verbose_name='Is this baby SGA?')
    ntl_lab_date = models.DateField(validators=[MinValueValidator(date(2015, 9, 1)),
                                                MaxValueValidator(date(2017, 9, 1))],
                                    verbose_name='What day was the placenta examined?')

    cord_frommarg = models.IntegerField(verbose_name='How far was the cord insertion '
                                                     'from the margin?')
    cord_lngth = models.IntegerField(verbose_name='How long was the cord?')
    cord_dm = models.IntegerField(verbose_name='What is the diameter of the cord?')
    cord_color = models.CharField(max_length=10, choices=CORD_COLOR_CHOICES,
                                  verbose_name='What is the color of the cord?')
    cord_color_other = models.CharField(max_length=10,
                                        verbose_name='Cord \'other\' color, please '
                                                     'specify:')
    placental_vessels = models.CharField(max_length=10, choices=PLACENTAL_VESSELS_CHOICES,
                                         verbose_name='Number of vessels?')
    cord_twists = models.IntegerField(verbose_name='There are 3 twists in how many cm?')
    cord_appear = models.CharField(max_length=10, choices=CORD_APPEAR_CHOICES,
                                   verbose_name='Did the cord appear:')
    trueknow = models.CharField(max_length=10, choices=YES_NO_UNKNOWN_CHOICES,
                                verbose_name='Did the cord have a true knot?')
    cord_insert = models.CharField(max_length=10, choices=CORD_INSERT_CHOICES,
                                   verbose_name='Was the cord inserted into the:')
    cord_otherfnd = models.CharField(verbose_name='other cord findings')
    membrane_color = models.CharField(verbose_name='What is the membrane color?')
    membrane_otherfnd = models.CharField(verbose_name='Other membrane findings')
    placenta_weight = models.IntegerField(
        verbose_name='What is the trimmed placental weight?',
        validators=[MinValueValidator(150),
                    MaxValueValidator(600)], )
    disc_diameter = models.IntegerField(verbose_name='What is the disc diameter?')
    disc_thick = models.IntegerField(verbose_name='How thick is the disc?')
    fetal_surf = models.CharField(verbose_name='Fetal surface findings?')
    maternal_surf = models.CharField(verbose_name='Maternal surface findings?')
    parench = models.CharField(verbose_name='Parenchyma findings?')
    placenta_sectioned = models.CharField(verbose_name='Was the placenta examined and '
                                                       'sectioned exactly as per '
                                                       'protocol?', choices=YES_NO_CHOICES)
