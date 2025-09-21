# Event Management System

A robust and user-friendly web application built with Python and Django for managing and organizing events. This system allows users to browse upcoming events, register for them, and track their registrations, while providing administrators with a powerful dashboard to manage events and participants.

## 📸 Project Screenshots


<p align="center">
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Event-Management-System/main/myproject/myapp/static/images/1.jpg" alt="Screenshot 1" width="30%" />
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Event-Management-System/main/myproject/myapp/static/images/2.jpg" alt="Screenshot 2" width="30%" />
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Event-Management-System/main/myproject/myapp/static/images/3.jpg" alt="Screenshot 3" width="30%" />
</p>


<p align="center">
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Event-Management-System/main/myproject/myapp/static/images/4.jpg" alt="Screenshot 4" width="30%" />
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Event-Management-System/main/myproject/myapp/static/images/5.jpg" alt="Screenshot 5" width="30%" />
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Event-Management-System/main/myproject/myapp/static/images/6.jpg" alt="Screenshot 6" width="30%" />
</p>


## ✨ Core Features

*   **User Authentication:**
    *   Secure user signup and login functionality.
    *   Automatic creation of a `Participant` profile for each new user.
*   **Event Catalog:**
    *   A dynamic homepage displaying all available events (e.g., Workshops, Seminars, Conferences).
    *   Ability to categorize events for easy browsing.
    *   Search functionality to find specific events.
*   **Event Registration:**
    *   Authenticated users can register for any available event.
    *   A user can only register for a specific event once to prevent duplicate entries.
    *   The registration button is disabled if the user has already registered.
*   **Participant Dashboard:**
    *   A dedicated "My Registrations" page where users can view all the events they have registered for and see their status.
*   **Admin Powerhouse:**
    *   Full control over the system via the Django admin panel.
    *   Admins can create, update, and delete `Events` and `Categories`.
    *   View all `Registrations` and manage participant lists for each event.

## 🛠️ Technology Stack

*   **Backend:** Python, Django
*   **Database:** SQLite 3 (Default)
*   **Frontend:** HTML, Bootstrap 5 (or your chosen framework)

## 🚀 Getting Started

Follow these steps to set up the project on your local machine for development and testing.

### Prerequisites

*   Python (3.8 or higher)
*   pip (Python package manager)
*   Git (for cloning the repository)

### Installation Guide

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/NoorMustafa4556/Event-Management-System.git
    ```
    ```bash
    cd Event-Management-System
    ```

2.  **Create and Activate a Virtual Environment:**
    *   **On Windows:**
        ```bash
        python -m venv env
        ```
        ```bash
        .\env\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        python3 -m venv env
        ```
        ```bash
        source env/bin/activate
        ```

3.  **Install Required Packages:**
    This command will install all the necessary dependencies listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Database Migrations:**
    This command sets up your database schema based on the models defined in the project.
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser:**
    This account will have full access to the Django admin panel.
    ```bash
    python manage.py createsuperuser
    ```
    You will be prompted to enter a username, email, and password.

6.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    Your Event Management System will now be live at `http://127.0.0.1:8000/`.

## ⚙️ How to Use the System

### As an Administrator:

1.  Navigate to `http://127.0.0.1:8000/admin/`.
2.  Log in using your superuser credentials.
3.  **First, create some `Event Categories`** (e.g., "Technology", "Health", "Business").
4.  **Next, create new `Events`**, providing details like title, description, date, and assign them to a category.

### As a User:

1.  Go to the homepage at `http://127.0.0.1:8000/`.
2.  **Sign up** for a new account.
3.  **Log in** with your new credentials.
4.  Browse the list of available events.
5.  Click on an event to view its details and click the **"Register"** button.
6.  Visit the **"My Registrations"** page to see a list of all your registered events.

## 🤝 How to Contribute

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

# 👋 Hi, I'm Noor Mustafa

A passionate and results-driven **Flutter Developer** from **Bahawalpur, Pakistan**, specializing in building elegant, scalable, and high-performance cross-platform mobile applications using **Flutter** and **Dart**.

With a strong understanding of **UI/UX principles**, **state management**, and **API integration**, I aim to deliver apps that are not only functional but also user-centric and visually compelling. My development approach emphasizes clean code, reusability, and performance.

---

## 🚀 What I Do

- 🧑‍💻 **Flutter App Development** – I build cross-platform apps for Android, iOS, and the web using Flutter.
- 🔗 **API Integration** – I connect apps to powerful RESTful APIs and third-party services.
- 🎨 **UI/UX Design** – I craft responsive and animated interfaces that elevate the user experience.
- 🔐 **Authentication & Firebase** – I implement secure login systems and integrate Firebase services.
- ⚙️ **State Management** – I use Provider, setState, and Riverpod (in-progress) for scalable app architecture.
- 🧠 **Clean Architecture** – I follow MVVM and MVC patterns for maintainable code.

---


## 🌟 Projects I'm Proud Of

- 🌤️ **[Live Weather Check App](https://github.com/NoorMustafa4556/Live-Weather-Check-App)** – Real-time weather forecast using OpenWeatherMap API  
- 🤖 **[AI Chatbot (Gemini)](https://github.com/NoorMustafa4556/Ai-ChatBot)** – Conversational AI chatbot powered by Google’s Gemini  

- 🍔 **[Recipe App](https://github.com/NoorMustafa4556/Recipe-App)** – Discover recipes with images, categories, and step-by-step instructions  

- 📚 **[Palindrome Checker](https://github.com/NoorMustafa4556/Palindrome-Checker-App)** – A Theory of Automata-based project to identify palindromic strings  

> 🎯 Check out all my repositories on [github.com/NoorMustafa4556](https://github.com/NoorMustafa4556?tab=repositories)

---

## 🛠️ Tech Stack & Tools

| Area                | Tools/Technologies |
|---------------------|--------------------|
| **Languages**       | Dart, JavaScript, Python (basic) |
| **Mobile Framework**| Flutter            |
| **Backend/Cloud**   | Firebase (Auth, Realtime DB, Storage), Django, Flask |
| **Frontend (Web)**  | React.js (basic), HTML, CSS, Bootstrap |
| **State Management**| Provider, setState, Riverpod (learning) |
| **API & Storage**   | REST APIs, HTTP, Shared Preferences, SQLite |
| **Design**          | Material, Cupertino, Lottie Animations, Gradient UI |
| **Version Control** | Git, GitHub        |
| **Tools**           | Android Studio, VS Code, Postman, Figma (basic) |

---

## 🧰 Tech Toolbox

<p align="left">
  <img src="https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white"/>
  <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/>
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
</p>

---

## 📈 Current Focus

- 💡 Enhancing Flutter animations and transitions
- 🤖 Implementing AI-based logic with Google Gemini API
- 📲 Building portfolio-level applications using full-stack Django & Flutter

---

## 📫 Let's Connect!

<p align="left">
  <a href="https://x.com/NoorMustafa4556" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="X / Twitter" height="30" width="40" />
  </a>
  <a href="https://www.linkedin.com/in/noormustafa4556/" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="30" width="40" />
  </a>
  <a href="https://www.facebook.com/NoorMustafa4556" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="Facebook" height="30" width="40" />
  </a>
  <a href="https://instagram.com/noormustafa4556" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram" height="30" width="40" />
  </a>
  <a href="https://wa.me/923087655076" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/whatsapp.svg" alt="WhatsApp" height="30" width="40" />
  </a>
  <a href="https://www.tiktok.com/@noormustafa4556" target="blank">
    <img src="https://cdn-icons-png.flaticon.com/512/3046/3046122.png" alt="TikTok" height="30" width="30" />
  </a>
</p>

- 📍 **Location:** Bahawalpur, Punjab, Pakistan

---

> _“Learning never stops. Every app I build makes me a better developer — one widget at a time.”_

---



1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---
