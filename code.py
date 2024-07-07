import re
import json

def parse_resume(resume_text):
    # Initialize an empty dictionary to store parsed data
    parsed_resume = {}

    # Extract name (assuming it's the first line of the resume)
    lines = resume_text.splitlines()
    parsed_resume["name"] = lines[0].strip()

    # Extract contact information using regular expressions
    contact_info_pattern = r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})|(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})'
    contact_info_matches = re.findall(contact_info_pattern, resume_text)
    email = ""
    phone = ""
    for match in contact_info_matches:
        if match[0]:
            email = match[0]
        if match[1]:
            phone = match[1]
    parsed_resume["contact_information"] = {
        "email": email,
        "phone": phone
    }

    # Extract education information (assuming it's structured similarly)
    education_pattern = r'Education: ([^\n\r]*)'
    education_match = re.search(education_pattern, resume_text, re.IGNORECASE)
    if education_match:
        parsed_resume["education"] = education_match.group(1).strip()

    # Extract skills (assuming it's a comma-separated list)
    skills_pattern = r'Skills: ([^\n\r]*)'
    skills_match = re.search(skills_pattern, resume_text, re.IGNORECASE)
    if skills_match:
        parsed_resume["skills"] = [skill.strip() for skill in skills_match.group(1).split(',')]

    # Extract experience (assuming it's structured similarly)
    experience_pattern = r'Experience: ([^\n\r]*)'
    experience_match = re.search(experience_pattern, resume_text, re.IGNORECASE)
    if experience_match:
        parsed_resume["experience"] = experience_match.group(1).strip()

    return parsed_resume

# Example usage
resume_text = """
John Doe
Email: john.doe@example.com
Phone: +1234567890

Education: Bachelor of Technology in Computer Science, SRM University

Skills: Python, SQL, Machine Learning

Experience: Data Analyst Intern at ABC Corp, Summer 2023
"""

parsed_data = parse_resume(resume_text)
print(json.dumps(parsed_data, indent=4))
