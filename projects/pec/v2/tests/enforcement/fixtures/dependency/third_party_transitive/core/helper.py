import yaml


def encode(value: str) -> str:
    return yaml.safe_dump(value)
