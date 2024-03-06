function addingEventListenerToPingButton() {
  document.getElementById("pingBtn").addEventListener("click", function () {
    let url = getUrlForVulnerabilityLevel();
    doGetAjaxCall(
      pingUtilityCallback,
      url + "?ipaddress=" + encodeURIComponent(document.getElementById("ipaddress").value),
      true
    );
  });
}
addingEventListenerToPingButton();

function pingUtilityCallback(data) {
  document.getElementById("pingUtilityResponse").textContent = data.content;
}
