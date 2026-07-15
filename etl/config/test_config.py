from etl.config.settings import settings

print("Configuration loaded successfully!")
print(f"Environment: {settings.environment.value}")
print(f"ERP URL: {settings.erp.base_url}")
print(f"Database: {settings.postgres.database}")

# python -m etl.config.test_config

# output 
# ==============================================
#  Supply Chain Intelligence Platform
#  Configuration Loaded Successfully
# ==============================================
# Environment : development
# ERP URL     : http://globalmart.localhost:8080/
# Database    : **********
# Batch Size  : 500
# ==============================================

# Configuration loaded successfully!
# Environment: development
# ERP URL: http://globalmart.localhost:8080/
# Database: **********


