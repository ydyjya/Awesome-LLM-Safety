document.addEventListener('DOMContentLoaded', function() {
    // Fetch repository stats from GitHub API
    fetchRepoStats();
    
    // Add smooth scrolling for navigation links
    addSmoothScrolling();
    
    // Handle language switch
    setupLanguageSwitch();
});

/**
 * Fetch repository statistics from GitHub API
 */
function fetchRepoStats() {
    const repoUrl = 'https://api.github.com/repos/ydyjya/Awesome-LLM-Safety';
    
    fetch(repoUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('stars').textContent = `★ ${data.stargazers_count} Stars`;
            document.getElementById('forks').textContent = `🍴 ${data.forks_count} Forks`;
            document.getElementById('issues').textContent = `❗ ${data.open_issues_count} Issues`;
        })
        .catch(error => {
            console.error('Error fetching repo stats:', error);
            document.getElementById('stars').textContent = '★ Stars';
            document.getElementById('forks').textContent = '🍴 Forks';
            document.getElementById('issues').textContent = '❗ Issues';
        });
}

/**
 * Add smooth scrolling behavior for navigation links
 */
function addSmoothScrolling() {
    const navLinks = document.querySelectorAll('.main-nav a');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70, // Adjust for fixed header
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Setup language switch functionality
 */
function setupLanguageSwitch() {
    const languageLinks = document.querySelectorAll('.language-switch a');
    
    languageLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Don't prevent default for actual page links
            if (this.getAttribute('href') && this.getAttribute('href') !== '#') {
                return; // Allow navigation to the linked page
            }
            
            e.preventDefault();
            
            // Remove active class from all links
            languageLinks.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
            
            // Get the language
            const language = this.textContent.trim();
            
            // Redirect to appropriate page
            if (language === '中文') {
                window.location.href = 'index_cn.html';
            } else if (language === 'English') {
                window.location.href = 'index.html';
            }
        });
    });
} 