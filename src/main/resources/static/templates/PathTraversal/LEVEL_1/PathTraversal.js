function addingEventListenerToLoadImageButton() {
  document.getElementById("loadButton").addEventListener("click", function () {
    let url = getUrlForVulnerabilityLevel();
    doGetAjaxCall(
      appendResponseCallback,
      url + "?fileName=" + encodeURIComponent(document.getElementById("fileName").value),
      true
    );
  });
}
addingEventListenerToLoadImageButton();

function appendResponseCallback(data) {
  if (data.isValid) {
    let tableInformation = '<table id="InfoTable">';
    let content = JSON.parse(data.content);
    if (content.length > 0) {
      for (let key in content[0]) {
        tableInformation +=
          '<th id="InfoColumn">' + escapeHTML(key) + "</th>";
      }
    }
    for (let index in content) {
      tableInformation += '<tr id="Info">';
      for (let key in content[index]) {
        tableInformation +=
          '<td id="InfoColumn">' +
          escapeHTML(content[index][key]) +
          "</td>";
      }
      tableInformation += "</tr>";
    }
    tableInformation += "</table>";
    document.getElementById("Information").textContent = ''; // Clear the element
    document.getElementById("Information").insertAdjacentHTML('beforeend', tableInformation);
  } else {
    document.getElementById("Information").textContent = "Unable to Load Users";
  }
}

function escapeHTML(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
