function addingEventListenerToLoadImageButton() {
  document.getElementById("loadImage").addEventListener("click", function () {
    let url = getUrlForVulnerabilityLevel();
    doGetAjaxCall(
      appendResponseCallback,
      url +
        "?src=/VulnerableApp/images/" +
        document.getElementById("images").value,
      false
    );
  });
}
addingEventListenerToLoadImageButton();

function appendResponseCallback(data) {
  // Assuming data is intended to be plain text and not HTML
  document.getElementById("image").textContent = data;
}
