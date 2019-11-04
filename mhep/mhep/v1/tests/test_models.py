import pytest

from django.conf import settings

from .. import VERSION
from ..models import Organisation

pytestmark = pytest.mark.django_db


def test_organisation_assessments(organisation_with_extras: Organisation):
    assert getattr(organisation_with_extras, f"{VERSION}_assessments").all().count() == 1


def test_organisations_related_name_on_user_model(user_with_org: settings.AUTH_USER_MODEL):
    assert getattr(user_with_org, f"{VERSION}_organisations").all().count() == 1
