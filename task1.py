
class ReportGenerator:
    def generate_report(self):
        return "This is the report content."


class FileManager:
    def save_to_file(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Report saved to {filename}")



class EmailSender:
    def send_email(self, email, content):
        print(f"Sending report to {email}")
        print(f"Email sent to {email} with content: {content}")


if __name__ == "__main__":
    report_generator = ReportGenerator()
    report_content = report_generator.generate_report()

    file_manager = FileManager()
    file_manager.save_to_file("report.txt", report_content)

    email_sender = EmailSender()
    email_sender.send_email("example@example.com", report_content)
