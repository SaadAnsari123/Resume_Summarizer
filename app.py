from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Resume Summarizer & Job Finder</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
            }
            .container {
                max-width: 600px;
                width: 90%;
                padding: 20px;
                border-radius: 10px;
                background: rgba(255, 255, 255, 0.2);
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
                backdrop-filter: blur(10px);
            }
            input, button {
                margin: 10px 0;
                padding: 10px;
                width: 100%;
                border: none;
                border-radius: 5px;
            }
            input {
                background: white;
                color: black;
            }
            button {
                background: #ff7eb3;
                color: white;
                cursor: pointer;
                transition: 0.3s;
            }
            button:hover {
                background: #ff5277;
            }
            h2, h3 {
                text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Resume Summarizer & Job Finder</h2>
            <input type="file" id="resumeUpload" accept=".pdf,.txt">
            <button onclick="uploadResume()">Upload & Analyze</button>
            <h3>Summary</h3>
            <p id="summary">Your resume summary will appear here...</p>
            <h3>Job Recommendations</h3>
            <ul id="jobList"></ul>
        </div>
        <script>
            function uploadResume() {
                alert("This is a frontend-only page. Backend integration required for processing.");
            }
        </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
