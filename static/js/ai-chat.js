// #region agent log
fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'ai-chat.js:1',message:'ai-chat.js loaded',data:{},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'D'})}).catch((e)=>{console.error('Log failed:',e);});
// #endregion

// AI Chat Widget
let chatHistory = [];
let currentLessonId = null;

// Initialize chat
document.addEventListener('DOMContentLoaded', function () {
    // Check if we are on a lesson page or general page
    if (typeof CURRENT_LESSON_ID !== 'undefined') {
        currentLessonId = CURRENT_LESSON_ID;
    }

    // Auto-focus input if chat is opened
    const chatToggle = document.getElementById('chat-toggle-btn');
    if (chatToggle) {
        chatToggle.addEventListener('click', () => {
            const container = document.getElementById('chat-container');
            if (container && container.classList.contains('active')) {
                setTimeout(() => {
                    const input = document.getElementById('chat-input');
                    if (input) input.focus();
                }, 300); // Wait for transition
            }
        });
    }
});

function toggleChat() {
    const chatContainer = document.getElementById('chat-container');
    const toggleBtn = document.getElementById('chat-toggle-btn');
    if (chatContainer && toggleBtn) {
        const isActive = chatContainer.classList.toggle('active');
        toggleBtn.setAttribute('aria-expanded', isActive);
        chatContainer.setAttribute('aria-hidden', !isActive);

        if (isActive) {
            toggleBtn.querySelector('i').className = 'fas fa-times';
        } else {
            toggleBtn.querySelector('i').className = 'fas fa-robot';
        }
    }
}

function handleChatKeyPress(event) {
    if (event.key === 'Enter') {
        sendChatMessage();
    }
}

async function sendChatMessage() {
    // #region agent log
    fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'ai-chat.js:49',message:'sendChatMessage called',data:{},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'D'})}).catch(()=>{});
    // #endregion
    const input = document.getElementById('chat-input');
    const messagesContainer = document.getElementById('chat-messages');

    if (!input || !messagesContainer) return;

    const question = input.value.trim();
    // #region agent log
    fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'ai-chat.js:58',message:'Message input',data:{question:question,hasInput:!!input,hasMessagesContainer:!!messagesContainer},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'D'})}).catch(()=>{});
    // #endregion
    if (!question) return;

    // Clear input
    input.value = '';

    // Add user message to UI
    addChatMessage('user', question);

    // Add to history
    chatHistory.push({ role: 'user', content: question });

    // Show loading indicator
    const loadingId = addChatMessage('assistant', 'Thinking...', true);

    try {
        // #region agent log
        fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'ai-chat.js:75',message:'Before fetch',data:{currentLessonId:currentLessonId,historyLength:chatHistory.length},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'D'})}).catch(()=>{});
        // #endregion
        // Send to backend
        const response = await fetch('/ai/chat/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                question: question,
                lesson_id: currentLessonId, // Will be null if general context
                history: chatHistory.slice(-5) // Last 5 messages for context
            })
        });

        const data = await response.json();
        // #region agent log
        fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'ai-chat.js:88',message:'Response received',data:{status:response.status,success:data.success,hasError:!!data.error},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'D'})}).catch(()=>{});
        // #endregion

        // Remove loading message
        const loadingMsg = document.getElementById(`msg-${loadingId}`);
        if (loadingMsg) {
            loadingMsg.remove();
        }

        if (data.success) {
            // Add assistant response
            addChatMessage('assistant', data.response);
            chatHistory.push({ role: 'assistant', content: data.response });
        } else {
            const errorMsg = data.error || 'I apologize, but I encountered an issue processing your request.';
            addChatMessage('assistant', `⚠️ ${errorMsg}`);
        }
    } catch (error) {
        // #region agent log
        fetch('http://127.0.0.1:7244/ingest/2ab6b6a7-b9bb-4b98-afcb-765703b2028c',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({location:'ai-chat.js:113',message:'Chat error caught',data:{errorMessage:error.message,errorName:error.name},timestamp:Date.now(),sessionId:'debug-session',runId:'run1',hypothesisId:'D'})}).catch(()=>{});
        // #endregion
        // Remove loading message
        const loadingMsg = document.getElementById(`msg-${loadingId}`);
        if (loadingMsg) {
            loadingMsg.remove();
        }

        addChatMessage('assistant', 'Sorry, I seems to be having connection trouble. Please check your internet or try again later.');
    }

    // Scroll to bottom
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function addChatMessage(role, content, isLoading = false) {
    const messagesContainer = document.getElementById('chat-messages');
    if (!messagesContainer) return;

    const messageId = Date.now();
    const messageDiv = document.createElement('div');
    messageDiv.id = `msg-${messageId}`;
    messageDiv.className = `chat-message ${role}${isLoading ? ' typing' : ''}`;
    messageDiv.setAttribute('role', role === 'user' ? 'user-message' : 'assistant-message');

    if (isLoading) {
        messageDiv.innerHTML = `<i class="fas fa-circle-notch fa-spin" aria-hidden="true"></i> <span>${content}</span>`;
        messageDiv.setAttribute('aria-live', 'polite');
    } else {
        // Simple Markdown-like parsing for code blocks and bold text
        let formattedContent = content
            .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>') // Code blocks
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>') // Bold
            .replace(/\n/g, '<br>'); // Line breaks

        messageDiv.innerHTML = formattedContent;
    }

    messagesContainer.appendChild(messageDiv);

    // Smooth scroll to bottom
    setTimeout(() => {
        messagesContainer.scrollTo({
            top: messagesContainer.scrollHeight,
            behavior: 'smooth'
        });
    }, 100);

    return messageId;
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

