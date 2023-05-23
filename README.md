# Real Estate App

This full-stack web application combines the power of React, Redux, and Django with the Django Rest Framework (DRF) to deliver a robust and scalable solution. With integrated Stripe payment integration, the application offers a secure and seamless payment experience for users.

The frontend of this  application utilizes React and Redux to provide a dynamic and interactive user interface. Redux manages the application state, ensuring efficient data handling and seamless integration with the backend.

On the backend, Django serves as the web framework, while DRF enables the creation of powerful and flexible APIs for seamless communication between the frontend and backend. This allows for efficient data retrieval, storage, and processing.

With Stripe payment integration, the application facilitates secure and reliable payment transactions, providing users with a smooth checkout process and peace of mind.

By leveraging the capabilities of React, Redux, Django, and DRF, this full-stack web application delivers a seamless user experience, robust backend functionality, and secure payment processing, making it an ideal choice for businesses looking to build a feature-rich and reliable web application.

## Setup

- clone the repository.
- run: `npm install`, this will install the required frontend packages
- run: `npm run build`, this will make the production react build folder
- run: `python3 -m venv venv`
- then activate the virtual environment
- run: `pip install -r requirements.txt`
- in `realest_estate/settings.py`, under `DATABASES`, set the `PASSWORD` field to your database password
- in `realest_estate/settings.py`, under `EMAIL_HOST_USER`, set your `email` that you are using
- in `realest_estate/settings.py`, under `EMAIL_HOST_PASSWORD`, set your app `password` you are using
- in `contacts/views.py`, under the `send_mail` function, input the `email` you are using
