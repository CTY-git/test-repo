function addingEventListenerToLoadImageButton() {
  document.getElementById("submit").addEventListener("click", function () {
    let url = getUrlForVulnerabilityLevel();
    doGetAjaxCall(
      appendResponseCallback,
      url + "?value=" + encodeURIComponent(document.getElementById("textInput").value),
      false
    );
  });
}
addingEventListenerToLoadImageButton();

function appendResponseCallback(data) {
  var parentContainer = document.getElementById("parentContainer");
  // Assuming data is supposed to contain HTML, we need to sanitize it before setting innerHTML
  parentContainer.innerHTML = sanitizeHTML(data);
  if (parentContainer.childNodes.length > 0) {
    parentContainer.childNodes[0].classList.add(
      sanitizeCSSClass(document.getElementById("fonts").value)
    );
  }
}

function sanitizeHTML(html) {
  var tempDiv = document.createElement('div');
  tempDiv.textContent = html;
  return tempDiv.innerHTML;
}

function sanitizeCSSClass(cssClass) {
  return cssClass.replace(/[^a-zA-Z0-9-_]/g, "");
}
