const orb = document.getElementById("orb");

let rotation = 0;

let currentState = "Idle";

function animate(){

    rotation += 0.2;

    switch(currentState){

        case "Listening":

            rotation += 0.35;
            break;

        case "Thinking":

            rotation += 1.5;
            break;

        case "Speaking":

            rotation += 0.8;
            break;

    }

    const outer = orb.querySelector(".outer-ring");
    const segment = orb.querySelector(".segment-ring");
    const inner = orb.querySelector(".inner-ring");

    outer.style.transform =
        `rotate(${rotation}deg)`;

    segment.style.transform =
        `rotate(${-rotation*1.8}deg)`;

    inner.style.transform =
        `rotate(${rotation*3}deg)`;

    requestAnimationFrame(animate);

}

requestAnimationFrame(animate);

export function setOrbState(state){

    currentState = state;

}