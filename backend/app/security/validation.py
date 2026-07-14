def validate_positive_amount(amount: float):
    if amount <= 0:
        raise ValueError('Amount must be positive')
    return True


def validate_owner(owner_id: str, current_owner: str):
    if owner_id != current_owner:
        raise PermissionError('Ownership validation failed')
    return True
