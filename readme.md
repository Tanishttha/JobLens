<h1 align="center">JobLens</h1>
<h2 align="center">JobLens is an AI-powered job posting scam-detection and resume-matching platform. The system combines a Groq-based large language model, resume parsing, and a Chrome extension to help job seekers instantly verify a posting's legitimacy and see how well their resume matches its requirements.</h2>

<h2>Live Demo</h2>

```bash
Frontend (Vercel): https://fake-job.vercel.app
Backend (Render):  https://fake-job-api-xeuu.onrender.com
```

> **Note:** The backend is hosted on Render's free tier. If it hasn't been used recently, it goes to sleep — the first request can take **up to 2 minutes** to respond while the server wakes up. Please wait a couple of minutes before retrying if the analysis seems stuck on first load.

<h2>Features</h2>

* AI-powered job posting scam classification (genuine / suspicious / uncertain)
* Automatic job detail extraction — title, company, location, work mode, salary, and skills
* Resume-to-job skill matching with match score, matched keywords, and missing keywords
* Chrome extension for one-click analysis of any job posting on the web
* Google OAuth login with credit-based usage
* Razorpay-powered credit recharge system
* Resume upload and parsing (PDF / DOCX)
* Standalone web app and browser extension, both backed by the same API

<h2>Technology Stack</h2>

<h3>Frontend</h3>

* React
* Vite
* Chrome Extension (Manifest V3)

<h3>Backend</h3>

* Python
* FastAPI
* MongoDB (via Motor)

<h3>AI & Matching</h3>

* Groq LLM for scam classification and job-detail extraction
* Skill-matching engine using AI-extracted job skills as the primary source
* Resume parsing (PDF / DOCX)

<h3>Payments</h3>

* Razorpay (orders, signature verification, and webhook fallback)

<h2>Installation</h2>

<h3>Clone Repository</h3>

```bash
git clone https://github.com/USERNAME/JobLens.git
cd JobLens
```

<h3>Backend Setup</h3>

Create Virtual Environment

```bash
cd backend
python -m venv venv
```

<h3>Activate Virtual Environment</h3>

Windows

```bash
venv\Scripts\activate
```

macOS/Linux

```bash
source venv/bin/activate
```

<h3>Install Dependencies</h3>

```bash
pip install -r requirements.txt
```

<h3>Configure Environment</h3>

Copy `.env.example` to `.env` and fill in MongoDB, Google OAuth, Groq, and Razorpay credentials.

```bash
cp .env.example .env
```

<h3>Run Backend</h3>

```bash
uvicorn app.main:app --reload --port 8000
```

<h3>Backend will start on:</h3>

```bash
http://localhost:8000
```

<h3>Frontend Setup</h3>

Navigate to the project root:

```bash
cd ..
```

<h3>Install dependencies:</h3>

```bash
npm install
```

<h3>Run development server:</h3>

```bash
npm run dev
```

<h3>Frontend will start on:</h3>

```bash
http://127.0.0.1:5173
```

<h3>Chrome Extension Setup</h3>

1. Open `chrome://extensions` in Chrome.
2. Enable **Developer mode**.
3. Click **Load unpacked** and select the `extension/` folder.
4. Select any text on a job posting page to trigger analysis.

<h2>Usage</h2>

1. Launch the backend server.
2. Start the frontend application (or load the Chrome extension).
3. Sign in with Google.
4. Paste or select a job posting's text.
5. View the scam-likelihood classification and extracted job details.
6. Upload a resume to see the skill-match score, matched keywords, and missing keywords.
7. Recharge credits via Razorpay when needed.

<h2>Deployment</h2>

* **Frontend** — deployed on **Vercel**, built with `vite build`.
* **Backend** — deployed on **Render** as a FastAPI service behind Gunicorn/Uvicorn workers.
* **Database** — MongoDB.

> Since the backend runs on Render's free tier, it spins down after periods of inactivity. The very first request after idle time can take **around 2 minutes** to wake the server back up — this is expected behavior, not a bug.

<h2>Future Enhancements</h2>

* Persisted analysis history and dashboard
* Support for more resume formats
* Rate limiting and abuse protection on public endpoints
* Improved skill-matching for non-technical roles
* Mobile-friendly extension companion app

<h2>License</h2>

This project is intended for educational and research purposes.