async function fetchUser() {
    try {
        const response = await fetch('/user');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const html = await response.text();
        const elements = document.getElementsByClassName('bot_resp_text');
                if (elements.length > 0) {
                    elements[0].innerHTML = html;
                }
            } 
        catch (error) {
               console.error('There was a problem with the fetch operation:', error);
    }
}
