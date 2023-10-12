"""
Single Responsibility Principle
-------------------------------

-   Your class should only have 1 reason to change
-   Your class should only have 1 responsibility
-   Reduces side effects upon change, increases cohesion,
    reduces coupling, and decreases code complexity.
"""

class Invoice:
    """
    Invoice class handling invoice stuff.
    """
    def add_invoice(self):
        pass


    def delete_invoice(self):
        pass



class Report:
    """
    Report class handling report stuff.
    """
    def generate_report(self):
        pass


class Email:
    """
    Email class handling emails.
    """
    def email_report(self, report: Report):
        pass