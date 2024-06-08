console.log("background.js loaded");

function fetchSvg(url, sendResponse) {
  fetch(url)
    .then((response) => response.text())
    .then((data) => {
      sendResponse({ svg: data });
    })
    .catch((error) => {
      console.error("Error fetching SVG:", error);
      sendResponse({ error: error.toString() });
    });
}

const iconPaths = {
  fetchIconShare: "icons/share.svg",
  fetchIconInfo: "icons/info.svg",
  fetchIconFlag: "icons/flag.svg",
  fetchIconClose: "icons/close.svg",
};

// Change these when backend is connected
const types = {
  summary: "Summary",
  positive: "Positive",
  negative: "Negative",
  authenticity: "Authenticity",
};

// Placeholder for fetchProductInfo function
function fetchContentInfo(sendResponse, type) {
  // Simulated asynchronous operation
  setTimeout(() => {
    if (type in types) {
      sendResponse({ content: types[type] });
    } else {
      sendResponse({ error: "Invalid type" });
    }
  }, 1000);
}

chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.text in iconPaths) {
    fetchSvg(chrome.runtime.getURL(iconPaths[msg.text]), sendResponse);
    return true; // keeps the message channel open until sendResponse is called
  } else if (msg.text === "fetchContentFor") {
    // Ensure msg.type is valid before proceeding
    if (msg.type in types) {
      fetchContentInfo(sendResponse, msg.type);
    } else {
      console.error("Invalid or missing type for fetchProductInfo");
      sendResponse({ error: "Invalid or missing type" });
    }
    return true; // keeps the message channel open until sendResponse is called
  } else {
    console.error(`Unknown message text: ${msg.text}`);
    sendResponse({ error: `Unknown message text: ${msg.text}` });
  }
});
