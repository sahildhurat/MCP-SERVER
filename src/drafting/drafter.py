import json
from dataclasses import dataclass, asdict
from src.processing.pulse_generator import PulseReport
from .groq_client import GroqClient
from .prompts import REPORT_DRAFT_PROMPT, EMAIL_DRAFT_PROMPT

@dataclass
class FinalDrafts:
    doc_content: str
    email_body: str

class ReportDrafter:
    """Orchestrates Groq to convert a structured PulseReport into polished prose."""
    
    def __init__(self, groq_client: GroqClient):
        self.client = groq_client
        
    def draft_report(self, report: PulseReport) -> FinalDrafts:
        """
        Takes a PulseReport DataClass, serializes it to JSON, 
        and uses Groq to generate a detailed report and a short email draft.
        """
        report_dict = asdict(report)
        report_json = json.dumps(report_dict, indent=2)
        
        # 1. Draft detailed Google Doc report
        doc_prompt = REPORT_DRAFT_PROMPT.format(report_json=report_json)
        doc_content = self.client.generate_draft(doc_prompt)
        
        # 2. Draft short email summary
        email_prompt = EMAIL_DRAFT_PROMPT.format(report_json=report_json)
        email_body = self.client.generate_draft(email_prompt)
        
        # Enforce presence of {doc_url} placeholder in email (Edge Case handling)
        if "{doc_url}" not in email_body:
            email_body += "\n\nFull detailed report: {doc_url}"
            
        return FinalDrafts(doc_content=doc_content, email_body=email_body)

