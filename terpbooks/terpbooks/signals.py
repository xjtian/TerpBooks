from django.db.models.signals import pre_save


def validate_model(sender, instance, raw, using, **kwargs):
    if not raw:
        instance.full_clean()


pre_save.connect(validate_model, dispatch_uid='full_clean_custom')