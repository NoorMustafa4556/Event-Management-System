# Event Management System

A robust and user-friendly web application built with Python and Django for managing and organizing events. This system allows users to browse upcoming events, register for them, and track their registrations, while providing administrators with a powerful dashboard to manage events and participants.

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
    cd Event-Management-System
    ```

2.  **Create and Activate a Virtual Environment:**
    *   **On Windows:**
        ```bash
        python -m venv env
        .\env\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        python3 -m venv env
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

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---
