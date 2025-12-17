# Mining IT Support Incident Analysis

## ► Project Overview
This project analyses IT support incidents from mining operations to understand:
- Common system issues
- Downtime impact
- Unresolved high-risk incidents

**Goal:** Support better prioritisation of IT support work and reduce operational disruptions at mine sites.

The dataset represents typical IT incidents in mining environments, such as:
- System outages
- Network failures
- Software issues affecting production systems

---

## ► Dataset Description
The dataset includes **10 IT support incidents** recorded across two mining sites:

**Sites:**
- Pilbara
- Kalgoorlie

**Systems Covered:**
- Drill Control System
- Truck Dispatch System
- Site Network
- Maintenance System

**Each incident record includes:**
- Incident ID and date
- Site and affected system
- Issue type and severity
- Downtime duration (minutes and hours)
- Resolution status

---

## ► Key Analysis Performed

**■ 1. Common IT Issues**  
The most frequent problems identified:
- Network failures
- Software bugs
- User-related errors

> Network issues appeared most often and generally caused longer downtime.

**■ 2. Downtime Impact by System**  
Total downtime was calculated for each system to identify which systems have the greatest operational impact:
- Truck Dispatch System – highest total downtime
- Drill Control System – high total downtime

> These systems are critical to daily mining operations; outages directly affect productivity.

**■ 3. High-Severity Unresolved Incidents**  
Two high-severity incidents were identified as unresolved:
- Network failure impacting the Site Network at Kalgoorlie
- Network failure affecting the Maintenance System at Pilbara

> These incidents represent higher operational risk and would normally require escalation in a real IT support environment.

---

## ► Key Takeaways
- Network reliability is a major issue across multiple systems and sites
- Core operational systems cause the most disruption when incidents occur
- Tracking unresolved high-severity incidents is critical for reducing downtime and operational risk

---

## ► Tools Used
- Python
- Pandas
- VS Code
