"""
Prompt templates for Groq Final Drafting.
"""

REPORT_DRAFT_PROMPT = """
You are an expert product analyst. I am providing you with a structured "Weekly Pulse Report" containing raw themes, quotes, and actionable steps extracted from user reviews.

Your task is to transform this structured data into a detailed, comprehensive, and professional report suitable for a Google Doc.

Here is the structured JSON report:
{report_json}

Requirements:
1. Tone: Professional and analytical.
2. Length: Write a comprehensive report (approx. 500-800 words).
3. Structure: 
   - An "Executive Summary" section.
   - A detailed breakdown of each theme, thoroughly integrating the quotes as evidence.
   - A comprehensive "Strategic Recommendations & Next Steps" section expanding on the actions.
4. Formatting: Use Markdown (headings, bullet points, bold text).

Output ONLY the final markdown text.
"""

EMAIL_DRAFT_PROMPT = """
You are an expert product communicator. I am providing you with a structured "Weekly Pulse Report" containing raw themes, quotes, and actionable steps extracted from user reviews.

Your task is to draft a concise, highly readable email summary for stakeholders.

Here is the structured JSON report:
{report_json}

Requirements:
1. Tone: Professional, concise, and scannable.
2. Length: Under 200 words total.
3. Structure: 
   - A brief introductory sentence.
   - 3-4 bullet points highlighting the most critical themes (do not include full quotes).
   - A concluding sentence noting that the full report is linked below.
4. EXACT MARKER REQUIRED: You MUST include the exact text `{{doc_url}}` at the very end of the email (e.g. "Full detailed report: {{doc_url}}"). Do not format it as a markdown link, just output the raw {{doc_url}} placeholder.

Output ONLY the final email body text.
"""

