from django.db import models


class RecordIDModelMixin(models.Model):

    record_id = models.PositiveIntegerField(
        verbose_name="Record ID (site code, RA number, 5 DIGIT number)",
        unique=True,
        help_text=("e.g. 100100001Site Codes:Princess Marina=10"
                   "Nyangabwge=20Molepolole=30Maun=40Ghanzi=50Selebi Phikwe=60Serowe=70Mahalapye=80"
                   "Bamalete Lutheran Hospital=90Palapye Primary Hospital=11Deborah Retief Hospaital=12 "
                   "Kanye SDA Hospital=13Athlone Hospital=14Bobonong Primary Hospital=15Gumare Primary Hospital=16"
                   "Goodhope Primary Hospital=17Tutume Primary Hospital=18Letlhakane Primary Hospital=19"
                   "RA Number:OM=01GL=02DS=03 EM=04CD=05RM=06PM=07KF=08TM=09GM=11MO=12MD=13RZ=14GKM=15JM=16RS=17SL=18SDP=19KP=20DJ=21JL=22MT=23SM=24"),
    )

    class Meta:
        abstract = True
