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

function createElementWithType(type, percent = null) {
  // Create header and content divs
  let headerWrapper = document.createElement("div");
  let headerDiv = document.createElement("div");
  let contentDiv = document.createElement("div");

  // Set IDs and classes based on type
  headerDiv.id = `${type}-header`;
  headerWrapper.id = `${type}-header-wrapper`;
  contentDiv.id = `${type}-content`;
  headerDiv.classList.add("header");
  headerWrapper.classList.add("header-wrapper");
  contentDiv.classList.add("content");

  // Use the capitalize function for the header text
  headerDiv.innerText = capitalize(type);
  headerWrapper.appendChild(headerDiv);

  if (percent) {
    let percentDiv = document.createElement("div");
    percentDiv.id = `${type}-percent`;
    percentDiv.classList.add("percent");
    percentDiv.innerText = `${percent.value}%`;
    percentDiv.style.color = percent.color;
    headerWrapper.appendChild(percentDiv);
  }

  // Prevent text selection
  headerWrapper.style.userSelect = "none";

  // Add click event listener to toggle content visibility
  headerWrapper.addEventListener("click", function () {
    contentDiv.classList.toggle("hidden");
    this.classList.toggle("rounded-bottom");
    contentDiv.classList.toggle("expanded");
  });

  // Append to mainBody or a specified parent element
  mainBody.appendChild(headerWrapper); // Adjust as needed
  mainBody.appendChild(contentDiv); // Adjust as needed

  // Send a message to fetch content based on type
  chrome.runtime.sendMessage(
    { text: "fetchContentFor", type: type },
    (response) => {
      if (chrome.runtime.lastError) {
        console.error("Error:", chrome.runtime.lastError.message);
        // Optionally handle the error, e.g., show a default message
        contentDiv.textContent = "Content not available";
      } else if (response && response.content) {
        // Set the contentDiv textContent with the received content
        contentDiv.textContent = response.content;
      } else {
        console.error(`${capitalize(type)} content not received`);
        // Optionally handle the absence of content
        contentDiv.textContent = "Content not available";
      }
    }
  );
}

createElementWithType("summary");
createElementWithType("positive", { value: 40, color: "green" });
createElementWithType("negative", { value: 60, color: "red" });
createElementWithType("authenticity");

// Create and append the first <hr>
let hr1 = document.createElement("hr");
// hr1.style.marginTop = "20px"; // Adjust the value as needed
// hr1.style.marginBottom = "20px"; // Adjust the value as needed
mainBody.appendChild(hr1);

// Function to create an element, set its content, and append it to the parent
function createElement(tagName, parent, className, innerText) {
  let element = document.createElement(tagName);
  if (className) {
    element.className = className;
  }
  if (innerText) {
    element.innerText = innerText;
  }
  parent.appendChild(element);
  return element;
}

// Create article analysis section and append it
let articleAnalysis = createElement("div", mainBody, "article-analysis");
mainBody.appendChild(articleAnalysis);

// Create and append the second <hr>
let hr2 = document.createElement("hr");
mainBody.appendChild(hr2);

// Create media analysis section and append it
let mediaAnalysis = createElement("div", mainBody, "media-analysis");
mainBody.appendChild(mediaAnalysis);

// Create analysis elements for article analysis
createElement("div", articleAnalysis, "analysis-ele", "Published By: ");
createElement("div", articleAnalysis, "analysis-ele", "Published Date: ");
createElement("div", articleAnalysis, "analysis-ele", "Written By: ");
createElement("div", articleAnalysis, "analysis-ele", "Last Edited: ");

// Create analysis elements for media analysis
createElement("div", mediaAnalysis, "analysis-ele", "Language: ");
createElement("div", mediaAnalysis, "analysis-ele", "Reading Time: ");
createElement("div", mediaAnalysis, "analysis-ele", "Links: ");
createElement("div", mediaAnalysis, "analysis-ele", "Videos: ");

let gemini = document.createElement("div");
gemini.id = "gemini";
gemini.textContent = "Powered by Gemini";
mainBody.appendChild(gemini);
