from etl.config.settings import settings

print("Configuration loaded successfully!")
print(f"Environment: {settings.environment.value}")
print(f"ERP URL: {settings.erp.base_url}")
print(f"Database: {settings.postgres.database}")

# python -m etl.config.test_config