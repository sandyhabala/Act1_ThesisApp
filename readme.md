# Documentation

This document provides an overview of the functionalities, usage instructions, and key components of our thesis searching website.

## Overview

Thesis Seeker is a web application designed to simplify the process of finding and accessing academic theses across various disciplines. Whether you're a student, researcher, or academic professional, Thesis Seeker offers a user-friendly platform to explore a wide range of scholarly works.

## Getting Started

To get started with Thesis Seeker, follow these steps:

1. **Installation**: Clone the repository or download the source code.
2. **Configuration**: Customize settings such as database configuration, static files, and URLs as per your requirements.
3. **Dependencies**: Install dependencies using `pip install -r requirements.txt`.
4. **Database Setup**: Set up the database and perform migrations using `py manage.py migrate`.
5. **Run the Server**: Start the development server using `py manage.py runserver`.
6. **Access the Website**: Visit `http://localhost:8000` in your web browser to access the website.

## Loading existing data

To load existing data from data.xml, execute the code below:

```
py manage.py loaddata data.xml
```
