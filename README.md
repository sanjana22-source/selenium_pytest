# Selenium + Pytest Automation Framework (UI + API)
## Overview
This is a modular automation framework built using:
- Selenium (UI automation)
- Pytest (test execution)
- Allure (reporting)
- Requests (API automation)
- JSON Schema validation (contract testing)

The framework supports both UI and API test automation using a layered architecture.

---
## Architecture

Test → Service Layer → API Client → Validators → External API

UI tests follow Page Object Model (POM).

API tests follow:
- Generic API Client abstraction
- Centralized response validation
- JSON schema contract validation
- YAML-based configuration

---

## Folder Structure

config/ → Configuration files  
pages/ → Page Object Model  
services/ → API service layer  
utilities/ → Core reusable utilities  
schemas/ → JSON schema definitions  
tests/ → UI & API tests  

---

## Configuration

Create `config/api_config.yaml` from example file and add your API key.

---


##  Highlights

- Modular layered architecture
- Centralized response validation
- Schema-based contract testing
- Secure configuration handling
- Designed for scalability and CI integration

---
