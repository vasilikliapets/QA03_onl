def check_spec_syllable(sylla):
    """
    The function check this is one spec syllable or not
    """
    if not sylla.isalnum() and len(sylla) == 1:
        return True
    return False
    # Или так просто нужно было?
    # return not sylla.isalnum()
