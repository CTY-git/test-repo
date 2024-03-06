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
  document.getElementById("image").innerText = data;
}
