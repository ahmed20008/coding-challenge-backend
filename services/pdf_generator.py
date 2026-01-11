from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from services.github_service import get_github_profile_image
import os

def generate_pdf(application):
    """Generate PDF document for application"""
    os.makedirs("pdfs", exist_ok=True)
    
    filename = f"pdfs/application_{application.id}_{application.email.replace('@', '_at_')}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    
    elements = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2C3E50'),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#34495E'),
        spaceAfter=12,
        spaceBefore=12
    )
    
    elements.append(Paragraph("Job Application", title_style))
    elements.append(Spacer(1, 0.2*inch))
    
    try:
        image_path = get_github_profile_image(application.github_user)
        if image_path and os.path.exists(image_path):
            img = Image(image_path, width=2*inch, height=2*inch)
            img.hAlign = 'CENTER'
            elements.append(img)
            elements.append(Spacer(1, 0.3*inch))
    except Exception as e:
        print(f"Could not fetch GitHub image: {e}")
    
    elements.append(Paragraph("Applicant Information", heading_style))
    
    applicant_data = [
        ["Name:", application.name],
        ["Email:", application.email],
        ["GitHub:", application.github_user],
        ["Application Date:", application.created_at.strftime("%Y-%m-%d %H:%M")]
    ]
    
    applicant_table = Table(applicant_data, colWidths=[2*inch, 4*inch])
    applicant_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#ECF0F1')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2C3E50')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#BDC3C7'))
    ]))
    
    elements.append(applicant_table)
    elements.append(Spacer(1, 0.4*inch))
    
    elements.append(Paragraph("Past Projects", heading_style))
    elements.append(Spacer(1, 0.2*inch))
    
    for idx, project in enumerate(application.projects, 1):
        project_title = Paragraph(f"<b>Project {idx}: {project.name}</b>", styles['Heading3'])
        elements.append(project_title)
        elements.append(Spacer(1, 0.1*inch))
        
        project_data = [
            ["Role:", project.role],
            ["Employment:", project.employment_mode.value],
            ["Capacity:", project.capacity.value],
            ["Duration:", f"{project.duration_months} months"],
            ["Start Year:", str(project.start_year)],
            ["Team Size:", str(project.team_size)],
        ]
        
        if project.repository_link:
            project_data.append(["Repository:", project.repository_link])
        if project.live_url:
            project_data.append(["Live URL:", project.live_url])
        
        project_table = Table(project_data, colWidths=[2*inch, 4*inch])
        project_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#E8F6F3')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2C3E50')),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#BDC3C7'))
        ]))
        
        elements.append(project_table)
        elements.append(Spacer(1, 0.3*inch))
    
    doc.build(elements)
    return filename
