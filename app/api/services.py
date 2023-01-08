import random
import string


def generate_unique_code(length: int = 5) -> str:
    characters_string = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return "".join([random.choice(characters_string) for _ in range(length)])
