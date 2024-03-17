# DETECT PERSON

The **DETECT PERSON** project utilizes facial recognition to identify individuals based on the details uploaded to the MySQL database. Users can upload person details via the designated webpage, and the system will recognize them when they appear in front of the camera. Visit the "Detect Person" webpage to experience this feature. To operate the camera, click the "Start/Stop" button. To halt the camera, click the same button.

## Features

- **Person Detection**: Utilizes face recognition Python library to detect persons based on uploaded details.
- **Web Interface**: Users can upload person details through a dedicated webpage.
- **Live Detection**: Real-time identification of individuals captured by the camera.
- **Customization**: The project offers flexibility with the option to use either the Face Recognition library or the Deep Face library.
- **MySQL Database**: Requires MySQL and the creation of a database with a table named "persons". Ensure to update the MySQL username and password in the `utils.py` file.

## Getting Started

1. **Setup MySQL Database**:
   - Install MySQL and create a database.
   - Within the database, create a table named "persons" to store person details.

2. **Configuration**:
   - Update the MySQL host,username,password,database in the `utils.py` file to match your database credentials.

3. **Installation**:
   - Download the required dependencies listed in `requirements.txt` by running `pip install -r requirements.txt`.

4. **Running the Project**:
   - Execute `app.py` using Python (`python app.py`) to start the application.

## Project Structure

- **src/static**: Stores static images.
- **src/templates**: Stores HTML templates.
- **src/app.py**: Contains Flask code, including index, upload details to the database, face detection, and admin functionalities.
- **utils/utils.py**: Includes code for frame detection, database connection, and loading images from the database.

## Future Developments

The **DETECT PERSON** project can be further enhanced with the following features:

- **Display Detected Person's Details**: Display detected person's details on the webpage for reference.
- **Unknown Person Identification**: Prompt users to upload details if an unknown person is detected.

## Contributions

Contributions to this project are welcome. Feel free to suggest improvements or submit pull requests to enhance its functionality.

## Disclaimer

This project is intended for educational purposes and should not be used for any illegal activities. Respect privacy and use the technology responsibly.

Enjoy detecting persons with **DETECT PERSON**! 📷👤