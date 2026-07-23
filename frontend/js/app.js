import BADSA from "./badsa.js";

import {
    STATES,
    changeState
} from "./state.js";

function startup(){

    BADSA.setConnection(false);

    changeState(STATES.IDLE);

    BADSA.addLog("BADSA GUI Started");

    BADSA.addLog("Initializing Orb Engine...");

    BADSA.addLog("Waiting for Backend...");

    BADSA.addAssistantMessage(
        "BADSA Online. Waiting for connection..."
    );

}

function demo(){

    const sequence = [
        STATES.LISTENING,
        STATES.THINKING,
        STATES.SPEAKING,
        STATES.IDLE
    ];

    let index = 0;

    setInterval(()=>{

        changeState(sequence[index]);

        index++;

        if(index >= sequence.length){

            index = 0;

        }

    },3000);

}

window.addEventListener("DOMContentLoaded",()=>{

    startup();

    demo();

});