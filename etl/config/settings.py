"""
settings.py

Centralized configuration management for the
Supply Chain Intelligence Platform.

Responsibilities:
- Load environment variables
- Validate configuration
- Convert data types
- Create required directories
- Provide a single immutable settings object
"""

import sys
from enum import Enum
from pathlib import Path
from pydantic import SecretStr


from pydantic import (
    BaseModel,
    Field,
    HttpUrl,
    ValidationError,
)

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


# ============================================================
# ENUMS
# ============================================================

class Environment(str, Enum):
    DEVELOPMENT = "development"
    TESTING = "testing"
    PRODUCTION = "production"


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


# ============================================================
# ERP SETTINGS
# ============================================================

class ERPSettings(BaseModel):
    base_url: HttpUrl = Field(alias="ERP_BASE_URL")

    api_key: SecretStr = Field(alias="ERP_API_KEY",min_length=1)

    api_secret: SecretStr = Field(alias="ERP_API_SECRET",min_length=1)

    timeout: int = Field(
        default=30,
        alias="ERP_TIMEOUT",
        gt=0,
        le=300
    )


# ============================================================
# POSTGRESQL SETTINGS
# ============================================================

class PostgreSQLSettings(BaseModel):
    host: SecretStr = Field(alias="POSTGRES_HOST",min_length=1)

    database: SecretStr = Field(alias="POSTGRES_DATABASE",min_length=1)

    username: SecretStr = Field(alias="POSTGRES_USER",min_length=1)

    password: SecretStr = Field(alias="POSTGRES_PASSWORD",min_length=1)

    port: int = Field(
        default=5432,
        alias="POSTGRES_PORT",
        ge=1,
        le=65535
    )


# ============================================================
# ETL SETTINGS
# ============================================================

class ETLSettings(BaseModel):
    batch_size: int = Field(
        default=500,
        alias="DEFAULT_BATCH_SIZE",
        gt=0
    )

    max_retries: int = Field(
        default=3,
        alias="MAX_RETRIES",
        ge=0,
        le=10
    )

    retry_delay: int = Field(
        default=5,
        alias="RETRY_DELAY",
        ge=1
    )


# ============================================================
# LOGGING SETTINGS
# ============================================================

class LoggingSettings(BaseModel):
    log_level: LogLevel = Field(
        default=LogLevel.INFO,
        alias="LOG_LEVEL"
    )

    log_directory: Path = Field(
        default=Path("etl/logs"),
        alias="LOG_DIRECTORY"
    )


# ============================================================
# BACKUP SETTINGS
# ============================================================

class BackupSettings(BaseModel):
    backup_directory: Path = Field(
        default=Path("etl/backup"),
        alias="BACKUP_DIRECTORY"
    )


# ============================================================
# MAIN SETTINGS
# ============================================================

class Settings(BaseSettings):

    environment: Environment = Field(
        default=Environment.DEVELOPMENT,
        alias="APP_ENV"
    )

    erp: ERPSettings

    postgres: PostgreSQLSettings

    etl: ETLSettings = Field(default_factory=ETLSettings)

    logging: LoggingSettings = Field(default_factory=LoggingSettings)

    backup: BackupSettings = Field(default_factory=BackupSettings)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        populate_by_name=True,
        extra="ignore",
        frozen=True,
    )


# ============================================================
# LOAD SETTINGS
# ============================================================

try:

    settings = Settings()

    # --------------------------------------------------------
    # Create Required Directories
    # --------------------------------------------------------

    settings.logging.log_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    settings.backup.backup_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    # --------------------------------------------------------
    # Startup Message
    # --------------------------------------------------------

    print("\n==============================================")
    print(" Supply Chain Intelligence Platform")
    print(" Configuration Loaded Successfully")
    print("==============================================")

    print(f"Environment : {settings.environment.value}")
    print(f"ERP URL     : {settings.erp.base_url}")
    print(f"Database    : {settings.postgres.database}")
    print(f"Batch Size  : {settings.etl.batch_size}")
    print("==============================================\n")


except ValidationError as e:

    print(
        "\n❌ CRITICAL CONFIGURATION ERROR",
        file=sys.stderr
    )

    print(
        "Application failed to start.\n",
        file=sys.stderr
    )

    print(
        "Please verify your .env configuration.\n",
        file=sys.stderr
    )

    for error in e.errors():

        field = " -> ".join(
            str(loc)
            for loc in error["loc"]
        )

        print(
            f"• {field}: {error['msg']}",
            file=sys.stderr
        )

    sys.exit(1)