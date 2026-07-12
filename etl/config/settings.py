import sys
from pathlib import Path
from pydantic import BaseModel, Field, HttpUrl, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

# --- 1. Define Sub-Models for Grouped Sections ---

class ERPSettings(BaseModel):
    # Field aliases map standard flat .env variables into this nested structure
    base_url: HttpUrl = Field(alias="ERP_BASE_URL")         # Mandatory
    api_key: str = Field(alias="ERP_API_KEY")               # Mandatory
    api_secret: str = Field(alias="ERP_API_SECRET")         # Mandatory
    timeout: int = Field(default=30, alias="ERP_TIMEOUT")   # Optional (has default)


class PostgreSQLSettings(BaseModel):
    host: str = Field(alias="POSTGRES_HOST")                # Mandatory
    database: str = Field(alias="POSTGRES_DATABASE")        # Mandatory
    username: str = Field(alias="POSTGRES_USER")            # Mandatory
    password: str = Field(alias="POSTGRES_PASSWORD")        # Mandatory
    port: int = Field(default=5432, alias="POSTGRES_PORT")  # Optional (has default)


class ETLSettings(BaseModel):
    batch_size: int = 100
    max_retries: int = 3
    retry_delay: int = 5


class LoggingSettings(BaseModel):
    log_level: str = "INFO"
    log_directory: Path = Path("logs")


class BackupSettings(BaseModel):
    backup_directory: Path = Path("backups")


# --- 2. Main Settings Class ---

class Settings(BaseSettings):
    # Groups
    erp: ERPSettings
    db: PostgreSQLSettings
    etl: ETLSettings = Field(default_factory=ETLSettings)
    logging: LoggingSettings = Field(default_factory=LoggingSettings)
    backup: BackupSettings = Field(default_factory=BackupSettings)

    # Telling Pydantic to read from a flat .env file using aliases
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        populate_by_name=True,  # Allows instantiating by field name or alias
        extra="ignore"          # Ignores unmatched environment variables
    )


# --- 3. The Startup Validation Hook & Instantiation ---

try:
    # This line triggers the parsing and strict type/presence validation
    settings = Settings()
    
except ValidationError as e:
    # If ANY critical variable is missing or malformed, catch it immediately
    print("\n❌ CRITICAL CONFIGURATION ERROR: Application failed to start.", file=sys.stderr)
    print("Please check your .env file or environment variables.\n", file=sys.stderr)
    
    # Loop through the validation errors and display clean feedback
    for error in e.errors():
        # Cleanly formats the field location path
        field_name = " -> ".join(str(loc) for loc in error['loc'])
        print(f"  • {field_name}: {error['msg']}", file=sys.stderr)
        
    # Crash the application immediately before any pipeline code can execute
    sys.exit(1)