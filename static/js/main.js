// #region agent log
fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:1',message:'main.js loaded',data:{},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'E'})}).catch((e)=>{console.error('Log failed:',e);});
// #endregion

// Mobile Menu Toggle
function toggleMobileMenu() {
    // #region agent log
    fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:2',message:'toggleMobileMenu called',data:{windowWidth:window.innerWidth},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'C'})}).catch(()=>{});
    // #endregion
    const menu = document.getElementById('nav-menu');
    const toggle = document.querySelector('.mobile-menu-toggle');
    // #region agent log
    fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:6',message:'Menu elements found',data:{menuFound:!!menu,toggleFound:!!toggle},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'C'})}).catch(()=>{});
    // #endregion
    if (menu && toggle) {
        menu.classList.toggle('active');
        toggle.classList.toggle('active');
        const isExpanded = menu.classList.contains('active');
        toggle.setAttribute('aria-expanded', isExpanded);
        // #region agent log
        fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:10',message:'Menu toggled',data:{isExpanded:isExpanded,menuHasActive:menu.classList.contains('active')},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'C'})}).catch(()=>{});
        // #endregion
    }
}

// Close mobile menu when clicking outside
document.addEventListener('click', function (e) {
    const menu = document.getElementById('nav-menu');
    const toggle = document.querySelector('.mobile-menu-toggle');
    if (menu && toggle && !menu.contains(e.target) && !toggle.contains(e.target)) {
        menu.classList.remove('active');
        toggle.classList.remove('active');
        toggle.setAttribute('aria-expanded', 'false');
    }
});

// Close mobile menu on window resize
window.addEventListener('resize', function () {
    if (window.innerWidth > 768) {
        const menu = document.getElementById('nav-menu');
        const toggle = document.querySelector('.mobile-menu-toggle');
        if (menu && toggle) {
            menu.classList.remove('active');
            toggle.classList.remove('active');
            toggle.setAttribute('aria-expanded', 'false');
        }
    }
});

// Language Switching
function switchLanguage(lang) {
    // #region agent log
    fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:38',message:'switchLanguage called',data:{lang:lang,currentUrl:window.location.href},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'A'})}).catch((err)=>{console.error('Log error:',err);});
    // #endregion
    const currentUrl = new URL(window.location.href);
    currentUrl.searchParams.set('lang', lang);
    // #region agent log
    fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:42',message:'Before redirect',data:{newUrl:currentUrl.toString()},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'A'})}).catch(()=>{});
    // #endregion
    window.location.href = currentUrl.toString();
}

// Theme Toggle
function toggleTheme() {
    // #region agent log
    fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:45',message:'toggleTheme called',data:{},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'B'})}).catch(()=>{});
    // #endregion
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    // #region agent log
    fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:48',message:'Theme change',data:{currentTheme:currentTheme,newTheme:newTheme},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'B'})}).catch(()=>{});
    // #endregion
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    // #region agent log
    fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:51',message:'Theme saved',data:{savedTheme:localStorage.getItem('theme')},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'B'})}).catch(()=>{});
    // #endregion
    updateThemeIcon(newTheme);
}

function updateThemeIcon(theme) {
    const icon = document.getElementById('theme-icon');
    if (icon) {
        icon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
    }
}

// Global error handler
window.addEventListener('error', function(e) {
    // #region agent log
    fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:error',message:'JavaScript error',data:{message:e.message,filename:e.filename,lineno:e.lineno,error:e.error?.toString()},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'E'})}).catch(()=>{});
    // #endregion
});

// Initialize theme from localStorage
document.addEventListener('DOMContentLoaded', function () {
    // #region agent log
    fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:61',message:'DOMContentLoaded - theme init',data:{bodyClass:document.body.className,htmlLang:document.documentElement.getAttribute('lang'),htmlDir:document.documentElement.getAttribute('dir')},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'E'})}).catch(()=>{});
    // #endregion
    const savedTheme = localStorage.getItem('theme') || 'light';
    // #region agent log
    fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'main.js:63',message:'Theme loaded from storage',data:{savedTheme:savedTheme,currentDataTheme:document.documentElement.getAttribute('data-theme')},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'B'})}).catch(()=>{});
    // #endregion
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);
});

// Code Editor Initialization
let codeEditor = null;
let exerciseEditor = null;

document.addEventListener('DOMContentLoaded', function () {
    // Initialize CodeMirror for code examples
    const codeTextarea = document.getElementById('code-editor');
    if (codeTextarea) {
        codeEditor = CodeMirror.fromTextArea(codeTextarea, {
            lineNumbers: true,
            mode: 'python',
            theme: 'dracula',
            readOnly: true,
            lineWrapping: true,
        });

        // Platform tabs functionality
        const platformTabs = document.querySelectorAll('.platform-tab');
        platformTabs.forEach(tab => {
            tab.addEventListener('click', function () {
                const platform = this.dataset.platform;

                // Update active tab
                platformTabs.forEach(t => t.classList.remove('active'));
                this.classList.add('active');

                // Update code editor content
                if (typeof CODE_EXAMPLES !== 'undefined' && CODE_EXAMPLES[platform]) {
                    codeEditor.setValue(CODE_EXAMPLES[platform]);
                }
            });
        });
    }

    // Initialize CodeMirror for exercise editor
    const exerciseTextarea = document.getElementById('exercise-editor');
    if (exerciseTextarea) {
        exerciseEditor = CodeMirror.fromTextArea(exerciseTextarea, {
            lineNumbers: true,
            mode: 'python',
            theme: 'dracula',
            lineWrapping: true,
        });
    }
});

// Enhanced Exercise Functions
function checkExercise() {
    if (!exerciseEditor) {
        showToast('Exercise editor not initialized', 'error');
        return;
    }

    const userCode = exerciseEditor.getValue();
    if (!userCode.trim()) {
        showToast('Please write your solution first!', 'warning');
        return;
    }

    // Improved validation: Ignore all whitespace differences including newlines
    if (typeof EXERCISE_SOLUTION !== 'undefined' && EXERCISE_SOLUTION) {
        // Normalize: remove all whitespace to compare logic
        const normalizeCode = (code) => code.replace(/\s+/g, ' ').trim();

        const userCodeNormalized = normalizeCode(userCode);
        const solutionNormalized = normalizeCode(EXERCISE_SOLUTION);

        if (userCodeNormalized === solutionNormalized) {
            showToast('Correct! Great job! 🎉', 'success', 4000);
            // Mark as complete
            if (typeof CURRENT_LESSON_ID !== 'undefined' && CURRENT_LESSON_ID) {
                updateProgress(CURRENT_LESSON_ID, true);
            }
        } else {
            showToast('Not quite right. Try again or check the solution!', 'warning');
        }
    } else {
        showToast('Solution not available for this exercise.', 'info');
    }
}

function showSolution() {
    const solutionContainer = document.getElementById('solution-container');
    if (solutionContainer) {
        solutionContainer.style.display = solutionContainer.style.display === 'none' ? 'block' : 'none';
    }
}

// Progress Tracking
function updateProgress(lessonId, completed) {
    if (!lessonId) return;

    fetch(`/api/lesson/${lessonId}/progress/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ completed: completed })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Update UI
                const progressBadge = document.querySelector('.progress-badge');
                if (progressBadge) {
                    if (data.completed) {
                        progressBadge.innerHTML = '<i class="fas fa-check-circle"></i> Completed';
                        progressBadge.style.background = 'var(--success-color)';
                    }
                }
            }
        })
        .catch(error => {
            console.error('Error updating progress:', error);
        });
}

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Mark lesson as complete when user scrolls to bottom
let progressMarked = false;
window.addEventListener('scroll', function () {
    if (progressMarked) return;

    const windowHeight = window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight;
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    // If user scrolled to 80% of the page
    if (scrollTop + windowHeight >= documentHeight * 0.8) {
        if (typeof CURRENT_LESSON_ID !== 'undefined' && CURRENT_LESSON_ID) {
            updateProgress(CURRENT_LESSON_ID, true);
            progressMarked = true;
        }
    }
});

// ===== Page Loading =====
function hidePageLoader(immediate = false) {
    const loader = document.getElementById('page-loader');
    if (loader) {
        if (immediate) {
            // Hide immediately (for back/forward navigation) - use class for CSS !important
            loader.classList.add('hidden');
        } else {
            // Hide with animation (for normal page loads)
            loader.classList.add('hidden');
        }
    }
}

// Hide loader when page is fully loaded
window.addEventListener('load', function () {
    setTimeout(hidePageLoader, 300);
});

// Also hide on DOMContentLoaded as fallback
document.addEventListener('DOMContentLoaded', function () {
    setTimeout(hidePageLoader, 100);
});

// Handle pageshow event (fires on back/forward navigation from cache)
window.addEventListener('pageshow', function (e) {
    const loader = document.getElementById('page-loader');
    if (loader) {
        // Always hide loader immediately on pageshow (handles back/forward cache)
        // For persisted pages (from bfcache), the loader state might be restored, so force hide
        loader.classList.add('hidden'); // CSS !important will handle display
    }
});

// Show loader on navigation
document.addEventListener('click', function (e) {
    const link = e.target.closest('a');
    if (link && link.href) {
        // Check if it's an anchor link (href starts with # or only hash differs)
        const hrefAttr = link.getAttribute('href');
        if (hrefAttr && (hrefAttr.startsWith('#') || hrefAttr.startsWith('javascript:'))) {
            // Don't show loader for anchor links or javascript links
            return;
        }
        
        // Check if it's a same-page anchor (only hash differs)
        try {
            const linkUrl = new URL(link.href, window.location.href);
            const currentUrl = new URL(window.location.href);
            if (linkUrl.pathname === currentUrl.pathname && 
                linkUrl.search === currentUrl.search && 
                linkUrl.hash !== currentUrl.hash) {
                // Only hash differs - this is an anchor link, don't show loader
                return;
            }
        } catch (err) {
            // Invalid URL, skip
            return;
        }
        
        const currentHost = window.location.host;
        let linkHost;
        try {
            linkHost = new URL(link.href, window.location.href).host;
        } catch (err) {
            return;
        }
        
        if (linkHost === currentHost || linkHost === '') {
            const loader = document.getElementById('page-loader');
            if (loader) {
                loader.classList.remove('hidden'); // CSS will handle display: flex via !important
            }
        }
    }
});

// Hide loader when page is about to unload (handles back button pressed during navigation)
window.addEventListener('beforeunload', function () {
    const loader = document.getElementById('page-loader');
    if (loader) {
        // Hide immediately when navigation is about to happen
        loader.classList.add('hidden'); // CSS !important will handle display
    }
});

// Handle browser back/forward navigation
window.addEventListener('popstate', function (e) {
    const loader = document.getElementById('page-loader');
    if (loader) {
        // Force hide loader immediately on back/forward navigation
        hidePageLoader(true);
    }
});

// Handle page visibility changes (when tab becomes visible again)
document.addEventListener('visibilitychange', function () {
    if (!document.hidden) {
        const loader = document.getElementById('page-loader');
        if (loader) {
            // If loader is visible when page becomes visible, hide it immediately
            const computedDisplay = window.getComputedStyle(loader).display;
            if (computedDisplay !== 'none' && !loader.classList.contains('hidden')) {
                hidePageLoader(true);
            }
        }
    }
});

// Initial check: always ensure loader is hidden on page load (handles edge cases and bfcache)
(function() {
    function ensureLoaderHidden() {
        const loader = document.getElementById('page-loader');
        if (loader) {
            const computedDisplay = window.getComputedStyle(loader).display;
            if (computedDisplay !== 'none') {
                loader.classList.add('hidden'); // CSS !important will handle display
            }
        }
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', ensureLoaderHidden);
    } else {
        // Document already loaded - check immediately
        ensureLoaderHidden();
    }
})();

// ===== Lazy Loading with Intersection Observer =====
function initLazyLoading() {
    const lazyElements = document.querySelectorAll('.lazy-load');

    if ('IntersectionObserver' in window) {
        const lazyObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const element = entry.target;
                    element.classList.add('loaded');
                    observer.unobserve(element);
                }
            });
        }, {
            rootMargin: '50px',
            threshold: 0.1
        });

        lazyElements.forEach(element => {
            lazyObserver.observe(element);
        });
    } else {
        // Fallback for browsers without IntersectionObserver
        lazyElements.forEach(element => {
            element.classList.add('loaded');
        });
    }
}

// ===== Skeleton Screen Logic =====
function showSkeletonScreens() {
    const skeletonCards = document.querySelectorAll('.skeleton-card');
    const courseCards = document.querySelectorAll('.course-card');

    // Show skeletons if no course cards are loaded yet
    if (courseCards.length === 0) {
        skeletonCards.forEach(skeleton => {
            skeleton.style.display = 'flex';
        });
    }
}

function hideSkeletonScreens() {
    const skeletonCards = document.querySelectorAll('.skeleton-card');
    skeletonCards.forEach(skeleton => {
        skeleton.style.display = 'none';
    });
}

// Initialize lazy loading and skeleton screens
document.addEventListener('DOMContentLoaded', function () {
    initLazyLoading();
    showSkeletonScreens();

    // Hide skeletons after a short delay (simulating content load)
    setTimeout(() => {
        hideSkeletonScreens();
        // Trigger lazy load animation for visible cards
        const visibleCards = document.querySelectorAll('.course-card');
        visibleCards.forEach((card, index) => {
            setTimeout(() => {
                card.classList.add('loaded');
            }, index * 100);
        });
    }, 500);
});

// ===== Enhanced Platform Tab Switching =====
document.addEventListener('DOMContentLoaded', function () {
    const platformTabs = document.querySelectorAll('.platform-tab');

    platformTabs.forEach(tab => {
        tab.addEventListener('click', function () {
            const platform = this.dataset.platform;

            // Remove active class from all tabs
            platformTabs.forEach(t => {
                t.classList.remove('active');
            });

            // Add active class to clicked tab with animation
            this.classList.add('active');

            // Update code editor content with smooth transition
            if (codeEditor && typeof CODE_EXAMPLES !== 'undefined' && CODE_EXAMPLES[platform]) {
                // Fade out
                const editorElement = codeEditor.getWrapperElement();
                editorElement.style.opacity = '0.5';
                editorElement.style.transition = 'opacity 0.2s ease';

                setTimeout(() => {
                    codeEditor.setValue(CODE_EXAMPLES[platform]);
                    // Fade in
                    editorElement.style.opacity = '1';
                }, 200);
            }
        });
    });
});

// ===== Smooth Scroll Enhancement =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && href.length > 1) {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

// ===== Platform Detection and Auto-highlighting =====
function detectPlatform() {
    const userAgent = navigator.userAgent.toLowerCase();
    if (userAgent.includes('mac')) {
        return 'mac';
    } else if (userAgent.includes('win')) {
        return 'windows';
    }
    return 'default';
}

document.addEventListener('DOMContentLoaded', function () {
    const detectedPlatform = detectPlatform();
    const platformTabs = document.querySelectorAll('.platform-tab');

    // Auto-select platform tab if available
    platformTabs.forEach(tab => {
        const tabPlatform = tab.dataset.platform;
        if (tabPlatform === detectedPlatform && !document.querySelector('.platform-tab.active')) {
            tab.click();
        }
    });

    // Highlight platform sections on course list
    if (window.location.pathname === '/' || window.location.pathname.includes('course_list')) {
        const platformSections = document.querySelectorAll('.platform-section');
        platformSections.forEach(section => {
            if (section.classList.contains(`${detectedPlatform}-section`)) {
                section.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }
        });
    }
});

// ===== Keyboard Shortcuts =====
document.addEventListener('keydown', function (e) {
    // Escape key to close chat
    if (e.key === 'Escape') {
        const chatContainer = document.getElementById('chat-container');
        if (chatContainer && chatContainer.classList.contains('active')) {
            toggleChat();
        }
    }

    // Ctrl/Cmd + K to open chat
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const chatContainer = document.getElementById('chat-container');
        if (chatContainer && !chatContainer.classList.contains('active')) {
            toggleChat();
        }
    }

    // Arrow keys for lesson navigation (when not in input/textarea)
    if (!['INPUT', 'TEXTAREA'].includes(e.target.tagName)) {
        if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
            const prevLink = document.querySelector('.lesson-navigation .nav-link.prev');
            const nextLink = document.querySelector('.lesson-navigation .nav-link.next');

            if (e.key === 'ArrowLeft' && prevLink && !prevLink.style.opacity) {
                prevLink.click();
            } else if (e.key === 'ArrowRight' && nextLink && !nextLink.style.opacity) {
                nextLink.click();
            }
        }
    }
});

// ===== Smooth Scroll for Anchor Links =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && href.length > 1) {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                const offset = 100; // Account for sticky navbar
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        }
    });
});

// ===== Progress Bar Animation =====
function animateProgressBar() {
    const progressBars = document.querySelectorAll('.progress-fill');
    progressBars.forEach(bar => {
        const width = bar.style.width || '0%';
        bar.style.width = '0%';
        setTimeout(() => {
            bar.style.width = width;
        }, 100);
    });
}

document.addEventListener('DOMContentLoaded', function () {
    animateProgressBar();
});

// ===== Toast Notification System =====
function showToast(message, type = 'info', duration = 3000) {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;

    const icons = {
        success: 'fa-check-circle',
        error: 'fa-exclamation-circle',
        warning: 'fa-exclamation-triangle',
        info: 'fa-info-circle'
    };

    toast.innerHTML = `
        <i class="fas ${icons[type] || icons.info}" aria-hidden="true"></i>
        <span>${message}</span>
    `;

    document.body.appendChild(toast);

    // Trigger animation
    setTimeout(() => {
        toast.classList.add('show');
    }, 10);

    // Remove after duration
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => {
            document.body.removeChild(toast);
        }, 300);
    }, duration);
}

// ===== Enhanced Error Handling =====
window.addEventListener('error', function (e) {
    console.error('Error:', e.error);
    if (typeof showToast === 'function') {
        showToast('An error occurred. Please try again.', 'error');
    }
});

// ===== Success Feedback =====
function showSuccess(message) {
    showToast(message, 'success');
}

// ===== Enhanced Exercise Feedback =====
const originalCheckExercise = window.checkExercise;
if (typeof originalCheckExercise === 'function') {
    window.checkExercise = function () {
        if (!exerciseEditor) {
            showToast('Exercise editor not initialized', 'error');
            return;
        }

        const userCode = exerciseEditor.getValue();
        if (!userCode.trim()) {
            showToast('Please write your solution first!', 'warning');
            return;
        }

        if (typeof EXERCISE_SOLUTION !== 'undefined' && EXERCISE_SOLUTION) {
            const userCodeNormalized = userCode.replace(/\s+/g, ' ').trim();
            const solutionNormalized = EXERCISE_SOLUTION.replace(/\s+/g, ' ').trim();

            if (userCodeNormalized === solutionNormalized) {
                showSuccess('Correct! Great job! 🎉');
                if (typeof CURRENT_LESSON_ID !== 'undefined' && CURRENT_LESSON_ID) {
                    updateProgress(CURRENT_LESSON_ID, true);
                }
            } else {
                showToast('Not quite right. Try again or check the solution!', 'warning');
            }
        } else {
            showToast('Solution not available for this exercise.', 'info');
        }
    };
}


