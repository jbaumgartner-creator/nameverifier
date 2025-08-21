/**
 * Name Variations Finder - Main JavaScript
 * Handles search functionality, form validation, and UI interactions
 */

document.addEventListener('DOMContentLoaded', function() {
    initializeSearch();
    initializeFormValidation();
    initializeAnimations();
});

/**
 * Initialize search functionality
 */
function initializeSearch() {
    const nameInput = document.getElementById('nameInput');
    
    if (nameInput) {
        // Auto-focus on the search input
        nameInput.focus();
        
        // Handle Enter key in search input
        nameInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                const form = this.closest('form');
                if (form && form.checkValidity()) {
                    form.submit();
                }
            }
        });
        
        // Auto-capitalize first letter
        nameInput.addEventListener('input', function(e) {
            const value = e.target.value;
            if (value.length === 1) {
                e.target.value = value.charAt(0).toUpperCase();
            }
        });
    }
}

/**
 * Initialize form validation
 */
function initializeFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
}

/**
 * Initialize animations and effects
 */
function initializeAnimations() {
    // Animate variation cards on load
    const variationCards = document.querySelectorAll('.variation-card');
    variationCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            card.style.transition = 'all 0.3s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 50);
    });
    
    // Add hover effects to variation cards
    variationCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
            this.style.boxShadow = '0 4px 8px rgba(0,0,0,0.1)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '';
        });
    });
}

/**
 * Copy text to clipboard with visual feedback
 */
function copyToClipboard() {
    const variationsList = document.getElementById('variationsList');
    if (!variationsList) return;
    
    const text = variationsList.textContent.trim();
    if (!text) return;
    
    // Use modern clipboard API if available
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(() => {
            showCopySuccess();
        }).catch(() => {
            fallbackCopyToClipboard(text);
        });
    } else {
        fallbackCopyToClipboard(text);
    }
}

/**
 * Fallback copy method for older browsers
 */
function fallbackCopyToClipboard(text) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    textArea.style.top = '-999999px';
    
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    
    try {
        document.execCommand('copy');
        showCopySuccess();
    } catch (err) {
        console.error('Failed to copy text: ', err);
        showCopyError();
    }
    
    document.body.removeChild(textArea);
}

/**
 * Show copy success feedback
 */
function showCopySuccess() {
    const button = event.target.closest('button');
    if (!button) return;
    
    const originalHTML = button.innerHTML;
    const originalClasses = button.className;
    
    button.innerHTML = '<i class="fas fa-check me-1"></i>Copied!';
    button.className = 'btn btn-sm btn-success';
    button.disabled = true;
    
    setTimeout(() => {
        button.innerHTML = originalHTML;
        button.className = originalClasses;
        button.disabled = false;
    }, 2000);
}

/**
 * Show copy error feedback
 */
function showCopyError() {
    const button = event.target.closest('button');
    if (!button) return;
    
    const originalHTML = button.innerHTML;
    const originalClasses = button.className;
    
    button.innerHTML = '<i class="fas fa-exclamation-triangle me-1"></i>Failed';
    button.className = 'btn btn-sm btn-danger';
    
    setTimeout(() => {
        button.innerHTML = originalHTML;
        button.className = originalClasses;
    }, 2000);
    
    // Also show an alert as fallback
    alert('Unable to copy to clipboard. Please select and copy the text manually.');
}

/**
 * Handle search suggestions (future enhancement)
 */
function initializeSearchSuggestions() {
    const nameInput = document.getElementById('nameInput');
    if (!nameInput) return;
    
    // This would integrate with the /api/names endpoint to provide suggestions
    // Implementation can be added later for enhanced UX
}

/**
 * Scroll to results smoothly
 */
function scrollToResults() {
    const resultsSection = document.querySelector('.card.shadow-sm');
    if (resultsSection && document.querySelector('.variation-card')) {
        resultsSection.scrollIntoView({ 
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Call scroll to results after page load if there are results
window.addEventListener('load', function() {
    if (document.querySelector('.variation-card')) {
        setTimeout(scrollToResults, 500);
    }
});
