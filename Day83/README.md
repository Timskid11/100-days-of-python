# 🔐 ADMIN MANUAL: Managing Your Site

Since this is a security-focused portfolio, the admin routes are hidden from the navigation bar. 
Use this guide to access your CMS (Content Management System).

## 1. Important URLs (Bookmark These!)

| Action | URL Route | Description |
| :--- | :--- | :--- |
| **Login** | `/login` | The entry point. You must be logged in to edit anything. |
| **Logout** | `/logout` | Ends your session securely. |
| **New Project** | `/add-project` | Upload a new project image, title, and GitHub link. |
| **New Job** | `/add-experience` | Add a new role to your timeline. |
| **Edit Intro** | `/edit-section/intro` | Change your photo or text in the top "Intro" section. |
| **Edit About** | `/edit-section/about` | Change the text in the "About Me" section. |
| **Register** | `/register` | **WARNING:** Keep this code commented out in `main.py` after you create your account. |

## 2. How to Edit Content
There are two ways to edit content:

### Method A: The Visual Way (Easiest)
1.  Go to `/login` and sign in.
2.  Go to the **Home Page**.
3.  Look for the yellow **[EDIT THIS]** buttons or the **+ Add Project** buttons directly on the page.
4.  Clicking them will take you to the correct form automatically.

### Method B: The Manual Way (If buttons are missing)
1.  Type the URL manually (e.g., `yourwebsite.com/add-project`).
2.  Fill out the form and hit Submit.

## 3. Database Management
* **Where is my data?** It is stored in `portfolio.db` (SQLite).
* **Resetting the DB:** If you break something or want to start fresh, simply **delete** the `portfolio.db` file. The next time you run `python main.py`, the app will generate a brand new, clean database for you.

## 4. Twilio Setup (SMS Alerts)
If the contact form stops sending SMS:
1.  Check your Twilio Dashboard.
2.  Ensure you have `$$` credits on your trial account.
3.  Verify the `TWILIO_SID` and `TWILIO_AUTH_TOKEN` in `main.py` (or your Dashboard environment variables) match your Twilio console.