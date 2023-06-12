# PandasAI_Streamlit_Project

## Introduction

Welcome to the Excel file Analyser powered by OpenAI-PandasAI and Streamlit! This application allows users to upload CSV/Excel files and input custom prompts to analyse the data. Leveraging the capabilities of OpenAI's natural language processing, the application can return text or generate plots based on the user's prompt. Whether you're dealing with sales data, survey responses, or any table data, this app provides a seamless and interactive way to gain insights.

## Features

- **CSV File Upload**: Easily upload your CSV file with a simple drag-and-drop interface.
- **Custom Prompts**: Enter custom prompts to ask specific questions about the data or request general analysis.
- **Powered by OpenAI**: Utilises OpenAI's Large Language Model - PandasAI
- **Intuitive Visualization**: Get data insights visually with auto-generated plots.
- **Easy Interaction**: User-friendly interface built with Streamlit.

## Getting Started

### Prerequisites

- Python 3.9
- Streamlit
- OpenAI Python library

### Installation

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/csv-analyser-with-openai.git
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Create a .env file and replace with your OpenAI API key:

    ```
    OPENAI_API_KEY=your_api_key_here
    ```
    

### Running the App

1. After setting up, you can run the Streamlit app by executing the following command:

    ```shell
    streamlit run app.py
    ```

## How to Use

1. **Upload CSV File**: Use the file uploader to upload your CSV file.

2. **Input Prompt**: In the text input box, type your custom prompt to analyse the data (e.g., "What is the average sales revenue in Q1 2023?").

