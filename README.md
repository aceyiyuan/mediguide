# Mediguide
Empowering Efficient Medication Distribution, Administration and Information Access

Mediguide is an innovative application designed to address the challenges faced by nurses during the medication distribution and administration process. It aims to empower nurses with efficient medication management and comprehensive information access. Here's an overview of Mediguide's key features, benefits, and future expansion plans:


![Tarjotin Image](https://github.com/aceyiyuan/mediguide/blob/main/tarjotin.png?raw=true)
|:--:| 
| *Given the multitude of medication cups occupying the medication tray, each housing various tablets, is it practical to rely solely on memory to accurately identify and differentiate the specific medication associated with each tablet?* |

Problem:
In healthcare settings, many nurses face significant challenges during the medication distribution and administration process. To ensure accuracy and patient safety, a double confirmation system is implemented. However, within the existing workflow, nurses often struggle to locate specific medication packages, especially when uncertain about specific medications. They frequently need to find the medication and open its packaging to confirm its accuracy. This approach is time-consuming and inefficient, particularly for new nurses or temporary agency nurses who may have difficulty locating medication storage areas. Factors such as time constraints, nursing shortages, and poorly designed electronic health systems further exacerbate the problem. As a result, the double confirmation process becomes superficial, significantly increasing the risk of medication errors, compromising patient safety, and leading to overall inefficiencies in healthcare workflows.

Solution:
To address these challenges and optimize medication administration, we present Mediguide, an innovative application designed to empower nurses with efficient medication management and comprehensive information access. The app aims to streamline the medication distribution and administration process, mitigate the impact of nursing shortages, and overcome the limitations of existing electronic health systems.

Key Features:

Visual Medication Reference: Mediguide includes an extensive database of medications, complete with visual representations of tablets, capsules, and packages. Nurses can quickly identify medications through visual cues, reducing the risk of errors and minimizing the need for extensive confirmation procedures.

Comprehensive Medication Information: Beyond visuals, the app provides detailed information about each medication, including its purpose, recommended dosage, potential side effects, and contraindications. This empowers nurses to have a deeper understanding of the medications they administer, enhancing safety and patient care.

Alternative Medication Suggestions: Mediguide offers alternative medication suggestions in situations where a specific medication is unavailable or contraindicated. These suggestions are provided based on the Anatomical Therapeutic Chemical (ATC) classification system, offering nurses efficient exploration of viable options.

User-Friendly Interface and Quick Navigation: The app features a user-friendly interface that enables nurses to access medication information with ease. Quick search functionality, intuitive navigation, and well-organized medication profiles facilitate swift and convenient access to the desired information, even in time-sensitive scenarios.

Benefits:

Efficient Medication Administration: Mediguide optimizes the medication administration process, reducing errors and streamlining workflows. The visual reference, comprehensive information, and alternative suggestions contribute to safer and more accurate medication administration.

Improved Decision-Making: Nurses can make informed decisions based on detailed medication information, including purpose, dosage, and potential side effects. This enhances their ability to deliver personalized patient care and prioritize patient safety.

Time Optimization: By providing a centralized and easily accessible medication database, Mediguide minimizes the time and effort required for information retrieval. Nurses can swiftly access essential medication details, even in time-constrained situations, improving overall efficiency.

Mitigating Nursing Shortages: Mediguide helps mitigate the impact of nursing shortages by optimizing workflows and reducing the burden on nursing staff. It enables nurses to perform medication-related tasks more efficiently, freeing up time for other critical patient care responsibilities.

Future Expansion:
As Mediguide continues to evolve, we plan to integrate artificial intelligence capabilities into the application to provide personalized medication recommendations. For example, nurses will be able to retrieve images of the medications they are looking up through voice prompts. The app aims to continuously improve and support nurses in making informed decisions, further enhancing patient care outcomes.


# Database Design

This repository contains the database design for our medication information system. The database is designed to support multiple languages for accommodating international users. 

## Tables

### MedicationInfo

| Column Name      | Data Type   | Description                                                  |
| ---------------- | ----------- | ------------------------------------------------------------ |
| ID               | INT         | Primary key                                                  |
| Name             | VARCHAR     | Medication name                                              |
| ActiveIngredient | VARCHAR     | Active ingredient of the medication                          |
| Purpose          | TEXT        | Purpose of the medication                                    |
| CNS_medication   | BOOLEAN     | Indicates if it has primarily central nervous system effects |
| MoreDetails      | TEXT        | Link or additional details about the medication              |

### MedicationStrength

| Column Name   | Data Type   | Description                                  |
| ------------- | ----------- | -------------------------------------------- |
| ID            | INT         | Primary key                          |
| MedicationID  | INT         | Foreign key referencing MedicationInfo.ID    |
| Strength      | VARCHAR20   | Strength of the medication (e.g., 5mg, 10mg) |


### MedicationImages

| Column Name           | Data Type   | Description                                                               |
| --------------------- | ----------- | ------------------------------------------------------------------------- |
| ID                    | INT         | Primary key                                                               |
| MedicationStrengthID  | INT         | Foreign key referencing MedicationStrength.ID                             |
| FrontImage            | ImageField  | Field for storing the front image of the medication                       |
| BackImage             | ImageField  | Field for storing the back image of the medication (optional)             |
| package_image         | ImageField  | Field for storing the package image of the medication (file upload field) |


### AlternativeMedications

| Column Name    | Data Type   | Description                                                |
| -------------- | ----------- | ---------------------------------------------------------- |
| ID             | INT         | Primary key                                                |
| MedicationID   | INT         | Foreign key referencing MedicationInfo.ID                  |
| MedicationName | VARCHAR     | Name of the alternative medication                         |
| MedicationLink | VARCHAR     | Link to more information about the alternative medication  |


## Language Support

This database design includes language support to accommodate multilingual data. The fields such as medication name, active ingredient, purpose, and alternative medication names can be stored in multiple languages using appropriate localization techniques. The database design allows for seamless retrieval and storage of data in different languages.

By implementing language support in a single database, we can manage and query data efficiently without the need for separate databases for each language. This approach provides convenience, scalability, and flexibility in handling multilingual data.

For more details on how to implement language support in the application, please refer to the corresponding code documentation.


## Installation


cd desktop
django-admin startproject mediguide
cd mediguide
python3 -m venv myvenv 
source myvenv/bin/activate
pip install django
pip install --upgrade pip
* django-admin version optional
python manage.py runserver
python manage.py migrate
deactivate (when stop)
python manage.py startapp core

python manage.py createsuperuser




# mediguide
