# Selenium Automation Framework (Python + Pytest)

This repository contains a Python-based Selenium automation codebase,
combining a small **test automation framework** with **standalone Selenium demo scripts**
created for learning and demonstration purposes.

The main focus of this repository is the automation framework built with
**Pytest** and the **Page Object Model (POM)** pattern.

---

## ✨ Key Features

- Selenium WebDriver automation using Python  
- Pytest-based test framework with fixtures  
- Page Object Model (POM) design for maintainable tests  
- Explicit and implicit waits  
- Data-driven testing using JSON  
- Screenshot capture on test failure  
- Optional HTML test reports (`pytest-html`)  
- Automatic browser setup and cleanup via fixtures  

---

## 📁 Repository Structure

```
pythonTesting/
├── tests/                  # Pytest test cases
├── pageObjects/            # Page Object Model classes
├── utils/                  # Shared utilities
├── data/                   # Test data (JSON)
├── learnings/              # Standalone Selenium demo scripts
├── conftest.py             # Pytest fixtures and browser configuration
├── pytest.ini              # Pytest configuration (markers)
├── requirements.txt        # Project dependencies
└── README.md
```

---

## ⚙️ Setup

### Prerequisites
- Python 3.8 or newer  
- Google Chrome browser  

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd pythonTesting
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run all tests:
```bash
python -m pytest
```

---

## ▶️ Running Tests

- Run all tests:
```bash
python -m pytest
```

- Run only smoke tests:
```bash
python -m pytest -m smoke
```

- Run tests with browser selection:
```bash
python -m pytest --browser_name=chrome
python -m pytest --browser_name=firefox
```

---

## 📊 HTML Report (Optional)

Generate an HTML test report:
```bash
python -m pytest --html=reports/report.html --self-contained-html
```

> The `reports/` folder is generated locally and is intentionally excluded from version control.

---

## 📘 Standalone Selenium Demos (`learnings/`)

The `learnings/` folder contains independent Selenium scripts created as part of
learning and experimentation.

These scripts demonstrate:
- Explicit vs implicit waits  
- Element locating strategies  
- Child window handling  
- Negative scenarios and validation messages  

⚠️ These scripts are **not part of the automation framework** and are included to
demonstrate hands-on Selenium knowledge.

---

## 🧾 Notes

- Demo websites used in this repository are public test applications  
- Some demo scripts intentionally validate failure scenarios  
- ChromeDriver is managed automatically by Selenium  

---

## 👤 Author

Computer Science B.Sc. graduate with hands-on experience in:
- Selenium & Pytest automation  
- Automation framework design  
- Page Object Model (POM)  
- Full-stack and backend development  

---

## 📄 License

This repository is intended for learning and demonstration purposes.
