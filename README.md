# Blood Bank Management System
> **Intelligent Blood Inventory & Donor Management System**

## The Problem
In many campus or local blood drives, tracking **donor eligibility** is manual and prone to error. Donating too frequently is a health risk. **Blood Bank Management System** automates this by calculating medical cooling periods and providing a secure bridge between hospitals and donors.

##  Core Features

###  For Hospital Staff (Admin)
- **Donor Lifecycle Management:** Register, update, and manage donors.
- **Automated Eligibility:** Real-time calculation of `Next Eligible Date` (90-day interval).
- **Inventory Control:** Full CRUD operations on the blood database.

###  For Hospitals (Receivers)
- **Live Inquiry:** Instant view of available blood units across all groups.
- **Privacy-First Design:** View-only access to prevent unauthorized data tampering.
- **Urgency Indicators:** Visual badges for critical blood types (O-ve, AB-ve).

---

##  Architecture



**Blood Link Pro** follows a clean **Model-View-Controller (MVC)** pattern:
- **Models:** MySQL tables (`users`, `donors`) ensuring data persistence.
- **Views:** Jinja2 templates styled with Bootstrap 5 for a mobile-responsive UI.
- **Controllers:** Flask routes in `app.py` handling the business logic and session security.

---

##  Quick Start

### 1. Prerequisites
- Python 3.9+
- MySQL Server 8.0+

### 2. Database Initialization
Execute the following in **MySQL Workbench**:
```sql
CREATE DATABASE blood_bank;
-- Import schema.sql found in the root directory

### 3.Run the server
python app.py
