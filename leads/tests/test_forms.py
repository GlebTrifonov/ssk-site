import pytest

from leads.forms import LeadForm




def test_lead_form_valid_phone(lead_data):
    form = LeadForm(data=lead_data)
    result = form.is_valid()
    assert result


@pytest.mark.parametrize("phone", ["123", "375298308649", "+8487678980"])
def test_lead_form_invalid_phone(lead_data, phone):
    lead_data["phone"] = phone
    form = LeadForm(data=lead_data)
    result = form.is_valid()
    assert not result
    assert "phone" in form.errors
