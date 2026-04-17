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

    // Sprint Progress Chart
    const sprintCtx = document.getElementById('sprintProgressChart');
    if (sprintCtx) {
        new Chart(sprintCtx, {
            type: 'doughnut',
            data: {
                labels: ['Completed', 'In Progress', 'To Do'],
                datasets: [{
                    label: 'Sprint Progress',
                    data: [300, 50, 100],
                    backgroundColor: [
                        'rgb(46, 204, 113)',
                        'rgb(52, 152, 219)',
                        'rgb(231, 76, 60)'
                    ]
                }]
            }
        });
    }
});
