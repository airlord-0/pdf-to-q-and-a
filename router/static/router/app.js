const chatBox = document.getElementById("chat-box");
const uploadForm = document.getElementById("upload-form");
const questionForm = document.getElementById("question-form");
const questionInput = document.getElementById("question-input");


function addMessage(text, type) {
    const message = document.createElement("div");

    message.classList.add("message");
    message.classList.add(type + "-message");

    const paragraph = document.createElement("p");
    paragraph.textContent = text;

    message.appendChild(paragraph);
    chatBox.appendChild(message);

    chatBox.scrollTop = chatBox.scrollHeight;
}


// PDF UPLOAD
uploadForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(uploadForm);

    addMessage("Uploading your PDF...", "bot");

    try {
        const response = await fetch(uploadForm.action, {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        const data = await response.json();

        addMessage(data.message, "bot");

    } catch (error) {
        console.error("Upload error:", error);
        addMessage("Something went wrong while uploading the PDF.", "bot");
    }
});


// QUESTION
questionForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const question = questionInput.value.trim();

    if (!question) {
        return;
    }

    // Create FormData BEFORE clearing the input
    const formData = new FormData(questionForm);

    addMessage(question, "user");

    questionInput.value = "";

    try {
        const response = await fetch(questionForm.action, {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        const data = await response.json();

        addMessage(data.answer, "bot");

    } catch (error) {
        console.error("Question error:", error);
        addMessage("Something went wrong while processing your question.", "bot");
    }
});