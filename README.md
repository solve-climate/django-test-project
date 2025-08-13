# Django Test Project

This is a sandbox for the Solve Climate platform - a development environment for building climate-related solutions with user authentication and team management.

## Prerequisites

Before setting up the project, you'll need:

### 1. Node.js
Download and install Node.js v22.18.0. You have two options:
- **Option A**: Download directly from [nodejs.org](https://nodejs.org/)
- **Option B**: Use a Node Version Manager ([installation guide](https://www.freecodecamp.org/news/node-version-manager-nvm-install-guide/))

**💡 Tip**: We recommend using a Node Version Manager as different projects may require different Node.js versions.

### 2. Conda
Install [Conda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/) for Python environment management.

## Setup Instructions

### Step 1: Create Python Environment

Create a new conda environment with the required packages:

```bash
# Create environment
conda create -n solve-climate-test-env python=3.13 

# Activate environment  
conda activate solve-climate-test-env

# Install Python packages
pip install django
pip install asgiref
pip install sqlparse
pip install django-browser-reload
```

**Note**: The `envs/environment.yml` file is currently outdated, so manual installation is required.

### Step 2: Install Node.js Dependencies

```bash
# Install npm packages
npm install
```

### Step 3: Setup Database

Navigate to the Django project directory and set up the database:

```bash
cd testwebsite

# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create a superuser account (optional but recommended)
python manage.py createsuperuser
```

### Step 4: Start Development Services

You'll need to run two processes simultaneously:

**Terminal 1** - Start CSS watch process (for Tailwind CSS):
```bash
npm run watch:css
```

**Terminal 2** - Start Django development server:
```bash
# Make sure you're in the testwebsite directory
cd testwebsite

# Start the server
python manage.py runserver
```

### Step 5: Access the Application

Once both services are running:
- **Main Application**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/ (use your superuser credentials)

## Quick Start (Subsequent Times)

After your initial setup is complete, starting the project on subsequent occasions only requires these steps:

### For Daily Development

1. **Activate your conda environment:**
   ```bash
   conda activate solve-climate-test-env
   ```

2. **Start both development services:**
   
   **Terminal 1** - CSS watch process:
   ```bash
   npm run watch:css
   ```
   
   **Terminal 2** - Django server:
   ```bash
   cd testwebsite
   python manage.py runserver
   ```

3. **Access the application at:** http://127.0.0.1:8000/

### Only Run These When Needed

- **Database migrations** (only if models changed):
  ```bash
  cd testwebsite
  python manage.py makemigrations
  python manage.py migrate
  ```

- **Install new dependencies** (only if package.json or requirements change):
  ```bash
  npm install  # For new Node packages
  pip install <package-name>  # For new Python packages
  ```

