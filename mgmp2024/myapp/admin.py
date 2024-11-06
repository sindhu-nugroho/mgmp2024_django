from django.contrib import admin
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from .models import StudentRecord

class StudentRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'position')

    def export_to_pdf(self, request, queryset):
        # Set up the HTTP response to create a downloadable PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="student_records.pdf"'

        # Create the PDF object, using A4 size
        p = canvas.Canvas(response, pagesize=A4)
        width, height = A4
        y = height - 50  # Initial Y position on the PDF

        # Loop through selected records and add details to the PDF
        for student in queryset:
            # Write text fields
            p.drawString(30, y, f"Name: {student.name}")
            p.drawString(30, y - 20, f"School: {student.school}")
            p.drawString(30, y - 40, f"Position: {student.position}")
            p.drawString(30, y - 60, f"Description: {student.description}")

            # If the student has an image, add it to the PDF
            if student.image:
                image_path = student.image.path
                try:
                    img = ImageReader(image_path)
                    p.drawImage(img, 400, y - 50, width=100, height=100)
                except Exception as e:
                    print(f"Error loading image: {e}")

            y -= 150  # Move down the page for the next record

            # If we run out of space on the page, add a new page
            if y < 100:
                p.showPage()
                y = height - 50  # Reset Y position for the new page

        # Finalize and save the PDF
        p.showPage()
        p.save()
        return response

    # Register the custom action in the admin
    export_to_pdf.short_description = "Export Selected to PDF"
    actions = [export_to_pdf]

admin.site.register(StudentRecord, StudentRecordAdmin)
