from sft import repositories, models
import pytest


@pytest.mark.django_db
class TestSFTRepositories:

    @pytest.fixture
    def loan_application(self):
        return models.LoanApplication.objects.create(
            rec_id=11,
            client_name="Test Client",
            amount=10
        )

    @pytest.fixture
    def contract(self, loan_application):
        return models.Contract.objects.create(
            rec_id=32812,
            customer_name="Test customer",
            loan_application=loan_application
        )

    @pytest.fixture
    def products(self, loan_application):
        return [models.Product.objects.create(
            rec_id=idx,
            product_name=f"Test product_{idx}",
            loan_application=loan_application
        ) for idx in range(5)]

    @pytest.fixture
    def manufacturers(self, products):
        return [models.Manufacturer.objects.create(
            rec_id=idx,
            name=f"Test manufacturer_{idx}",
            product=product
        ) for idx, product in enumerate(products)]

    def test_get_manufacturer_by_contract_id(self, contract, manufacturers):
        # given
        contract_id = 32812

        # when
        manufacturers = repositories.get_manufacturer_by_contract_id(contract_id)

        # then
        assert len(manufacturers) > 0
        assert len(manufacturers) == 5
