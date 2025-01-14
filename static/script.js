const promptInput = document.getElementById('prompt');
const sendBtn = document.getElementById('send-btn');
const chatMessages = document.querySelector('.chat-messages');

sendBtn.addEventListener('click', async () => {
    const prompt = promptInput.value;

    if (prompt.trim() === '') {
        return;
    }

    const userMessage = document.createElement('div');
    userMessage.classList.add('user-message');
    userMessage.textContent = prompt;
    chatMessages.appendChild(userMessage);

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                prompt: prompt
            })
        });

        const data = await response.json();

        if (response.ok) {
            const aiMessage = document.createElement('div');
            aiMessage.classList.add('ai-message');
            aiMessage.textContent = data.response;
            chatMessages.appendChild(aiMessage);
        } else {
            alert('Error: ' + data.error);
        }

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again later.');
    }

    promptInput.value = '';
    chatMessages.scrollTop = chatMessages.scrollHeight;
});