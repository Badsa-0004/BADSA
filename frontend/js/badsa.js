import {
    addUserMessage,
    addAssistantMessage,
    addLog,
    setState,
    updateOrb
} from "./ui.js";

import { setOrbState } from "./orb.js";


const connectionStatus = document.getElementById("connection-status");

const statusDot = document.querySelector(".status-dot");



const BADSA = {

    addUserMessage(message) {

        addUserMessage(message);

    },



    addAssistantMessage(message) {

        addAssistantMessage(message);

    },



    addLog(message) {

        addLog(message);

    },



    setState(state) {

        setState(state);
        updateOrb(state);
        setOrbState(state);

    },


    setConnection(connected) {

        if (connected) {

            connectionStatus.textContent = "Connected";

            statusDot.style.background = "#00ff88";
            statusDot.style.boxShadow = "0 0 12px #00ff88";

        }

        else {

            connectionStatus.textContent = "Disconnected";

            statusDot.style.background = "#ff3b30";
            statusDot.style.boxShadow = "0 0 12px #ff3b30";

        }

    }

};



export default BADSA;