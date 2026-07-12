# 🌍 Travel Intelligence AI

An AI-powered travel planning and budget optimization application built using **IBM watsonx Orchestrate**, **IBM Cloud**, **Python**, and **Streamlit**.

The application generates personalized travel itineraries and provides intelligent budget optimization based on user preferences.

---

# 📌 Project Overview

Travel Intelligence AI is an intelligent travel assistant that helps users plan their trips efficiently. It leverages IBM watsonx Orchestrate to generate customized travel plans and optimize travel budgets using Artificial Intelligence.

The application consists of two AI-powered modules:

- 🧳 AI Travel Planner
- 💰 AI Budget Optimizer

---

# 🚀 Features

## 🧳 AI Travel Planner

The Travel Planner generates a personalized itinerary based on:

- Source
- Destination
- Total Trip Duration
- Budget
- Number of Travelers
- Travel Type
- Interests

The generated itinerary includes:

- Trip Overview
- Day-wise Itinerary
- Recommended Attractions
- Accommodation Suggestions
- Transportation Recommendations
- Estimated Cost
- Packing Suggestions
- Safety Tips

---

## 💰 AI Budget Optimizer

The Budget Optimizer analyzes the travel budget and provides:

- Budget Allocation
- Budget Analysis
- Transportation Recommendation
- Money Saving Tips
- Hidden Expenses
- Budget Score

The optimization considers:

- Source
- Destination
- Budget
- Duration
- Number of Travelers
- Travel Type

---

# 🏗️ System Architecture

```

                               User
                                ⬇
                         Streamlit Web App
                                |
                                |
                        User Inputs & Requests
                                ⬇
                    IBM watsonx Orchestrate Agent
                                |
                                │
                            AI Processing
                                ⬇
                    Travel Intelligence AI Agent
                                │
                 ───────────────|─────────────────
                ⬇                                 ⬇
        AI Travel Itinerary              AI Budget Optimization
                │                                   │
                 ─────────────── ──────────────────
                                ⬇
                    Results displayed to User
```

---

# 🔄 Workflow

```
User Opens Application
          │
          ▼
Select Feature
(Trip Planner / Budget Optimizer)
          │
          ▼
Enter Travel Details
          │
          ▼
IBM IAM Authentication
          │
          ▼
IBM watsonx Orchestrate
          │
          ▼
Travel Intelligence AI Agent
          │
          ▼
AI Generated Response
          │
          ▼
Display Results in Streamlit
```

---

# 🛠️ Technologies Used

- Python
- Streamlit
- IBM Cloud
- IBM watsonx Orchestrate
- IBM IAM Authentication
- REST APIs
- Requests
- Python Dotenv

---

# 📂 Project Structure

```
Travel-Intelligence-AI/
│
├── app.py
│
├── pages/
│   ├── 1_Trip_Planner.py
│   └── 2_Budget_Optimizer.py
│
├── services/
│   └── orchestrate_service.py
│
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/travel-intelligence-ai.git
```

Go to the project folder

```bash
cd travel-intelligence-ai
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
WATSONX_API_KEY=YOUR_API_KEY
WATSONX_URL=YOUR_INSTANCE_URL
AGENT_ID=YOUR_AGENT_ID
```

Run the application

```bash
streamlit run app.py
```

---

# 🔐 IBM Cloud Services Used

- IBM Cloud
- IBM watsonx Orchestrate
- IBM Identity and Access Management (IAM)

---

# 🌟 Project Highlights

- AI-powered personalized travel planning
- AI-based travel budget optimization
- IBM watsonx Orchestrate integration
- Cloud-based architecture
- Interactive Streamlit interface
- Modular project structure
- Secure API authentication using IBM IAM

---

# 🎯 Future Scope

- Hotel Recommendation System
- Weather Integration
- PDF Report Generation
- Voice-based Travel Planning
- Multi-language Support
- Travel History

---

# 👩‍💻 Developer

**Haseena Rahaman**

B.Tech – Computer Science Engineering

---
