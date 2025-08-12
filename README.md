# AWS Bedrock Knowledge Base Chatbot

A simple Streamlit chatbot that demonstrates AWS Bedrock Knowledge Base capabilities with two modes:
- **Retrieve**: Get relevant documents from your knowledge base
- **Retrieve & Generate**: Get AI-generated answers based on your knowledge base

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure AWS Credentials
Set up your AWS credentials using one of these methods:
- AWS CLI: `aws configure`
- Environment variables: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`
- IAM roles (if running on EC2)

### 3. Set Environment Variables
```bash
export KNOWLEDGE_BASE_ID="your-knowledge-base-id"
export MODEL_ARN="arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0"
```

Or create a `.env` file:
```
KNOWLEDGE_BASE_ID=your-knowledge-base-id
MODEL_ARN=arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0
```

### 4. Run the Application
```bash
streamlit run app.py
```

## Usage

1. Open your browser to the Streamlit URL (usually `http://localhost:8501`)
2. Choose your mode in the sidebar:
   - **Retrieve**: Shows source documents from your knowledge base
   - **Retrieve & Generate**: Provides AI-generated answers with citations
3. Enter your question and click Submit

## Requirements

- Python 3.8+
- AWS account with Bedrock access
- Configured Knowledge Base in AWS Bedrock
- Appropriate IAM permissions for Bedrock operations

## File Structure

```
├── app.py              # Main Streamlit application
├── knowledge_base.py   # AWS Bedrock client wrapper
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Demo Features

- Clean, intuitive interface suitable for non-technical users
- Error handling with user-friendly messages
- Expandable result sections for better readability
- Built-in instructions panel
- Minimal configuration required# knowledge-base-bedrock
# knowledge-base-bedrock
# knowledge-base-bedrock
