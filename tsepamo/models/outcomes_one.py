from .model_mixins.complete_field_mixin import CompleteFieldMixin
from .model_mixins.record_id_model_mixin import RecordIDModelMixin
from .model_mixins.outcomes_model_mixin import OutcomesModelMixin

class OutcomesOne(OutcomesModelMixin,RecordIDModelMixin,
                  CompleteFieldMixin):

  class Meta:
        app_label = 'tsepamo'
        verbose_name = 'Outcomes 1'
        verbose_name_plural = 'Outcomes 1'

