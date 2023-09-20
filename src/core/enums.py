from enum import Enum


class EnvEnum(str, Enum):
    LOCAL = "local"
    DEV = "dev"
    STG = "stg"
    PROD = "prod"
