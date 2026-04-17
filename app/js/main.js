document.addEventListener('DOMContentLoaded', function() {
    // Traffic Chart
    const trafficCtx = document.getElementById('trafficChart');
    if (trafficCtx) {
        new Chart(trafficCtx, {
            type: 'line',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                datasets: [{
                    label: 'System Traffic',
                    data: [65, 59, 80, 81, 56, 55],
                    fill: false,
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                }]
            }
        });
    }

    // Security Trends Chart (Dashboard)
    const securityTrendsCtx = document.getElementById('securityTrendsChart');
    if (securityTrendsCtx) {
        new Chart(securityTrendsCtx, {
            type: 'bar',
            data: {
                labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                datasets: [{
                    label: 'Security Incidents',
                    data: [12, 19, 3, 5, 2, 3, 7],
                    backgroundColor: 'rgba(231, 76, 60, 0.6)',
                    borderColor: 'rgb(231, 76, 60)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    // Real-time Threat Detection Chart (Security Page)
    const securityCtx = document.getElementById('securityChart');
    if (securityCtx) {
        new Chart(securityCtx, {
            type: 'line',
            data: {
                labels: ['12:00', '12:05', '12:10', '12:15', '12:20', '12:25'],
                datasets: [{
                    label: 'Threat Density',
                    data: [5, 10, 8, 15, 7, 10],
                    fill: true,
                    backgroundColor: 'rgba(231, 76, 60, 0.2)',
                    borderColor: 'rgb(231, 76, 60)',
                    tension: 0.4
                }]
            }
        });
    }

    // System Scan Interaction
    const scanButton = document.getElementById('scanButton');
    const scanStatus = document.getElementById('scanStatus');
    if (scanButton && scanStatus) {
        scanButton.addEventListener('click', function() {
            scanButton.disabled = true;
            scanButton.innerText = 'Scanning...';
            scanStatus.innerText = 'Initializing malware scan...';

            setTimeout(() => {
                scanStatus.innerText = 'Analyzing system files (45%)...';
            }, 1000);

            setTimeout(() => {
                scanStatus.innerText = 'Checking network vulnerabilities (80%)...';
            }, 2500);

            setTimeout(() => {
                scanButton.disabled = false;
                scanButton.innerText = 'Scan System Now';
                scanStatus.innerText = 'Scan Complete: No active threats found.';
                scanStatus.style.color = '#27ae60';
            }, 4000);
        });
    }
});
