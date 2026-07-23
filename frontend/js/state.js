import BADSA from "./badsa.js";

const STATES = {

    IDLE: "Idle",

    LISTENING: "Listening",

    THINKING: "Thinking",

    SPEAKING: "Speaking"

};



export function changeState(state){

    BADSA.setState(state);

    BADSA.addLog(`State → ${state}`);

}



export {STATES};