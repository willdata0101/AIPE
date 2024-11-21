# Historical Archive Assistant Chatbot

This repository contains the Python code for a chatbot designed to assist users in navigating historical archives. The chatbot leverages natural language processing (NLP) techniques to provide meaningful insights and answers to user queries about historical data.

## Features
- **Question Answering**: Responds to user queries about historical topics.
- **Search Functionality**: Provides a search mechanism for specific historical archives.
- **Customizable Knowledge Base**: Easily extendable to include additional historical data sources.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- A working knowledge of virtual environments (recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/historical-archive-assistant.git
   cd historical-archive-assistant

2. Create and activate a virtual environment:
   ```python3 -m venv venv
   source venv/bin/activate   # For Linux/MacOS
   venv\Scripts\activate      # For Windows```

3. Install the dependencies:
   ```pip install -r requirements.txt```

### Usage
1. Run the chatbot application:
   ```streamlit run MHAA.py```
2. Ask the assistant any question about your historical documents!

### File Structure
historical-archive-assistant/
```
├── MHAA.py          # Main entry point for the chatbot
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and submit a pull request.

## Acknowledgements
- Thanks to Shikhar Kwatra, Armando Díaz, and ELVTR for a tremendous amount of help in developing this project.
- Amazon Sagemaker for code development
- Amazon Bedrock for LLMs/Foundation Models
- Anthropic for the use of their Claude Sonnet 3.5 model.
