# PDF-Based Query Answering System

This project is a Django-based application that allows users to upload PDF documents, ask questions about the content of these PDFs, and receive answers generated using OpenAI's GPT-3.5 model. The system uses LangChain for text processing and FAISS for vector storage, enabling efficient and accurate responses.

## Features

- **PDF Upload:** Upload PDF files to the system for processing.
- **Query Answering:** Ask questions related to the uploaded PDF content and get detailed responses generated using OpenAI's language model.
- **API Key Validation:** Ensure that the provided OpenAI API key is valid before processing any queries.
- **Custom CORS Middleware:** Allows cross-origin requests to interact with the API.

## Technologies Used

- **Django:** A high-level Python web framework for rapid development and clean, pragmatic design.
- **Django REST Framework:** A powerful toolkit for building Web APIs.
- **OpenAI API:** Utilized for generating responses to queries based on PDF content.
- **LangChain:** Used for text splitting and processing.
- **FAISS:** A library for efficient similarity search and clustering of dense vectors.
- **HTML & CSS:** Frontend technologies used to create the user interface for file uploads and querying.
- **Python-dotenv:** A Python library for managing environment variables.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/pdf-query-system.git
    cd pdf-query-system
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - Create a `.env` file in the root directory.
    - Add your OpenAI API key:
      ```plaintext
      OPENAI_API_KEY=your-openai-api-key
      ```

5. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

1. **Frontend Interface:**
   - The frontend is built using HTML and CSS.
   - Navigate to `/upload` to upload a PDF file. 
   - After uploading, go to `/ask-query` to submit your questions related to the PDF content.

2. **API Endpoints:**
   - **Upload a PDF File:**
     - Endpoint: `/api/upload/`
     - Method: `POST`
     - Description: Upload a PDF file for processing.
   - **Ask a Query:**
     - Endpoint: `/api/ask-query/`
     - Method: `POST`
     - Description: Submit a query related to the uploaded PDF content.
   - **Validate OpenAI API Key:**
     - Endpoint: `/api/validate-key/`
     - Method: `POST`
     - Description: Validate the provided OpenAI API key.

## Project Structure

- **views.py:** Contains the API views for handling PDF uploads, querying, and API key validation.
- **utils.py:** Utility functions for validating API keys, generating vector stores from PDFs, and processing queries.
- **templates:** Contains the HTML files for the frontend interface.
- **static:** Includes the CSS files for styling the frontend.
- **serializers.py:** Defines the serializers for handling file uploads and queries.

## Future Enhancements

- Implement user authentication to save and manage uploaded PDFs and query history.
- Add support for other document formats like Word or Excel.
- Enhance the UI/UX for a more user-friendly experience.


![image](https://github.com/user-attachments/assets/81435775-86ed-406c-9f3e-82ec92780096)

