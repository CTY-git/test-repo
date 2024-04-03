function addingEventListenerToLoadImageButton() {
  document.getElementById("loadImage").addEventListener("click", function () {
    let url = getUrlForVulnerabilityLevel();
    doGetAjaxCall(
      appendResponseCallback,
      url + "?value=images/" + encodeURIComponent(document.getElementById("images").value),
      false
    );
  });
}
addingEventListenerToLoadImageButton();

function appendResponseCallback(data) {
  let div = document.getElementById("image");
  div.textContent = ''; // Clear the div
  let sanitizedData = document.createTextNode(data); // Create a text node which automatically escapes HTML
  div.appendChild(sanitizedData); // Append the text node to the div
}
