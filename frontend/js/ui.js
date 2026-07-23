const conversation = document.getElementById("conversation");
const logs = document.getElementById("logs");
const state = document.getElementById("agent-state");
const orb = document.getElementById("orb");

/* ==========================
        Conversation
========================== */

export function addUserMessage(message){

    conversation.insertAdjacentHTML(
        "beforeend",
        `
        <div class="message user">
            <div class="sender">👤 You</div>
            ${message}
        </div>
        `
    );

    scrollConversation();

}

export function addAssistantMessage(message){

    conversation.insertAdjacentHTML(
        "beforeend",
        `
        <div class="message assistant">
            <div class="sender">🤖 BADSA</div>
            ${message}
        </div>
        `
    );

    scrollConversation();

}

/* ==========================
            Logs
========================== */

export function addLog(message){

    const time = new Date().toLocaleTimeString();

    logs.insertAdjacentHTML(
        "beforeend",
        `<p>[${time}] ${message}</p>`
    );

    logs.scrollTop = logs.scrollHeight;

}

/* ==========================
            State
========================== */

export function setState(newState){

    state.textContent = newState;

}

/* ==========================
            Orb
========================== */

const STATES = [
    "orb-idle",
    "orb-listening",
    "orb-thinking",
    "orb-speaking"
];

export function updateOrb(newState){

    orb.classList.remove(...STATES);

    switch(newState){

        case "Idle":

            orb.classList.add("orb-idle");
            break;

        case "Listening":

            orb.classList.add("orb-listening");
            break;

        case "Thinking":

            orb.classList.add("orb-thinking");
            break;

        case "Speaking":

            orb.classList.add("orb-speaking");
            break;

        default:

            orb.classList.add("orb-idle");

    }

}

/* ==========================
        Helpers
========================== */

function scrollConversation(){

    conversation.scrollTop = conversation.scrollHeight;

}