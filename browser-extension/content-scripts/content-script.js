console.log("content-script.js loaded");

/**
 * Creates and appends an SVG element to a specified parent element.
 * @param {string} svgString - The SVG string to be parsed and appended.
 * @param {string} parentId - The ID of the parent element to which the SVG will be appended.
 * @param {string} id - The ID to be assigned to the new SVG element.
 * @param {string|null} fill - Optional fill color for the SVG.
 * @param {function|null} clickHandler - Optional click handler for the SVG.
 * @returns {Element} The appended SVG element.
 */
function createAndAppendSvg(
  svgString,
  parentId,
  id,
  fill = null,
  clickHandler = null
) {
  let parentElement = document.getElementById(parentId);
  let parser = new DOMParser();
  let svgElement = parser.parseFromString(
    svgString,
    "image/svg+xml"
  ).documentElement;
  svgElement.id = id;

  if (fill) {
    for (let child of svgElement.children) {
      child.setAttribute("fill", fill);
    }
  }
  let iconDiv = document.createElement("div");
  iconDiv.id = "icon-div";
  iconDiv.appendChild(svgElement);
  parentElement.appendChild(iconDiv);

  if (clickHandler) {
    svgElement.addEventListener("click", clickHandler);
  }

  return svgElement;
}

/**
 * Requests and appends an icon SVG to a specified parent element.
 * @param {string} iconName - The name of the icon to be fetched.
 * @param {string} parentId - The ID of the parent element to which the icon will be appended.
 * @param {string} id - The ID to be assigned to the new SVG element.
 * @param {function|null} callback - Optional click handler for the SVG.
 * @returns {Promise} A promise that resolves when the icon is appended.
 */
function getAndAppendIcon(iconName, parentId, id, callback) {
  return new Promise((resolve, reject) => {
    chrome.runtime.sendMessage(
      { text: `fetchIcon${capitalize(iconName)}` },
      (response) => {
        if (chrome.runtime.lastError) {
          console.error("Error:", chrome.runtime.lastError.message);
          reject(chrome.runtime.lastError);
        } else if (response && response.svg) {
          let element = createAndAppendSvg(
            response.svg,
            parentId,
            id,
            null,
            callback
          );
          element.style.height = "16px";
          element.style.cursor = "pointer";
          element.classList.add("icon-svg");
          resolve();
        } else {
          console.error(`${capitalize(iconName)} Icon not received`);
          reject(new Error(`${iconName} Icon not received`));
        }
      }
    );
  });
}

/**
 * Capitalizes the first letter of a string.
 * @param {string} str - The string to be capitalized.
 * @returns {string} The capitalized string.
 */
function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

let mainBtn = document.createElement("div");
mainBtn.id = "main-btn";
document.body.appendChild(mainBtn);
mainBtn.addEventListener("click", () => {
  if (contentDiv.style.display === "none" || contentDiv.style.display === "") {
    contentDiv.style.display = "flex";
  } else {
    contentDiv.style.display = "none";
  }
});

let contentDiv = document.createElement("div");
contentDiv.id = "content-div";
contentDiv.style.display = "none";
document.body.appendChild(contentDiv);

// Navbar setup
let nav = document.createElement("div");
nav.id = "nav";
contentDiv.appendChild(nav);

(async () => {
  let functionIconDiv = document.createElement("div");
  functionIconDiv.id = "function-icon-div";
  nav.appendChild(functionIconDiv);

  await getAndAppendIcon("info", "function-icon-div", "info-svg");
  await getAndAppendIcon("flag", "function-icon-div", "flag-svg");
  await getAndAppendIcon("share", "function-icon-div", "share-svg");
  await getAndAppendIcon("close", "function-icon-div", "close-svg", () => {
    contentDiv.style.display = "none";
  });
})();

// main body div
let mainBody = document.createElement("div");
mainBody.id = "main-body";
contentDiv.appendChild(mainBody);

// Summary Div
let summaryHeader = document.createElement("div");
summaryHeader.id = "summary-header";
summaryHeader.innerText = "Summary";
summaryHeader.classList.add("header");
summaryHeader.style.userSelect = "none";
// Modify in content-script.js
summaryHeader.addEventListener("click", function () {
  // Toggle the 'hidden' class on summaryDiv
  summaryDiv.classList.toggle("hidden");
  // Toggle a class that adds/removes the border-radius
  this.classList.toggle("rounded-bottom");
  // Toggle the 'expanded' class to trigger the transition
  summaryDiv.classList.toggle("expanded");
});
mainBody.appendChild(summaryHeader);

let summaryDiv = document.createElement("div");
summaryDiv.id = "summary-div";
mainBody.appendChild(summaryDiv);
summaryDiv.classList.add("content");
summaryDiv.textContent = "Summary of the product";
