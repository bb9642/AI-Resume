import json

def parse_resume(resume_text):
    sections = resume_text.split("\n\n")
    resume_json = {}
    
    for section in sections:
        lines = section.split("\n")
        header = lines[0].strip(":")
        content = lines[1:]
        
        if header == "Contact Information":
            contact_info = {}
            for line in content:
                key, value = line.split(": ")
                contact_info[key] = value
            resume_json[header] = contact_info
        
        elif header in ["Summary", "Skills", "Certifications"]:
            resume_json[header] = content[0] if header == "Summary" else content
        
        else:
            items = []
            for i in range(0, len(content), 4):
                item = {}
                for line in content[i:i+4]:
                    key, value = line.split(": ", 1)
                    item[key] = value
                items.append(item)
            resume_json[header] = items
    
    return json.dumps(resume_json, indent=2)

# Example usage
resume_text = """Contact Information:
Name: Bhuvan Beera
Phone: 7788005517
Email: bb9642@srmist.edu.in.com
LinkedIn: https://www.linkedin.com/in/bhuvan-beera-80a989251/

Summary:
 A entustiactic software engineer with a passion for developing innovative programs...


Education:
Institution: SRM University
Degree: Bachelor of Science
Field of Study: Computer Science
Graduation Year: 2025

Skills:
Python
Linux
SQL
CLoud
Security

Certifications:
Certified Ethical Hacker

Projects:
Title: AI Chatbot
Description: Developed a chatbot using natural language processing...
Technologies: Python, TensorFlow
"""

parsed_resume = parse_resume(resume_text)
print(parsed_resume)
