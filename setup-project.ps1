# ==========================================
# Supply Chain Intelligence Platform
# Project Structure Creator
# Safe: Creates only missing folders/files
# Existing files are NOT modified.
# ==========================================

$projectRoot = "."

# ----------------------------
# Folders
# ----------------------------
$folders = @(
    "airflow",

    "database",
    "database\bronze",
    "database\silver",
    "database\gold",
    "database\sql",

    "dbt",
    "docker",
    "docs",
    "powerbi",

    "tests",
    "tests\unit",
    "tests\integration",

    "etl",
    "etl\config",
    "etl\clients",
    "etl\extractors",
    "etl\loaders",
    "etl\validators",
    "etl\checkpoints",
    "etl\logging",
    "etl\utils",
    "etl\models",
    "etl\backup",
    "etl\logs"
)

foreach ($folder in $folders) {
    $path = Join-Path $projectRoot $folder

    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path | Out-Null
        Write-Host "[Created Folder] $folder" -ForegroundColor Green
    }
    else {
        Write-Host "[Exists] $folder" -ForegroundColor Yellow
    }
}

# ----------------------------
# Files
# ----------------------------
$files = @(

    # Root
    ".env.example",
    ".gitignore",
    "requirements.txt",
    "README.md",
    "docker-compose.yml",

    # Tests
    "tests\__init__.py",

    # ETL
    "etl\__init__.py",

    # Config
    "etl\config\__init__.py",
    "etl\config\settings.py",

    # Clients
    "etl\clients\__init__.py",
    "etl\clients\erpnext_client.py",

    # Extractors
    "etl\extractors\__init__.py",
    "etl\extractors\base_extractor.py",
    "etl\extractors\item_extractor.py",

    # Loaders
    "etl\loaders\__init__.py",
    "etl\loaders\postgres_loader.py",

    # Validators
    "etl\validators\__init__.py",
    "etl\validators\validator.py",

    # Checkpoints
    "etl\checkpoints\__init__.py",
    "etl\checkpoints\checkpoint.py",

    # Logging
    "etl\logging\__init__.py",
    "etl\logging\logger.py",

    # Utils
    "etl\utils\__init__.py",
    "etl\utils\helpers.py",

    # Models
    "etl\models\__init__.py",
    "etl\models\schemas.py",

    # Runner
    "etl\run_pipeline.py"
)

foreach ($file in $files) {

    $path = Join-Path $projectRoot $file

    if (-not (Test-Path $path)) {

        New-Item -ItemType File -Path $path | Out-Null

        Write-Host "[Created File] $file" -ForegroundColor Cyan
    }
    else {

        Write-Host "[Exists] $file" -ForegroundColor Yellow

    }
}

Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host "Project structure verification completed." -ForegroundColor Green
Write-Host "Missing folders/files created successfully." -ForegroundColor Green
Write-Host "Existing files were NOT modified." -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green