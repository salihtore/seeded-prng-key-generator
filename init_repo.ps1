$ErrorActionPreference = "Stop"

$RepoName = "seeded-prng-key-generator"

Write-Host "Creating repository structure: $RepoName"

# Root directory (zaten icindeysek tekrar olusturmaz)
New-Item -ItemType Directory -Force -Path src | Out-Null
New-Item -ItemType Directory -Force -Path tests | Out-Null

# src files
New-Item -ItemType File -Force -Path src\__init__.py | Out-Null
New-Item -ItemType File -Force -Path src\prng.py | Out-Null
New-Item -ItemType File -Force -Path src\keygen.py | Out-Null
New-Item -ItemType File -Force -Path src\cli.py | Out-Null

# test file
New-Item -ItemType File -Force -Path tests\test_vectors.py | Out-Null

# root files
New-Item -ItemType File -Force -Path README.md | Out-Null
New-Item -ItemType File -Force -Path requirements.txt | Out-Null
New-Item -ItemType File -Force -Path .gitignore | Out-Null

Write-Host "Repository structure created successfully."
Write-Host "You can now add the source code."
