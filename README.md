# 🧩 Lab 5 — Static Code Analysis

This repository contains the cleaned and updated version of `inventory_system.py` after performing static code analysis using **Pylint**, **Bandit**, and **Flake8**.  
The purpose of this lab was to identify, understand, and fix coding, security, and style issues in the given Python script.

---

##  Deliverable 1

**File:** `inventory_system_fixed.py`

- The original `inventory_system.py` file was analyzed using Bandit, Flake8, and Pylint.
- A total of **7 issues** (from high to low severity) were identified and fixed.
- The final version of the file produces no Bandit security issues and achieves a **Pylint score of 9.64/10**.

---

##  Deliverable 2 — Issues Table (Documented Fixes)

| No. | Issue Description | Tool Used | Original Code | Fix Applied | Severity |
|-----|-------------------|------------|----------------|--------------|-----------|
| 1 | **Use of `eval()` – potential code injection vulnerability** | Bandit | `eval("print('eval used')")` | Removed the `eval()` line completely and replaced it with a safe `print()` statement. | 🔴 **High** |
| 2 | **Bare `except:` block silently ignored all errors** | Bandit / Flake8 | ```python\nexcept:\n    pass``` | Changed to `except KeyError:` with a clear error message. |  **High** |
| 3 | **Mutable default argument (`logs=[]`) can lead to shared state bugs** | Pylint | `def add_item(item="default", qty=0, logs=[])` | Replaced with `logs=None` and initialized inside the function (`if logs is None: logs = []`). | 🔴 **High** |
| 4 | **Files opened without context manager or encoding** | Pylint | `f = open(file, "r")` / `f = open(file, "w")` | Used `with open(file, "r", encoding="utf-8") as f:` and `with open(file, "w", encoding="utf-8") as f:` for safe file handling. | 🔴 **High** |
| 5 | **Function names not in snake_case** | Pylint | `addItem`, `removeItem`, `saveData`, etc. | Renamed to `add_item`, `remove_item`, `save_data`, etc., following PEP8 naming standards. |  **Medium** |
| 6 | **Missing module and function docstrings** | Pylint | Functions had no descriptions. | Added a module docstring at the top and short descriptive docstrings for each function. |  **Medium** |
| 7 | **Unused import** | Flake8 | `import logging` | Removed the unused import line. |  **Low** |

---

##  Deliverable 3 — Reflection Answers

### **1. Which issues were the easiest to fix, and which were the hardest? Why?**
The easiest issues to fix were the **removal of the `eval()` statement** and replacing the **mutable default argument** (`logs=[]`).  
They required straightforward edits that did not affect the rest of the code.  

The hardest issue to fix was the **bare `except:` block**, since I had to identify the correct exception type (`KeyError`) and ensure that error handling didn’t break functionality.  
Fixing file handling using `with open()` also required understanding Python’s file context management and encoding.

---

### **2. Did the static analysis tools report any false positives? If so, describe one example.**
Yes.  
**Pylint** reported `W0603: Using the global statement` for the variable `stock_data`.  
However, this was not actually an issue because the global variable is necessary to share data between functions in this small script.  
Therefore, it can be considered a *false positive* in this context.

---

### **3. How would you integrate static analysis tools into your actual software development workflow?**
Static analysis tools can be integrated both **locally** and in **CI/CD pipelines**:

- **Local development:** Add a pre-commit hook using the `pre-commit` framework to automatically run Bandit, Pylint, and Flake8 before every commit.  
- **Continuous Integration (CI):** Configure GitHub Actions or Jenkins to run these tools automatically on each push or pull request.  
If any high-severity Bandit issues or Pylint errors are found, the pipeline can block the merge until the issues are resolved.

---

### **4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**
After applying all fixes:
- **Code quality** improved — all dangerous and unsafe code was removed.  
- **Readability** increased — naming conventions and docstrings make the code easy to understand.  
- **Robustness** improved — safe file handling and specific exceptions prevent unexpected crashes.  
- **Maintainability** was enhanced — fewer warnings, clean structure, and adherence to PEP8 make future modifications easier.  

Overall, the code is now more **secure, readable, and professional**.

---

## ⚙️ How to Run the Fixed Code

#### ** Clone or open the repository**
```bash
git clone https://github.com/Riha007/inventory_system_lab5.git
cd inventory_system_lab5
