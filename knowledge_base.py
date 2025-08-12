import boto3
import os

class KnowledgeBaseClient:
    def __init__(self):
        # Initialize boto3 client
        self.client = boto3.client('bedrock-agent-runtime')
        
        # Configuration - replace with your actual values
        self.knowledge_base_id = os.getenv('KNOWLEDGE_BASE_ID')
        self.model_arn = os.getenv('MODEL_ARN')
    
    def retrieve(self, query):
        """Retrieve documents from knowledge base"""
        try:
            response = self.client.retrieve(
                knowledgeBaseId=self.knowledge_base_id,
                retrievalQuery={'text': query},
                retrievalConfiguration={
                    'vectorSearchConfiguration': {
                        'numberOfResults': 5
                    }
                }
            )
            return response
        except Exception as e:
            raise Exception(f"Retrieve failed: {str(e)}")
    
    def retrieve_and_generate(self, query):
        """Retrieve and generate response from knowledge base"""
        try:
            response = self.client.retrieve_and_generate(
                input={'text': query},
                retrieveAndGenerateConfiguration={
                    'type': 'KNOWLEDGE_BASE',
                    'knowledgeBaseConfiguration': {
                        'knowledgeBaseId': self.knowledge_base_id,
                        'modelArn': self.model_arn,
                        'retrievalConfiguration': {
                            'vectorSearchConfiguration': {
                                'numberOfResults': 5
                            }
                        }
                    }
                }
            )
            return response
        except Exception as e:
            raise Exception(f"Retrieve and generate failed: {str(e)}")