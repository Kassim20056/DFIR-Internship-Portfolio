import os
import json
import logging
from typing import Dict, Any, List
try:
    from evtx import PyEvtxParser
except ImportError:
    PyEvtxParser = None

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ForensicParser:
    def __init__(self, file_path: str, filename: str):
        self.file_path = file_path
        self.filename = filename
        self.ext = os.path.splitext(filename)[1].lower()

    def parse(self) -> str:
        """Parses the evidence file and returns a structured string/text representation for the AI to analyze."""
        try:
            if self.ext == '.json':
                return self._parse_json()
            elif self.ext == '.evtx':
                return self._parse_evtx()
            elif self.ext in ['.log', '.txt', '.csv']:
                return self._parse_text()
            elif self.ext == '.pcap':
                return self._parse_pcap()
            else:
                return self._parse_generic()
        except Exception as e:
            logger.error(f"Error parsing {self.filename}: {e}")
            return f"Error parsing {self.filename}: {str(e)}"

    def _parse_json(self) -> str:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return json.dumps(data, indent=2)[:10000] # Limit to 10k chars for simulated context

    def _parse_evtx(self) -> str:
        if not PyEvtxParser:
            return "EVTX parsing library not available."

        parsed_events = []
        try:
            parser = PyEvtxParser(self.file_path)
            for record in parser.records():
                # For brevity, extract only a few events in this simulation
                parsed_events.append(record['data'])
                if len(parsed_events) >= 50: # Limit to 50 events for context size
                    break
            return "\\n".join(parsed_events)
        except Exception as e:
            return f"EVTX parsing failed: {str(e)}"

    def _parse_text(self) -> str:
        with open(self.file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read(10000) # Read first 10k characters
            return content

    def _parse_pcap(self) -> str:
        # Placeholder for PCAP parsing (would typically use Scapy or invoke tshark)
        return f"[Simulated PCAP Parsing] Extracted network flows from {self.filename}:\\n- 192.168.1.5 -> 10.0.0.8:443 (TLS)\\n- 10.0.0.8 -> 192.168.1.5:443 (TLS)\\n- Potential Command & Control traffic detected on port 4444."

    def _parse_generic(self) -> str:
        return f"[Generic File Parsing] File {self.filename} received but specific parsing is not implemented yet. Assuming binary or unstructured data."
