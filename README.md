
# 🏥 US Healthcare Case Study – Data Analyst Portfolio Project

## 📌 Overview

This project presents an analytical case study for the **US Healthcare Department**, based on data from **100 hospitals**. The dataset includes patient demographics, admission types, billing information, and insurance details.

The goal was to uncover actionable insights to help **executives make data-driven decisions** regarding pricing, patient care, and hospital resource management.

---

## 🗂️ Dataset Description

- **Records:** Patients admitted to 100 hospitals (over 2,000 rows)
- **Features:** Patient demographics, admission dates, medical conditions, insurance types, and billing amounts
- **Time Period:** 2018 – 2023

---

## 🎯 Project Objectives & Insights

### 1. 📊 **Demographic Analysis of Medical Conditions**

**Objective:**  
Identify the most prevalent medical conditions across demographic groups.

**Approach:**  
- Buckets created for **age**, **gender**, and **income** groups  
- Conditions aggregated per demographic segment  
- Designed to be **mutually exclusive and collectively exhaustive**

**Key Insight:**  
> Certain conditions like hypertension and diabetes are highly concentrated in older male patients with low-to-mid income levels.

---

### 2. 💰 **Patient Price Optimization**

**Objective:**  
Recommend ways for patients to reduce their healthcare costs.

**Approach:**  
- Compared billing amounts across **insurance providers**, **admission types**, and **demographic buckets**
- Merged with findings from demographic analysis

**Key Insight:**  
> Patients with private insurers like *Cigna* and *Aetna* have higher bills than Medicare patients. Elective admissions and younger age groups consistently show lower average bills.

---

### 3. 🏥 **Hospital Resource Management**

**Objective:**  
Help hospitals better manage workload and admissions.

**Approach:**  
- Time-series analysis of **admission volume**
- Segmented by **admission type** and **monthly trends**

**Key Insight:**  
> Admission spikes in **January and August–October**, driven largely by emergency visits. Recommend optimizing staff and beds around these periods.

---

## 📈 Visual Dashboard

> ✅ [**View Interactive Dashboard**](https://your-link-here.com)

![Dashboard Screenshot](dashboard/screenshot.png)

Includes:
- Top insurance providers
- Average hospital stay duration
- Monthly admission trends
- Billing breakdown by provider

---

## 🧪 Tools Used

- **Python**: `pandas`, `matplotlib`, `seaborn`
- **SQL**: Basic joins and aggregations
- **Excel**: Initial EDA and filtering
- **Power BI / Tableau / HTML**: Final interactive dashboard
- **Git & GitHub**: Version control and project documentation

---

## 📁 Project Structure

```
project-root/
├── data/                     # Raw and cleaned data
├── notebooks/                # Jupyter notebooks for EDA and analysis
├── scripts/                  # SQL queries, Python scripts
├── outputs/
│   ├── charts/               # Static visualizations
│   ├── dashboard/            # HTML/PDF dashboards
│   └── presentation/         # Slide deck
├── dashboard/                # Interactive HTML dashboard
└── README.md
```

---

## ✅ Final Recommendations

- 📉 **Patients**: Choose insurers and admission types based on cost patterns
- 🏥 **Hospitals**: Manage resources better during seasonal spikes
- 📊 **Executives**: Use demographic-driven care planning for high-risk groups

---

## 🔗 Contact

Made with 💙 by SainiRahul
📫 Sainirahul430@gmail.com • 🌐 www.linkedin.com/in/rahul-saini-data-analyst
