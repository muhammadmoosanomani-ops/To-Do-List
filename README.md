# 📝 To-Do List

A lightweight, fully functional full-stack web application that allows users to manage their daily schedules efficiently. This project tracks and organizes your operations in real-time, designed with a modular, hierarchical architecture.

[![Deployment Status](https://img.shields.io/badge/Live-Demo-blue?style=for-the-badge&logo=vercel)](https://your-app-name.vercel.app)

> **Live Demo:** [https://to-do-list-nine-vert-17.vercel.app/](https://to-do-list-nine-vert-17.vercel.app/)

---

## 🚀 Features & CRUD Operations

This application utilizes a standard relational database structure to handle full **CRUD (Create, Read, Update, Delete)** operations natively:

* **Create (POST):** Users can instantly type and add a task to the queue from the home page dashboard.
* **Read (GET):** The application fetches and displays all tasks dynamically, organized cleanly in a structural tracking table sorted by their exact creation timestamp.
* **Update (GET/POST):** Selecting the "Edit" prompt seamlessly routes users to an independent workspace where they can modify the content of a specific task and save updates directly back to the infrastructure database.
* **Delete (GET):** Clean, immediate click-to-delete logic allows users to purge finished or irrelevant entries instantly.

---

## 🛠️ Built With

* **Backend Framework:** Python 3 + Flask
* **Database Management:** Flask-SQLAlchemy (relational Object-Relational Mapping system)
* **Database Engine:** SQLite
* **Frontend Engine:** Jinja2 Template Engine (utilizing hierarchical layout inheritance)
* **Styling Engine:** Pre-compiled Sass/SCSS to static standard CSS layouts

---

## 📁 Repository Structure

The architecture of this repository separates the data infrastructure, static digital assets, and structural interfaces cleanly:

```text
To-Do List/
├── .vscode/               # Local editor workspaces
├── static/                # Asset pipeline
│   ├── styles.css         # Main pre-compiled visual stylesheet
│   └── styles.scss        # Raw development source code for styles
├── templates/             # Front-end design blueprints
│   ├── base.html          # Global structural blueprint layout
│   ├── index.html         # Main dashboard and task list viewport
│   └── edit.html          # Independent task editor component
├── app.py                 # Core routing, control architecture, and configuration
├── requirements.txt       # Frozen platform dependency manifest
├── vercel.json            # Deployment configuration matrix
└── README.md              # Documentation manual
