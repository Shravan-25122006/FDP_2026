const text = "Full Stack Developer | UI/UX Enthusiast";
let index = 0;

function typingEffect() {
    if (index < text.length) {
        document.getElementById("role").innerHTML += text.charAt(index);
        index++;
        setTimeout(typingEffect, 100);
    }
}

typingEffect();
