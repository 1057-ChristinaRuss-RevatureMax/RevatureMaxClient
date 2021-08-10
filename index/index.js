async function invalid() {
    let url = 'http://18.209.14.19:9001/invalid'
    let response = await fetch(url)
    let element = document.getElementById("invalid")
    if (await response.json() == "invalid"){
        element.innerHTML += "Incorrect Login. Try Again."
    }
}

window.onload = function () {
    this.invalid()
}