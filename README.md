# Flask REST API with OpenAI Integration

## Overview

This API allows users to send queries and receive responses generated by an OpenAI model. The API connects to a Supabase PostgreSQL database, processes user queries using LangChain, and handles rate limit errors gracefully.

## Features

- **Query Processing:** Accepts user queries and generates SQL queries based on the database schema.
- **Natural Language Response:** Returns a human-readable response based on the SQL query results.
- **Error Handling:** Graceful handling of rate limit errors from OpenAI, returning appropriate messages.

## Installation

### Prerequisites

- Python 3.8 or higher
- Virtual environment (optional but recommended)

### Setup

1. **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-directory>
    ```

2. **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Environment Variables:**
   Create a `.env` file in the root directory and add the following variables:
    ```bash
    OPENAI_API_KEY=your-openai-api-key
    SUPABASE=your-supabase-uri
    ```

## Usage

### Running the API

To start the Flask API, run:
```bash
flask run
```  

The API will be accessible at `http://127.0.0.1:5000/`.

### Endpoints

- **POST /query**
    - **Description:** Accepts a user query and returns a processed response.
    - **Request Body:** JSON with a `query` field.
    - **Response:** JSON with the processed response or an error message.

### Example Request

```bash
curl -X POST http://127.0.0.1:5000/query -H "Content-Type: application/json" -d '{"query": "how many renters are there in the database?"}'
```

### Example Response

```json
{
  "response": "There are X renters in the database."
}
```
