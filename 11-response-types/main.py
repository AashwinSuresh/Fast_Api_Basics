from pathlib import Path

from fastapi import FastAPI, Response
from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse

app = FastAPI(title="FastAPI Basics - Lesson 11: Response Types")

# 1. Plain Text — text/plain
@app.get("/text", response_class=PlainTextResponse)
def get_text():
    return "Hello! This is raw, unformatted text."

# 2. HTML — text/html
@app.get("/page", response_class=HTMLResponse)
def get_html():
    return """
    <html>
        <body>
            <h1>Welcome to my website</h1>
            <p>Rendered directly by FastAPI.</p>
        </body>
    </html>
    """

# 3. Files — FileResponse
# Add a sample file at 11-response-types/files/report.pdf before testing this route.
@app.get("/download-report", response_class=FileResponse)
def get_report():
    report_path = Path(__file__).parent / "files" / "report.pdf"
    return FileResponse(report_path, filename="monthly_report.pdf")

# 4. Explicit media type without a dedicated response class
@app.get("/media-type-example")
def media_type_example():
    return Response(
        content="This response explicitly declares its media type.",
        media_type="text/plain",
    )

#EXAMPLES OF MEDIA TYPE WITHOUT A DEDICATED RESPONSE CLASS 

# 1. Generic Response — CSV
@app.get("/export-csv")
def export_csv():
    csv_data = "name,role\nAlice,Admin\nBob,User"
    return Response(content=csv_data, media_type="text/csv", headers={"Content-Disposition":"attachment; filename=data.csv"}) #another content-disposition type : inline

# 2. Generic Response — XML
@app.get("/xml-data")
def export_xml():
    xml_data = "<user><name>Alice</name><role>Admin</role></user>"
    return Response(content=xml_data, media_type="application/xml", headers={"Content-Disposition":"attachment; filename=data.xml"})

