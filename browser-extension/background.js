console.log("bakground.js loaded");

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

chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.text in iconPaths) {
    fetchSvg(chrome.runtime.getURL(iconPaths[msg.text]), sendResponse);
    return true; // keeps the message channel open until sendResponse is called
  } else if (msg.text === "fetchProductInfo") {
    fetchProductInfo(sendResponse);
    return true; // keeps the message channel open until sendResponse is called
  } else {
    console.error(`Unknown message text: ${msg.text}`);
    sendResponse({ error: `Unknown message text: ${msg.text}` });
  }
});
