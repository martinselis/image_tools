link = document.getElementsByName("link")[0]
if (url_info) {
    console.log(url_info)
}

var resizeButton = document.getElementById("resizeButton")
resizeButton.firstElementChild.addEventListener("click", function(e) {
    let url = document.getElementsByName("urlname")[0].value
    let width = document.getElementsByName("width")[0].value
    let height = document.getElementsByName("height")[0].value

    if (width == "" || height == "" || url == "") {
        e.preventDefault()
        alert("Don't leave empty fields")
    }
})
