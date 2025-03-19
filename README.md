
# 🚀 **LLM-Powered Booking Analytics & QA System**

## 📚 **Project Overview**
This project builds an **AI-Powered Booking Analytics & QA System** that processes hotel booking data, generates insightful analytics, and answers booking-related queries using an LLM with **Retrieval-Augmented Generation (RAG)**.

---

## 🎯 **Objective**
- Analyze hotel booking data for trends, cancellation rates, and geographical distribution.
- Enable natural language Q&A using an open-source LLM.
- Build REST APIs for seamless interaction.

---

## 📄 **Dataset Overview**
- **Dataset Name:** Hotel Booking Demand Dataset
- **Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)
- **File Format:** CSV
- **Key Features:**
  - `hotel` – Type of hotel (City or Resort)
  - `lead_time` – Number of days between booking and arrival
  - `adr` – Average Daily Rate (Revenue per booking)
  - `is_canceled` – Whether a booking was canceled
  - `country` – Country of origin of guests
  - `arrival_date_year` – Year of booking arrival

---

## 🧼 **1. Data Collection & Preprocessing**
- Loaded dataset from Kaggle or a custom source.
- Performed:
  - Handling of missing values.
  - Date formatting and transformation.
  - Encoding categorical data for processing.
- Stored cleaned data in a structured format for analytics.

---

## 📊 **2. Analytics & Reporting**
### 🔎 **Implemented Analytics:**
- **Revenue Trends:** Visualized revenue trends over time.
- **Cancellation Rate:** Calculated cancellation percentage.
- **Geographical Distribution:** Analyzed booking patterns across regions.
- **Booking Lead Time:** Distribution of lead time for bookings.
- **Additional Insights:** Generated useful patterns and statistics.

---

## 🤖 **3. Retrieval-Augmented Question Answering (RAG)**
- **Vector Storage:** Used FAISS/ChromaDB to store vector embeddings of booking data.
- **LLM Integration:** Connected an open-source LLM (e.g., Llama 2, Falcon) to enable query responses.
- **Workflow:**
  1. Convert query to vector embedding.
  2. Search for relevant records in vector DB.
  3. Pass retrieved context to LLM for response generation.

### 🔥 **Sample Queries:**
- “Show me total revenue for July 2017.”
- “Which locations had the highest booking cancellations?”
- “What is the average price of a hotel booking?”

---

## 🛠️ **4. API Development**
- **Framework:** FastAPI for high-speed request handling.
- **Endpoints:**
  - `POST /analytics` → Returns booking insights.
  - `POST /ask` → Returns AI-powered responses.
  - `GET /health` → (Bonus) System health check.

---

## 📈 **5. Performance Evaluation**
- **Q&A Accuracy Evaluation:**
  - Validated AI-generated responses with sample queries.
  - Measured accuracy using precision and recall.
- **API Speed Optimization:**
  - Ensured API response time < 500ms for 95% queries.
  - Used load testing tools (Postman/JMeter) for optimization.

---

## 🚀 **6. Deployment & Submission**
### 🎁 **Deliverables:**
- **GitHub Repository:** Contains:
  - Complete Codebase with LLM, Analytics, and API.
  - Sample Test Queries with Expected Answers.
  - A Short Report explaining implementation choices & challenges.
- **Deployment Instructions:** Dockerfile for API deployment.

---

## 🎁 **Bonus Features (Optional)**
- **Real-Time Data Updates:** Database integration (PostgreSQL) to reflect live data.
- **Query History Tracking:** Store user queries and responses.
- **System Health API:** `GET /health` to check internal status.

---

##  **Setup Instructions**
### **Prerequisites**
- Python 3.8+  
- FastAPI, FAISS, Hugging Face Transformers, and Required Packages.
- 
###  ** Install Required Packages**
```bash
pip install -r requirements.txt
```

### ** Run FastAPI Server**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### ** API Endpoints**
- **POST /analytics:** Returns booking insights.  
- **POST /ask:** Returns AI-powered responses.  
- **GET /health:** Checks API health (optional).

---

##  **Usage Guide**
### **Query Examples:**
- POST `/analytics` → Get booking statistics.
- POST `/ask` with `{"query": "What is the revenue for July 2017?"}`  
- GET `/health` → System status check.

---

## **Challenges & Learnings**
- **Data Quality Issues:** Handling inconsistent date formats and missing values.
- **Vector Search Optimization:** Fine-tuned FAISS parameters for high recall.
- **LLM Fine-Tuning:** Improved query response quality through iterative testing.

---

## **Future Enhancements**
- Real-time data ingestion for dynamic updates.
- Implement JWT Authentication for API security.
- Advanced query personalization based on user preferences.


---

## **Links**
- [Dataset Link](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)  
  
