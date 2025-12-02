# 📊 Grammys Website Performance & Segmentation Analysis

**Overview**: Data analysis project evaluating the digital strategy of The Recording Academy following their 2022 decision to split their web presence into two sites: the high-volume `grammy.com` and the industry-focused `recordingacademy.com`.

The analysis focuses on key web performance indicators (KPIs) to assess the impact of the separation and identify optimization opportunities for the Academy's digital properties, with findings relevant to digital operations and marketing strategy.

---

## 🔑 Key Insights & Business Impact

* **Audience Split Validation**: The data confirms a successful segmentation. `grammy.com` drives high-volume, low-engagement traffic, while `recordingacademy.com` captures lower volume but significantly higher engagement (higher pages/session and average session duration).
* **Mobile Optimization Gap**: Analysis of the combined data revealed that while `grammy.com` dominates desktop traffic, the overall mobile engagement metrics **lag behind key competitors (e.g., AMA)**, pointing to a critical need for mobile UX/performance optimization to capture a younger, mobile-first audience.
* **Awards Effect**: Spikes in traffic and session metrics are directly correlated with `awards_week` and `awards_night` flags, confirming the massive ROI of the awards ceremony as a traffic driver.

---

## 🛠️ Technical Stack & Project Components

* **Methodology**: Data loading, cleaning, KPI calculation (Bounce Rate, Pages per Session), time-series analysis, and comparative benchmarking.
* **Tools**: Python (Pandas for data manipulation, Plotly for interactive visualization, NumPy for data generation).
* **Data**: Hypothetical daily web metrics data (visitors, sessions, bounce rates, etc.) for both domains, simulated using `generate_data.py`.

| File / Folder | Description |
| :--- | :--- |
| `notebooks/` | Contains the core Jupyter Notebook (`David_Ortiz-Analyzing-Website-Performance-Grammys.ipynb`) with the full analysis and visualizations. |
| `generate_data.py` | Python script to programmatically create the runnable CSV files expected by the notebook, ensuring reproducibility. |
| `requirements.txt` | Lists all necessary Python dependencies (Pandas, Plotly, etc.). |

## ▶️ How to Run Locally

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/grammys-web-analytics.git](https://github.com/your-username/grammys-web-analytics.git)
    cd grammys-web-analytics
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Generate Data Files:**
    ```bash
    python generate_data.py
    ```
4.  **Launch Analysis:** Open the Jupyter Notebook in the `notebooks/` folder to view the full analysis.
