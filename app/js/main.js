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

    // AI Assistant Chat Interaction
    const chatInput = document.getElementById('chatInput');
    const sendButton = document.getElementById('sendButton');
    const chatMessages = document.getElementById('chatMessages');

    if (sendButton && chatInput && chatMessages) {
        const appendMessage = (text, sender) => {
            const messageDiv = document.createElement('div');
            messageDiv.classList.add('message', sender);
            const bubbleDiv = document.createElement('div');
            bubbleDiv.classList.add('chat-bubble');
            bubbleDiv.textContent = text;
            messageDiv.appendChild(bubbleDiv);
            chatMessages.appendChild(messageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        };

        const handleSend = async () => {
            const prompt = chatInput.value.trim();
            if (!prompt) return;

            appendMessage(prompt, 'user');
            chatInput.value = '';

            try {
                const response = await fetch('http://localhost:8000/ask', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ prompt: prompt, provider: 'ollama' }),
                });

                if (response.ok) {
                    const data = await response.json();
                    appendMessage(data.response, 'ai');
                } else {
                    appendMessage('Error: Could not connect to the AI service.', 'ai');
                }
            } catch (error) {
                console.error('Error:', error);
                appendMessage('Error: Failed to fetch response from AI.', 'ai');
            }
        };

        sendButton.addEventListener('click', handleSend);
        chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') handleSend();
        });
    }

    // Operations Page Dynamic Data
    const serverTableBody = document.querySelector('#serverTable tbody');
    if (serverTableBody) {
        const fetchMetrics = async () => {
            try {
                const response = await fetch('http://localhost:8000/metrics');
                if (response.ok) {
                    const data = await response.json();
                    serverTableBody.innerHTML = '';
                    data.servers.forEach(server => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td>${server.host}</td>
                            <td><span class="status healthy">${server.status}</span></td>
                            <td>${server.cpu}</td>
                            <td>${server.memory}</td>
                            <td><span class="status healthy" style="color: ${server.security === 'Secure' ? '#27ae60' : '#e67e22'};">${server.security}</span></td>
                        `;
                        serverTableBody.appendChild(row);
                    });
                }
            } catch (error) {
                console.error('Error fetching metrics:', error);
            }
        };

        fetchMetrics();
        setInterval(fetchMetrics, 5000);
    }

    // Kanban Board Interaction
    const addTaskButton = document.getElementById('addTaskButton');
    const newTaskInput = document.getElementById('newTaskInput');
    const todoColumn = document.getElementById('todoColumn');

    if (addTaskButton && newTaskInput && todoColumn) {
        addTaskButton.addEventListener('click', function() {
            const taskText = newTaskInput.value.trim();
            if (taskText) {
                const card = document.createElement('div');
                card.className = 'kanban-card';
                card.textContent = taskText;

                // Insert before the add-task div
                const addTaskDiv = todoColumn.querySelector('.add-task');
                todoColumn.insertBefore(card, addTaskDiv);

                newTaskInput.value = '';
            }
        });

        newTaskInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                addTaskButton.click();
            }
        });
    }

    // Integrations Page Logic
    const posTableBody = document.querySelector('#posTable tbody');
    const githubReposDiv = document.getElementById('githubRepos');
    const googleServicesDiv = document.getElementById('googleServices');

    if (posTableBody || githubReposDiv || googleServicesDiv) {
        const fetchIntegrations = async () => {
            try {
                // Fetch POS data
                const posResponse = await fetch('http://localhost:8000/integrations/pos');
                if (posResponse.ok && posTableBody) {
                    const data = await posResponse.json();
                    posTableBody.innerHTML = '';
                    data.integrations.forEach(item => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td><strong>${item.name}</strong></td>
                            <td>${item.type}</td>
                            <td><span class="status healthy">${item.status}</span></td>
                            <td>${item.last_sync}</td>
                        `;
                        posTableBody.appendChild(row);
                    });
                }

                // Fetch GitHub data
                const githubResponse = await fetch('http://localhost:8000/integrations/github');
                if (githubResponse.ok && githubReposDiv) {
                    const data = await githubResponse.json();
                    githubReposDiv.innerHTML = '';
                    data.repositories.forEach(repo => {
                        const div = document.createElement('div');
                        div.className = 'kanban-card';
                        div.innerHTML = `
                            <strong>${repo.name}</strong><br>
                            <small>⭐ ${repo.stars} | 🍴 ${repo.forks} | ❗ ${repo.open_issues} issues</small>
                        `;
                        githubReposDiv.appendChild(div);
                    });
                    document.getElementById('githubStatus').textContent = data.status;
                }

                // Fetch Google data
                const googleResponse = await fetch('http://localhost:8000/integrations/google');
                if (googleResponse.ok && googleServicesDiv) {
                    const data = await googleResponse.json();
                    googleServicesDiv.innerHTML = '';
                    data.services.forEach(service => {
                        const div = document.createElement('div');
                        div.className = 'kanban-card';
                        div.innerHTML = `
                            <strong>${service.name}</strong><br>
                            <small>Status: ${service.status} | ${service.storage_used || service.events_today + ' events today'}</small>
                        `;
                        googleServicesDiv.appendChild(div);
                    });
                    document.getElementById('googleStatus').textContent = data.status;
                }
            } catch (error) {
                console.error('Error fetching integration data:', error);
            }
        };

        fetchIntegrations();
    }
});
