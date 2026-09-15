const chatBox = document.getElementById("chat-box");
const uploadForm = document.getElementById("upload-form");
const questionForm= document.getElementById("question-form");
const questionInput = document.getElementById("question-input");

function addMessage(text, type) {

    const message = document.createElement("div");    // create an empty div element of html 
 
    message.classList.add("message"); // where message is a css class defined in html
    message.classList.add(type + "-message");

    const paragraph = document.createElement("p"); // js creates <p></p>
    paragraph.textContent=text;

    message.appendChild(paragraph);  // put the paragraph inside div of message

    chatBox.appendChild(message); // first we created a div, appended div with paragraph now append this div in the actual chatbox

    chatBox.scrollTop = chatBox.scrollHeight // automatically scroll to the end of the chat

}

uploadForm.addEventListener("submit", async function(event){    // when the question form is submitted, run this function
    console.log("UPLOAD SUBMIT FIRED");
    
    event.preventDefault(); // when submitted a browser may refresh or follow default instructions, this code prevents it from happening 

    event.preventDefault();
    const formData = new FormData(uploadForm); // get the data from the html uploadForm

    addMessage("uploading your PDF ...", "bot");

    const response = await fetch(uploadForm.action, {   // fetch sends http request to a given url 
        method: "POST",
        body : formData // send the data to django 
        // after sending the request to django await keeps the page unfreezed untill django response 
    })
    const data = await response.json(); 

    addMessage(data.message,"bot");

});

// now lets work on the user question aim to send this question to django response 

questionForm.addEventListener("submit", async function (event) {
    event.preventDefault(); 

    const question = questionInput.value.trim(); 
    if (!question) {
        return;
    }

    addMessage(question, "user");
    questionInput.value = "";
    const formData = new FormData(questionForm);

    const response = await fetch (questionForm.action,{
        method: "POST",
        body : formData
    });
    const data = await response.json();

    addMessage(data.answer,"bot");

});
