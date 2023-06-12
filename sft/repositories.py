from sft.models import Contract, Manufacturer
from typing import List


def get_manufacturer_by_contract_id(contract_id: int) -> List[Manufacturer]:
    """
    Get uniques id of manufacturers which linked with contract.

    :param contract_id: Id of contract.
    :return: List of manufacturer with unique id.
    """
    contract = Contract.objects.get(rec_id=contract_id)

    manufacturers = Manufacturer.objects.filter(product__loan_application__loan_application_contract=contract)

    return [manufacturer for manufacturer in manufacturers]
