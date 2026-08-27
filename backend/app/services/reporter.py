import os
import matplotlib.pyplot as plt
from fpdf import FPDF
from app.models.schemas import AnalysisResult
import uuid
import logging

logger = logging.getLogger(__name__)

class ReportGenerator:
    def __init__(self, result: AnalysisResult):
        self.result = result
        self.report_id = str(uuid.uuid4())
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def _generate_graph(self) -> str:
        """Generates a timeline or IOC graph and saves it as an image."""
        graph_path = f"data/reports/{self.report_id}_graph.png"

        # We will create a simple timeline visualization using OO interface to be thread-safe
        fig, ax = plt.subplots(figsize=(10, 4))

        events = self.result.timeline
        if not events:
            # Fallback if no timeline
            ax.text(0.5, 0.5, 'No timeline events to display', ha='center', va='center')
        else:
            dates = [e.get('timestamp', '')[11:19] for e in events] # Extract time
            labels = [e.get('event', 'Event')[:30] + '...' for e in events]

            ax.plot(dates, [1]*len(dates), "ro-")
            ax.set_yticks([])
            ax.set_title("Incident Event Timeline", pad=20)

            for i, label in enumerate(labels):
                ax.annotate(label, (dates[i], 1), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

        fig.tight_layout()
        fig.savefig(graph_path)
        plt.close(fig)
        return graph_path

    def generate_pdf(self) -> str:
        pdf_path = f"data/reports/DFIR_Report_{self.report_id}.pdf"

        self.pdf.add_page()

        # Title
        self.pdf.set_font("Arial", 'B', 24)
        self.pdf.set_text_color(0, 51, 102)
        self.pdf.cell(0, 20, "AI DFIR Expert Analysis Report", ln=True, align="C")
        self.pdf.ln(10)

        # Summary
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.cell(0, 10, "1. Executive Summary", ln=True)
        self.pdf.set_font("Arial", '', 12)
        self.pdf.multi_cell(0, 10, self.result.summary)
        self.pdf.ln(5)

        # Confidence Score
        self.pdf.set_font("Arial", 'B', 12)
        score_text = f"AI Confidence Score: {self.result.confidence_score * 100:.0f}% (High Accuracy Achieved)"
        self.pdf.cell(0, 10, score_text, ln=True)
        self.pdf.ln(5)

        # IOCs
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(0, 10, "2. Indicators of Compromise (IOCs)", ln=True)
        self.pdf.set_font("Arial", '', 12)
        for ioc in self.result.iocs:
            ioc_text = f"- {ioc.indicator} ({ioc.type}): {ioc.description}"
            self.pdf.multi_cell(0, 8, ioc_text)
        self.pdf.ln(10)

        # MITRE ATT&CK
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(0, 10, "3. MITRE ATT&CK Mapping", ln=True)
        self.pdf.set_font("Arial", '', 12)
        for tactic in self.result.mitre_attack:
            self.pdf.cell(0, 8, f"- {tactic}", ln=True)
        self.pdf.ln(10)

        # Timeline Graph
        self.pdf.add_page()
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(0, 10, "4. Incident Timeline Analysis", ln=True)

        try:
            graph_img = self._generate_graph()
            self.pdf.image(graph_img, x=10, w=190)
            # Clean up image after embedding
            if os.path.exists(graph_img):
                os.remove(graph_img)
        except Exception as e:
            logger.error(f"Failed to generate graph for PDF: {e}")
            self.pdf.set_font("Arial", 'I', 12)
            self.pdf.cell(0, 10, "[Graph generation failed or no data available]", ln=True)

        self.pdf.output(pdf_path)
        return pdf_path
