# Email Extractor Automation
import re

text = """Hello, please contact us at support@codealpha.com or sales@alpha.org.
Alternatively, reach out to hello.world@company.co.in for international queries."""

emails = re.findall(r"[\w\.-]+@[\w\.-]+", text)
print("Extracted Emails:")
for email in emails:
    print(email)
