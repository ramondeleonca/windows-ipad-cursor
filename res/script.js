const cursor = document.querySelector("div[data-cursor]")

window.addEventListener("hashchange", () => {
    const cursorString = window.location.hash.replace(/^#/, "");
    cursor.setAttribute("data-cursor", cursorString);
});