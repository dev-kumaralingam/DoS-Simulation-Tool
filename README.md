# DoS Simulation Tool

This project is a simple web application designed to simulate high network traffic by sending a large number of HTTP requests to a target website. It allows you to test the performance, load balancing, and request-handling capacity of your own web applications in a controlled and legal environment.

# ⚠️ Disclaimer:

This tool should only be used for educational purposes and performance testing on websites that you own or have explicit permission to test. Unauthorized use of this tool against any third-party websites or services is illegal and may lead to serious legal consequences.

# Features

User-friendly web interface to input the target website and number of requests.
Sends multiple concurrent HTTP requests using multithreading.
Tracks the total requests sent, successful requests, and failed requests.
Real-time statistics to monitor the performance of your target system.

# Project Structure

DoS-Simulation-Tool/
│
├── app.py             # Flask backend to handle the requests and statistics.
├── static/
│   └── styles.css     # CSS styling for the web UI.
├── templates/
│   └── index.html     # Frontend HTML page for user interaction.
└── requirements.txt   # Python dependencies required to run the app.
└── README.md          # This file.

# Installation
Follow these steps to install and run the application:

    1.Clone the Repository:

        git clone https://github.com/dev-kumaralingam/DoS-Simulation-Tool.git
        cd DoS-Simulation-Tool

    2.Create a Virtual Environment (Optional but Recommended):

        python -m venv venv
        source venv/bin/activate    # On macOS/Linux
        venv\Scripts\activate       # On Windows

    3.Install the Dependencies:

        pip install -r requirements.txt

    4.Run the Application:

        python app.py

    5.Access the Web Interface: Open your browser and visit:

        http://127.0.0.1:5000/

# Usage

1.Enter the target URL in the input field (must be your own test site or a site you have permission to test).
2.Specify the number of requests to send (e.g., 1000 requests).
3.Click the "Start Attack" button to initiate the load simulation.
4.Monitor the progress and check statistics by visiting the /stats endpoint:
http://127.0.0.1:5000/stats

# Example Output from /stats Endpoint

{
    "total_sent": 980,
    "total_failed": 20,
    "start_time": 1697812801.678,
    "end_time": 1697812812.123
}

# Customization

1.Modify the CSS styles in static/styles.css to adjust the look and feel of the UI.
2.You can tweak the request-handling logic in app.py to adjust timeouts, retry mechanisms, or error handling.
3.For larger-scale tests, you can deploy this application on a cloud platform like AWS or DigitalOcean.

# Best Practices

1.Use a private testing environment: Perform all tests on your own servers or services to avoid unintended damage.
2.Limit request numbers: Avoid overwhelming your network infrastructure with excessive requests.
3.Monitor performance: Use additional monitoring tools to evaluate system resource consumption (CPU, memory, etc.) during the simulation.

# Known Issues

1.Timeouts: If too many requests are sent at once, some requests might time out.
2.Network Limits: Your system’s or network's bandwidth may restrict the number of requests you can send.

# Contributing

Feel free to fork this repository, submit pull requests, or suggest features by creating issues. Please ensure your contributions align with the legal and ethical use of this tool.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Disclaimer

This tool is intended solely for educational purposes and controlled load testing. Use it responsibly and legally. The developer assumes no liability for any misuse of the tool. Ensure you have permission to test any site or service you target.

# Contact

For questions or issues, feel free to contact the developer:
📧 kumaralingam2384@gmail.com  







