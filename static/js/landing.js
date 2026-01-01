// Landing Page Interactive Features

document.addEventListener('DOMContentLoaded', function() {
    // #region agent log
    fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'landing.js:3',message:'Landing page DOMContentLoaded',data:{},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'E'})}).catch(()=>{});
    // #endregion
    initArchitectureDiagram();
    initSmoothScroll();
    initScrollAnimations();
});

// Get current language
function getCurrentLanguage() {
    const htmlLang = document.documentElement.getAttribute('lang');
    const bodyRtl = document.body.classList.contains('rtl');
    return htmlLang === 'fa' || bodyRtl ? 'fa' : 'en';
}

// Architecture Diagram Component Data with Enhanced Information
const componentData = {
    'http-request': {
        icon: '<i class="fas fa-globe"></i>',
        title: { en: 'HTTP Request', fa: 'درخواست HTTP' },
        description: {
            en: 'The request cycle begins when a user\'s browser sends an HTTP request to the Django server. This request contains information about the URL, HTTP method (GET, POST, etc.), headers, and any data.',
            fa: 'چرخه درخواست زمانی شروع می‌شود که مرورگر کاربر یک درخواست HTTP به سرور Django ارسال می‌کند. این درخواست شامل اطلاعات URL، متد HTTP (GET، POST و غیره)، هدرها و داده‌ها است.'
        },
        flowPosition: { en: 'Step 1: Request Initiation', fa: 'مرحله ۱: شروع درخواست' },
        relationships: { en: ['URL Routing'], fa: ['مسیریابی URL'] },
        codeExample: {
            en: 'Browser → GET /courses/\nHTTP/1.1\nHost: example.com',
            fa: 'مرورگر → GET /courses/\nHTTP/1.1\nHost: example.com'
        },
        features: {
            en: ['HTTP methods (GET, POST, PUT, DELETE)', 'Request headers', 'URL parameters', 'Query strings', 'Request body'],
            fa: ['متدهای HTTP (GET، POST، PUT، DELETE)', 'هدرهای درخواست', 'پارامترهای URL', 'رشته‌های Query', 'بدنه درخواست']
        }
    },
    url: {
        icon: '<i class="fas fa-route"></i>',
        title: { en: 'URL Routing', fa: 'مسیریابی URL' },
        description: {
            en: 'URL routing is Django\'s way of mapping URLs to views. The URLconf module (urls.py) contains URL patterns that tell Django which view function to call for a given URL pattern.',
            fa: 'مسیریابی URL روش Django برای نگاشت URLها به viewها است. ماژول URLconf (urls.py) شامل الگوهای URL است که به Django می‌گوید برای یک الگوی URL مشخص چه تابع view را فراخوانی کند.'
        },
        flowPosition: { en: 'Step 2: URL Resolution', fa: 'مرحله ۲: تفکیک URL' },
        relationships: { en: ['HTTP Request', 'Middleware'], fa: ['درخواست HTTP', 'میان‌افزار'] },
        codeExample: {
            en: '# urls.py\nfrom django.urls import path\nfrom . import views\n\nurlpatterns = [\n    path(\'courses/\', views.course_list),\n]',
            fa: '# urls.py\nfrom django.urls import path\nfrom . import views\n\nurlpatterns = [\n    path(\'courses/\', views.course_list),\n]'
        },
        features: {
            en: ['URL patterns and path converters', 'Named URL patterns for reverse lookup', 'Including other URL configurations', 'URL namespacing', 'Regular expressions support'],
            fa: ['الگوهای URL و مبدل‌های مسیر', 'الگوهای URL نام‌گذاری شده برای جستجوی معکوس', 'فراخوانی سایر تنظیمات URL', 'فضای نام URL', 'پشتیبانی از عبارات منظم']
        }
    },
    middleware: {
        icon: '<i class="fas fa-cogs"></i>',
        title: { en: 'Middleware', fa: 'میان‌افزار' },
        description: {
            en: 'Middleware is a series of hooks into Django\'s request/response processing. It\'s a lightweight, low-level plugin system for globally altering Django\'s input or output.',
            fa: 'Middleware مجموعه‌ای از قلاب‌ها در فرآیند پردازش درخواست/پاسخ Django است. این یک سیستم افزونه سبک‌وزن و سطح پایین است که امکان تغییر سراسری ورودی یا خروجی Django را فراهم می‌کند.'
        },
        flowPosition: { en: 'Step 3: Middleware Processing', fa: 'مرحله ۳: پردازش میان‌افزار' },
        relationships: { en: ['URL Routing', 'Views'], fa: ['مسیریابی URL', 'Viewها'] },
        codeExample: {
            en: '# settings.py\nMIDDLEWARE = [\n    \'django.middleware.security.SecurityMiddleware\',\n    \'django.contrib.sessions.middleware.SessionMiddleware\',\n]',
            fa: '# settings.py\nMIDDLEWARE = [\n    \'django.middleware.security.SecurityMiddleware\',\n    \'django.contrib.sessions.middleware.SessionMiddleware\',\n]'
        },
        features: {
            en: ['Process requests before views', 'Process responses after views', 'Global exception handling', 'Session management', 'CSRF protection', 'Authentication processing'],
            fa: ['پردازش درخواست‌ها پیش از viewها', 'پردازش پاسخ‌ها پس از viewها', 'مدیریت خطاهای سراسری', 'مدیریت جلسه کاربری', 'محافظت در برابر CSRF', 'پردازش احراز هویت']
        }
    },
    views: {
        icon: '<i class="fas fa-code"></i>',
        title: { en: 'Views', fa: 'Viewها' },
        description: {
            en: 'Views are Python functions that receive web requests and return web responses. They handle the business logic of your application, process data, and decide what response to return. Views interact with Models to fetch data and with Templates to render HTML.',
            fa: 'Viewها توابع Python هستند که درخواست‌های وب را دریافت کرده و پاسخ‌های وب را برمی‌گردانند. این توابع منطق کسب‌وکار برنامه شما را پیاده‌سازی می‌کنند، داده‌ها را پردازش کرده و نوع پاسخ مناسب را تعیین می‌کنند. Viewها با Modelها تعامل می‌کنند تا داده دریافت کنند و با Templateها برای رندر HTML.'
        },
        flowPosition: { en: 'Step 4: View Processing', fa: 'مرحله ۴: پردازش View' },
        relationships: { en: ['Middleware', 'Models', 'Templates'], fa: ['میان‌افزار', 'مدل‌ها', 'قالب‌ها'] },
        codeExample: {
            en: '# views.py\nfrom django.shortcuts import render\nfrom .models import Course\n\ndef course_list(request):\n    courses = Course.objects.all()\n    return render(request, \'courses/list.html\', {\n        \'courses\': courses\n    })',
            fa: '# views.py\nfrom django.shortcuts import render\nfrom .models import Course\n\ndef course_list(request):\n    courses = Course.objects.all()\n    return render(request, \'courses/list.html\', {\n        \'courses\': courses\n    })'
        },
        features: {
            en: ['Function-based views (FBV)', 'Class-based views (CBV)', 'Request handling (GET, POST, etc.)', 'Template rendering', 'JSON responses', 'File downloads'],
            fa: ['Viewهای مبتنی بر تابع (FBV)', 'Viewهای مبتنی بر کلاس (CBV)', 'پردازش انواع درخواست (GET، POST و غیره)', 'رندر قالب‌ها', 'ارسال پاسخ‌های JSON', 'دانلود فایل']
        }
    },
    models: {
        icon: '<i class="fas fa-database"></i>',
        title: { en: 'Models', fa: 'مدل‌ها' },
        description: {
            en: 'Models define the structure of your data, relationships between data, and behaviors of data. Django\'s ORM translates Python model definitions into database tables and provides a Python API for database operations. Views query Models to retrieve data.',
            fa: 'مدل‌ها ساختار داده‌های شما، روابط بین داده‌ها و رفتارهای داده را تعریف می‌کنند. ORM Django تعاریف مدل Python را به جداول پایگاه داده ترجمه می‌کند و یک API Python برای عملیات پایگاه داده ارائه می‌دهد. Viewها از Modelها برای دریافت داده استفاده می‌کنند.'
        },
        flowPosition: { en: 'Step 5: Database Query', fa: 'مرحله ۵: پرس‌وجوی پایگاه داده' },
        relationships: { en: ['Views'], fa: ['Viewها'] },
        codeExample: {
            en: '# models.py\nfrom django.db import models\n\nclass Course(models.Model):\n    title = models.CharField(max_length=200)\n    slug = models.SlugField(unique=True)\n    \n    def __str__(self):\n        return self.title',
            fa: '# models.py\nfrom django.db import models\n\nclass Course(models.Model):\n    title = models.CharField(max_length=200)\n    slug = models.SlugField(unique=True)\n    \n    def __str__(self):\n        return self.title'
        },
        features: {
            en: ['Object-Relational Mapping (ORM)', 'Database abstraction', 'Model relationships (ForeignKey, ManyToMany)', 'Database migrations', 'Query API', 'Model validation'],
            fa: ['نگاشت شی‌گرا-رابطه‌ای (ORM)', 'انتزاع از پایگاه داده', 'تعریف روابط مدل (ForeignKey، ManyToMany)', 'سیستم مهاجرت پایگاه داده', 'API پرس‌وجو', 'اعتبارسنجی خودکار مدل']
        }
    },
    templates: {
        icon: '<i class="fas fa-file-code"></i>',
        title: { en: 'Templates', fa: 'قالب‌ها' },
        description: {
            en: 'Templates are text files that define the structure or layout of a file (such as an HTML page), with placeholders used to represent actual content. Django uses its own template system. Views pass data to Templates through Context objects.',
            fa: 'قالب‌ها فایل‌های متنی هستند که ساختار یا چیدمان یک فایل (مانند یک صفحه HTML) را تعریف می‌کنند، با متغیرهای جایگزین که برای نشان دادن محتوای واقعی استفاده می‌شوند. Django از سیستم قالب خود استفاده می‌کند. Viewها داده را از طریق Context به Templateها منتقل می‌کنند.'
        },
        flowPosition: { en: 'Step 6: Template Rendering', fa: 'مرحله ۶: رندر قالب' },
        relationships: { en: ['Views', 'Context'], fa: ['Viewها', 'Context'] },
        codeExample: {
            en: '<!-- templates/courses/list.html -->\n{% for course in courses %}\n    <h2>{{ course.title }}</h2>\n{% endfor %}',
            fa: '<!-- templates/courses/list.html -->\n{% for course in courses %}\n    <h2>{{ course.title }}</h2>\n{% endfor %}'
        },
        features: {
            en: ['Template inheritance', 'Template tags and filters', 'Context variables', 'Template includes', 'Custom template tags', 'Template caching'],
            fa: ['سیستم وراثت قالب', 'تگ‌ها و فیلترهای قالب', 'متغیرهای Context', 'شامل کردن قالب‌های دیگر', 'ایجاد تگ‌های قالب سفارشی', 'کش‌سازی قالب‌ها']
        }
    },
    context: {
        icon: '<i class="fas fa-box"></i>',
        title: { en: 'Context', fa: 'Context' },
        description: {
            en: 'Context is a dictionary-like object that maps template variable names to Python objects. Views pass Context objects to Templates, which use them to render dynamic content. The Context bridges the gap between Views (data) and Templates (presentation).',
            fa: 'Context یک شیء شبیه dictionary است که نام متغیرهای قالب را به اشیاء Python نگاشت می‌کند. Viewها اشیاء Context را به Templateها منتقل می‌کنند که از آنها برای رندر محتوای پویا استفاده می‌کنند. Context پلی بین Viewها (داده) و Templateها (ارائه) است.'
        },
        flowPosition: { en: 'Step 7: Context Binding', fa: 'مرحله ۷: اتصال Context' },
        relationships: { en: ['Views', 'Templates', 'HTTP Response'], fa: ['Viewها', 'قالب‌ها', 'پاسخ HTTP'] },
        codeExample: {
            en: '# In views.py\ncontext = {\n    \'courses\': Course.objects.all(),\n    \'user\': request.user\n}\nreturn render(request, \'template.html\', context)',
            fa: '# In views.py\ncontext = {\n    \'courses\': Course.objects.all(),\n    \'user\': request.user\n}\nreturn render(request, \'template.html\', context)'
        },
        features: {
            en: ['Dictionary-like structure', 'Variable mapping', 'Data binding', 'Template variable access', 'Automatic escaping'],
            fa: ['ساختار شبیه dictionary', 'نگاشت متغیر', 'اتصال داده', 'دسترسی به متغیرهای قالب', 'فرار خودکار']
        }
    },
    'http-response': {
        icon: '<i class="fas fa-paper-plane"></i>',
        title: { en: 'HTTP Response', fa: 'پاسخ HTTP' },
        description: {
            en: 'The final step is sending the rendered HTML (or other content) back to the user\'s browser as an HTTP response. The response includes status codes, headers, and the rendered content. The cycle completes when the browser receives and displays the response.',
            fa: 'مرحله نهایی ارسال HTML رندر شده (یا محتوای دیگر) به مرورگر کاربر به عنوان پاسخ HTTP است. پاسخ شامل کدهای وضعیت، هدرها و محتوای رندر شده است. چرخه زمانی تکمیل می‌شود که مرورگر پاسخ را دریافت و نمایش می‌دهد.'
        },
        flowPosition: { en: 'Step 8: Response Delivery', fa: 'مرحله ۸: تحویل پاسخ' },
        relationships: { en: ['Context', 'Templates'], fa: ['Context', 'قالب‌ها'] },
        codeExample: {
            en: '# Response is automatically created by render()\nreturn render(request, \'template.html\', context)\n# Becomes:\n# HTTP/1.1 200 OK\n# Content-Type: text/html\n# <html>...</html>',
            fa: '# Response به صورت خودکار توسط render() ایجاد می‌شود\nreturn render(request, \'template.html\', context)\n# تبدیل می‌شود به:\n# HTTP/1.1 200 OK\n# Content-Type: text/html\n# <html>...</html>'
        },
        features: {
            en: ['HTTP status codes', 'Response headers', 'Rendered HTML', 'JSON responses', 'File downloads', 'Redirects'],
            fa: ['کدهای وضعیت HTTP', 'هدرهای پاسخ', 'HTML رندر شده', 'پاسخ‌های JSON', 'دانلود فایل', 'Redirectها']
        }
    }
};

// Flow Animation State
let flowState = {
    currentStep: 0,
    totalSteps: 8,
    isPlaying: false,
    animationInterval: null,
    stepDuration: 2000 // milliseconds
};

// Initialize Architecture Diagram
function initArchitectureDiagram() {
    const components = document.querySelectorAll('.flow-component');
    const infoPanel = document.getElementById('component-info');
    const infoClose = document.getElementById('info-close');
    const infoIcon = document.getElementById('info-icon');
    const infoTitle = document.getElementById('info-title');
    const infoDescription = document.getElementById('info-description');
    const infoFeatures = document.getElementById('info-features');
    const infoFlowPosition = document.getElementById('info-flow-position');
    const infoRelationships = document.getElementById('info-relationships');
    const infoCodeExample = document.getElementById('info-code-example');

    // Initialize flow controls
    initFlowControls();

    // Handle component clicks
    components.forEach(component => {
        component.addEventListener('click', function() {
            const componentType = this.dataset.component;
            showComponentInfo(componentType, this);
        });

        // Hover effect to show connections
        component.addEventListener('mouseenter', function() {
            const componentType = this.dataset.component;
            highlightRelatedComponents(componentType);
        });

        component.addEventListener('mouseleave', function() {
            clearComponentHighlights();
        });
    });

    // Close info panel
    if (infoClose) {
        infoClose.addEventListener('click', function(e) {
            e.stopPropagation();
            infoPanel.classList.remove('active');
            clearComponentHighlights();
        });
    }

    // Close panel when clicking outside
    document.addEventListener('click', function(e) {
        if (!infoPanel.contains(e.target) && 
            !Array.from(components).some(c => c.contains(e.target)) &&
            !e.target.closest('.flow-component')) {
            infoPanel.classList.remove('active');
            clearComponentHighlights();
        }
    });

    // Keyboard support (ESC to close)
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && infoPanel.classList.contains('active')) {
            infoPanel.classList.remove('active');
            clearComponentHighlights();
        }
    });

    // Function to show component info
    function showComponentInfo(componentType, componentElement) {
        const data = componentData[componentType];
        if (!data) return;

        const lang = getCurrentLanguage();

        // Update info panel content
        infoIcon.innerHTML = data.icon;
        infoTitle.textContent = data.title[lang] || data.title.en;
        infoDescription.textContent = data.description[lang] || data.description.en;

        // Flow position
        if (infoFlowPosition && data.flowPosition) {
            infoFlowPosition.innerHTML = `
                <strong>${lang === 'fa' ? 'موقعیت در جریان' : 'Flow Position'}</strong>
                <span>${data.flowPosition[lang] || data.flowPosition.en}</span>
            `;
            infoFlowPosition.style.display = 'block';
        } else if (infoFlowPosition) {
            infoFlowPosition.style.display = 'none';
        }

        // Relationships
        if (infoRelationships && data.relationships) {
            const relationships = data.relationships[lang] || data.relationships.en;
            if (relationships && relationships.length > 0) {
                const relationshipsList = document.createElement('ul');
                relationships.forEach(rel => {
                    const li = document.createElement('li');
                    li.textContent = rel;
                    relationshipsList.appendChild(li);
                });
                infoRelationships.innerHTML = `
                    <strong>${lang === 'fa' ? 'مرتبط با' : 'Related To'}</strong>
                `;
                infoRelationships.appendChild(relationshipsList);
                infoRelationships.style.display = 'block';
            } else {
                infoRelationships.style.display = 'none';
            }
        }

        // Code example
        if (infoCodeExample && data.codeExample) {
            const code = data.codeExample[lang] || data.codeExample.en;
            infoCodeExample.innerHTML = `
                <strong>${lang === 'fa' ? 'مثال کد' : 'Code Example'}</strong>
                <pre><code>${escapeHtml(code)}</code></pre>
            `;
            infoCodeExample.style.display = 'block';
        } else if (infoCodeExample) {
            infoCodeExample.style.display = 'none';
        }

        // Features list
        if (infoFeatures && data.features) {
            const features = data.features[lang] || data.features.en;
            const featuresList = document.createElement('ul');
            features.forEach(feature => {
                const li = document.createElement('li');
                li.textContent = feature;
                featuresList.appendChild(li);
            });
            infoFeatures.innerHTML = '';
            infoFeatures.appendChild(featuresList);
        }

        // Show info panel
        infoPanel.classList.add('active');

        // Highlight clicked component
        clearComponentHighlights();
        if (componentElement) {
            componentElement.classList.add('component-active');
        }

        // Scroll to info panel on mobile
        if (window.innerWidth <= 768) {
            setTimeout(() => {
                infoPanel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }, 300);
        }
    }

    // Function to highlight related components
    function highlightRelatedComponents(componentType) {
        const data = componentData[componentType];
        if (!data || !data.relationships) return;

        components.forEach(comp => {
            const compType = comp.dataset.component;
            if (compType === componentType) {
                comp.classList.add('component-active');
            } else if (data.relationships.en.some(rel => 
                compType === rel.toLowerCase().replace(/\s+/g, '-') ||
                getComponentNameMapping(rel) === compType
            )) {
                comp.classList.add('component-connected');
            }
        });
    }

    // Function to clear highlights
    function clearComponentHighlights() {
        components.forEach(comp => {
            comp.classList.remove('component-active', 'component-connected', 'active');
        });
    }

    // Helper function to map relationship names to component types
    function getComponentNameMapping(name) {
        const mapping = {
            'URL Routing': 'url',
            'Middleware': 'middleware',
            'Views': 'views',
            'Models': 'models',
            'Templates': 'templates',
            'Context': 'context',
            'HTTP Request': 'http-request',
            'HTTP Response': 'http-response'
        };
        return mapping[name] || name.toLowerCase().replace(/\s+/g, '-');
    }

    // Helper function to escape HTML
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // Make showComponentInfo available globally for step navigation
    window.showComponentInfo = showComponentInfo;
}

// Initialize Flow Controls
function initFlowControls() {
    const playPauseBtn = document.getElementById('play-pause-btn');
    const prevStepBtn = document.getElementById('prev-step-btn');
    const nextStepBtn = document.getElementById('next-step-btn');
    const resetBtn = document.getElementById('reset-btn');
    const stepCurrent = document.getElementById('step-current');
    const stepTotal = document.getElementById('step-total');
    const stepProgress = document.getElementById('step-progress');

    if (stepTotal) stepTotal.textContent = flowState.totalSteps;

    // Play/Pause button
    if (playPauseBtn) {
        playPauseBtn.addEventListener('click', function() {
            if (flowState.isPlaying) {
                stopFlowAnimation();
            } else {
                startFlowAnimation();
            }
        });
    }

    // Previous step button
    if (prevStepBtn) {
        prevStepBtn.addEventListener('click', function() {
            stepBackward();
        });
    }

    // Next step button
    if (nextStepBtn) {
        nextStepBtn.addEventListener('click', function() {
            stepForward();
        });
    }

    // Reset button
    if (resetBtn) {
        resetBtn.addEventListener('click', function() {
            resetFlow();
        });
    }

    // Update step display
    function updateStepDisplay() {
        if (stepCurrent) stepCurrent.textContent = flowState.currentStep;
        if (stepProgress) {
            const percentage = (flowState.currentStep / flowState.totalSteps) * 100;
            stepProgress.style.setProperty('--progress-width', percentage + '%');
            stepProgress.setAttribute('data-progress', percentage);
            // Also update the ::after pseudo-element via a class or style
            const style = document.createElement('style');
            style.id = 'step-progress-style';
            const existingStyle = document.getElementById('step-progress-style');
            if (existingStyle) existingStyle.remove();
            style.textContent = `.step-progress::after { width: ${percentage}% !important; }`;
            document.head.appendChild(style);
        }
    }

    // Start flow animation
    function startFlowAnimation() {
        if (flowState.currentStep >= flowState.totalSteps) {
            resetFlow();
        }
        flowState.isPlaying = true;
        if (playPauseBtn) {
            const icon = playPauseBtn.querySelector('i');
            const span = playPauseBtn.querySelector('span');
            if (icon) icon.className = 'fas fa-pause';
            if (span) span.textContent = document.documentElement.lang === 'fa' ? 'توقف' : 'Pause';
        }
        
        flowState.animationInterval = setInterval(() => {
            if (flowState.currentStep < flowState.totalSteps) {
                stepForward();
            } else {
                stopFlowAnimation();
            }
        }, flowState.stepDuration);
    }

    // Stop flow animation
    function stopFlowAnimation() {
        flowState.isPlaying = false;
        if (flowState.animationInterval) {
            clearInterval(flowState.animationInterval);
            flowState.animationInterval = null;
        }
        if (playPauseBtn) {
            const icon = playPauseBtn.querySelector('i');
            const span = playPauseBtn.querySelector('span');
            if (icon) icon.className = 'fas fa-play';
            if (span) span.textContent = document.documentElement.lang === 'fa' ? 'اجرای جریان' : 'Play Flow';
        }
    }

    // Step forward
    function stepForward() {
        if (flowState.currentStep < flowState.totalSteps) {
            flowState.currentStep++;
            updateStepDisplay();
            goToStep(flowState.currentStep);
        }
    }

    // Step backward
    function stepBackward() {
        if (flowState.currentStep > 0) {
            flowState.currentStep--;
            updateStepDisplay();
            goToStep(flowState.currentStep);
        }
    }

    // Reset flow
    function resetFlow() {
        stopFlowAnimation();
        flowState.currentStep = 0;
        updateStepDisplay();
        clearAllHighlights();
        const infoPanel = document.getElementById('component-info');
        if (infoPanel) infoPanel.classList.remove('active');
    }

    // Go to specific step
    function goToStep(step) {
        const stepComponents = [
            'http-request', 'url', 'middleware', 'views', 
            'models', 'templates', 'context', 'http-response'
        ];
        
        if (step > 0 && step <= stepComponents.length) {
            const componentType = stepComponents[step - 1];
            const component = document.querySelector(`[data-component="${componentType}"]`);
            if (component && window.showComponentInfo) {
                // Highlight all components up to this step
                clearAllHighlights();
                for (let i = 0; i < step; i++) {
                    const compType = stepComponents[i];
                    const comp = document.querySelector(`[data-component="${compType}"]`);
                    if (comp) {
                        comp.classList.add('active');
                        if (i === step - 1) {
                            comp.classList.add('component-active');
                        }
                    }
                }
                window.showComponentInfo(componentType, component);
            }
        } else if (step === 0) {
            clearAllHighlights();
        }
    }

    // Clear all highlights
    function clearAllHighlights() {
        const components = document.querySelectorAll('.flow-component');
        components.forEach(comp => {
            comp.classList.remove('active', 'component-active', 'component-connected');
        });
    }

    // Initialize step display
    updateStepDisplay();

    // Make functions available globally
    window.startFlowAnimation = startFlowAnimation;
    window.stopFlowAnimation = stopFlowAnimation;
    window.stepForward = stepForward;
    window.stepBackward = stepBackward;
    window.resetFlow = resetFlow;
}

// Smooth scrolling for anchor links
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#' || href === '#!') return;

            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const offsetTop = target.offsetTop - 80; // Account for navbar
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Scroll animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe elements for animation
    const animateElements = document.querySelectorAll(
        '.highlight-card, .feature-card, .benefit-item, .step-card, .flow-component'
    );

    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}

// Parallax effect for hero section (optional enhancement)
function initParallaxEffect() {
    const heroSection = document.querySelector('.hero-section');
    if (!heroSection) return;

    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const heroContent = heroSection.querySelector('.hero-content');
        
        if (heroContent && scrolled < window.innerHeight) {
            const parallaxSpeed = 0.5;
            heroContent.style.transform = `translateY(${scrolled * parallaxSpeed}px)`;
        }
    });
}

// Optional: Initialize parallax if desired
// initParallaxEffect();

// Update navbar on scroll (only if old navbar exists, React navbar handles its own styling)
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
    if (window.scrollY > 50) {
        navbar.style.boxShadow = 'var(--shadow-md)';
    } else {
        navbar.style.boxShadow = 'none';
        }
    }
});
