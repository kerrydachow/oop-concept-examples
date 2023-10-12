"""
Single Responsibility Principle
-------------------------------

-   This is an example of code that violates the Single
    Responsibility Principle.
-   Invoice has too many roles, once other modules depend
    on this component, changing the class will create
    unintended side effects.
"""

class Invoice:
    """
    Invoice class handling invoices AND reports.
    """
    def add_invoice(self):
        pass


    def delete_invoice(self):
        pass


    def email_report(self):
        pass


    def generate_report(self):
        pass