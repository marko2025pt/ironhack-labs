# Lab 2 - Titanic Data Analysis

## Overview
This folder contains my Lab 2 work for Ironhack, focused on analyzing the Titanic dataset. The project includes data cleaning, feature engineering, exploratory analysis, and exporting enriched data to JSON.

## Folder Structure
- **.vscode/**: VS Code workspace settings.
- **data/**: Contains raw and processed data files:
  - `titanic.csv`: Original Titanic dataset.
  - `titanic_data.json`: Exported JSON file with all passengers and summary statistics.
- **Lab_Summary.txt**: Text summary of the lab and key observations.
- **Log_Outputs.txt**: Output logs from code execution.
- **titanic_analysis.ipynb**: Jupyter Notebook with full analysis, feature engineering, visualization, and JSON export.

## Features Engineered
- **FamilySize**: Total number of family members aboard.
- **IsAlone**: Indicates if the passenger traveled alone.
- **AgeGroup**: Categorized passenger ages (Child, Young Adult, Adult, Senior).
- **HasCabin**: Whether the passenger had a cabin assigned.
- **FarePerPerson**: Fare divided by family size to estimate cost per individual.
- **Title**: Extracted from passenger names.

## Key Functionality
- Data cleaning including handling missing values (e.g., filling missing ages with the mean).
- Feature engineering for better survival pattern analysis.
- Encapsulation using Python **classes**:
  - `Passenger`: Represents a passenger and all related attributes.
  - `TitanicDataset`: Manages the dataset, computes statistics, and exports JSON.
- Comprehensive summary statistics including:
  - Total survivors and non-survivors.
  - Average age, fare, and fare per person.
  - Survival breakdown by sex and age group.

## Usage
Open `titanic_analysis.ipynb` to explore the full analysis, modify features, or run additional statistics. The JSON export can be reused in other scripts or projects.

## Author
Marco Martins
