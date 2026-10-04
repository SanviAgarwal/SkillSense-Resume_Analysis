# 🧠 SkillSense — Resume Analysis That Tells You What's Missing

> A Streamlit web platform that doesn't just parse your resume — it tells you which role your skills point to, what's missing for that role, how your resume reads to a recruiter, and what to learn next.

---

## 🔍 The Problem

Most students and freshers send out resumes blind. They don't know whether their skills actually match the role they want, which sections recruiters expect to see, or what to learn to close the gap. Generic advice ("add more projects") doesn't help much, and paid resume reviewers don't scale.

This project asks a practical question:

> **Given just a PDF resume, can a system infer the target field, point out the skill gaps, and hand back concrete next steps — instantly, and with no manual review?**

SkillSense answers it end to end: upload a resume, get an analysis, and (on the admin side) see aggregate trends across every resume that has been uploaded.

---

## ✨ What Makes This Project Different

| Typical Resume Checker                  | SkillSense                                                                                              |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Gives a score and nothing else          | **Skills → field → missing skills → courses** in one flow                                               |
| Generic tips for everyone               | **Field-specific skill gaps** across Data Science, Web, Android, iOS and UI/UX                          |
| Stops at feedback                       | **Curated course and certificate recommendations**, with an adjustable number of suggestions            |
| Single-user tool                        | **Separate User and Admin sides** — admins get a data table, CSV export and analytics charts            |
| Throws the data away                    | Every analysis is **stored in MySQL**, so trends across candidates can be studied                       |
| Feedback only                           | **Bonus resume-writing and interview videos** pulled in alongside the analysis                          |

---

## 🎯 Features

**For users**
- 🔐 Registration and login with secure password handling
- 📄 Resume upload (PDF) with an inline preview
- 🧾 Automatic extraction of name, email, contact number, page count and skills
- 🎚️ Experience level inferred from resume length — Fresher / Intermediate / Experienced
- 🎯 Target-field prediction from the skills found on the resume
- 💡 Recommended skills for the predicted field, shown as tags
- 🎓 Course and certificate recommendations (choose 1–10)
- ✅ Resume tips — checks for Objective, Declaration, Hobbies/Interests, Achievements and Projects
- 📝 Resume score out of 100
- 🎬 Bonus videos on resume writing and interview preparation

**For admins**
- 📊 Full table of every analysed resume
- ⬇️ One-click CSV download of user data
- 🥧 Pie charts of predicted fields and candidate experience levels

---

## 🛠️ Tech Stack

| Library / Tool        | Purpose                                                     |
| --------------------- | ----------------------------------------------------------- |
| `streamlit`           | Web interface for both user and admin sides                 |
| `pyresparser`         | Extracting structured fields (name, email, skills) from resumes |
| `pdfminer3`           | Raw text extraction, used for the resume-section checks     |
| `nltk` / `spacy`      | NLP backbone used by the parser                             |
| `pymysql` + MySQL     | Persistent storage of every analysis                        |
| `streamlit-tags`      | Interactive skill tags                                      |
| `plotly`              | Admin-side analytics charts                                 |
| `pandas`              | Tabulating and exporting user data                          |
| `yt-dlp` / `pafy`     | Fetching titles for the bonus videos                        |
| `Pillow`              | Logo and image handling                                     |

---

## 📁 Project Structure

```
SkillSense-Resume_Analysis/
│
├── App.py                     ← Main Streamlit app (user + admin flows)
├── courses.py                 ← Course lists per field + resume / interview video links
├── Logos.png                  ← App logo
├── logo2.png                  ← Secondary logo
├── use case diagram.pdf       ← Use-case diagram of the system
├── Uploaded_Resumes/          ← Created locally; resumes are saved here on upload
└── README.md                  ← This file
```

---

## ⚙️ How It Works

1. **Upload** — the user uploads a PDF resume; it is saved and previewed in the page.
2. **Parse** — `pyresparser` pulls out the name, email, phone number, page count and skills, while `pdfminer3` extracts the full text.
3. **Level** — page count sets the experience level: 1 page → Fresher, 2 pages → Intermediate, 3+ pages → Experienced.
4. **Field prediction** — each extracted skill is matched against keyword lists for five fields:

   | Field            | Example trigger keywords                      |
   | ---------------- | --------------------------------------------- |
   | Data Science     | tensorflow, keras, pytorch, machine learning, streamlit |
   | Web Development  | react, django, node js, php, laravel, angular js |
   | Android          | android, flutter, kotlin, kivy                |
   | iOS              | ios, swift, cocoa, xcode                      |
   | UI/UX            | figma, adobe xd, wireframes, prototyping      |

5. **Gap analysis** — once a field is identified, the app lists the skills that field typically expects, so the user can see what their resume is missing.
6. **Recommendations** — a randomised set of relevant courses and certificates for that field.
7. **Resume tips and score** — the resume text is scanned for the sections recruiters expect, and each one found adds to the score.
8. **Store** — the result is saved to MySQL for the admin dashboard.

---

## ▶️ How to Run

**1. Install dependencies**

```
python -m venv .venv && source .venv/bin/activate
pip install streamlit pandas pyresparser pdfminer3 streamlit-tags pillow pymysql pafy yt-dlp plotly nltk spacy
python -m spacy download en_core_web_sm
```

**2. Set up MySQL**

Create a database named `uploaded_cv` and update the connection details in `App.py` (host, user, password). The `user_data` table is created automatically on first run.

**3. Create the upload folder**

```
mkdir Uploaded_Resumes
```

**4. Launch the app**

```
streamlit run App.py
```

> ⚠️ Run the command from the repo root so the app can find its assets and the upload folder.

---

## 🧪 Resume Scoring

The score is rule-based and transparent — each section found in the resume adds 20 points:

| Section checked            | Points |
| -------------------------- | ------ |
| Objective                  | 20     |
| Declaration                | 20     |
| Hobbies / Interests        | 20     |
| Achievements               | 20     |
| Projects                   | 20     |
| **Total**                  | **100** |

It measures **completeness of structure**, not the quality of the writing — the app says so explicitly next to the score.

---

## 🧠 Key Insights

- **Skill gaps are more useful than scores.** Telling a candidate *which* skills their target field expects is far more actionable than a number.
- **Combining a parser with raw-text checks works well.** `pyresparser` gives structured fields; `pdfminer3` text lets us check for sections the parser doesn't expose.
- **Storing every analysis turns a tool into a dataset.** The admin charts show which fields and experience levels dominate the uploads, something a stateless checker could never offer.
- **Keyword matching is simple but predictable** — easy to explain and debug, at the cost of missing skills not on the lists.

---

## ⚠️ Limitations

In the interest of being upfront about what this does and doesn't do:

- **Field prediction is keyword-based**, and the first matching skill decides the field, so resumes spanning several fields get a single label.
- **Experience level comes from page count**, which is a rough proxy, not a measure of real experience.
- **The score checks for section headings**, so a resume that uses different wording ("Academic Projects" is fine, "Work Samples" is not) can be under-scored.
- **Course lists are curated by hand** in `courses.py` and need periodic updating.
- Only **PDF** resumes are supported.

---

## 🚀 Future Improvements

- **Job-description matching** — compare a resume against a pasted job description and report missing keywords.
- **ML-based field classification** — replace keyword lists with a trained text classifier and report its accuracy.
- **Multi-label prediction** — show the top 2–3 fields instead of one.
- **Content-quality scoring** — score bullet points on action verbs and measurable impact, not just section presence.
- **Secrets management** — move database and admin credentials into environment variables.
- **Deployment** — host the app and move to a managed database.

---

## 🧠 What I Learned

Building SkillSense showed me that a useful tool is mostly about what happens *after* the analysis: a score on its own is forgettable, but a skill gap with a course attached gives someone a next step. I also learned how much of a "smart" feature is plain, explainable logic done carefully, and how important it is to be honest about its limits.

---

## 👥 Team

Built collaboratively by:

- **Shanvi Agarwal** — [LinkedIn](https://www.linkedin.com/in/shanvi-agarwal-93b38928b)
- **Anshika Agrawal** — [LinkedIn](https://www.linkedin.com/in/anshika-agrawal-417305293)
- **Swati Chaudhary** — [LinkedIn](https://www.linkedin.com/in/swati-chaudhary-636039290)
- **Sumit Pilaniya** — [LinkedIn](https://www.linkedin.com/in/sumit-pilaniya-1b663828a)

🐙 [GitHub](https://github.com/SanviAgarwal)
