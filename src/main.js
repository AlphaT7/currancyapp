const log = console.log.bind(console);
const $ = document.querySelector.bind(document);
const abs = Math.abs.bind(Math);
const USDollar = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
});

let pointerDown;
let isPointerUp = true;
let installApp;

window.addEventListener("beforeinstallprompt", (e) => {
  e.preventDefault();
  installApp = e;
  $("#installApp").addEventListener("pointerdown", () => {
    if (installApp.prompt()) {
      log(true);
    }
  });
});

function pointerUp() {
  isPointerUp = true;
}

function trackPointer(e) {
  if (pointerDown == undefined) return;
  let motionDifference = {
    x: abs(abs(e.x) - pointerDown.x),
    y: abs(abs(e.y) - pointerDown.y),
  };

  let motionDirection = {
    x: pointerDown.x > e.x ? "right" : "left",
    y: pointerDown.y > e.y ? "down" : "up",
  };

  let fx = $("#displaySwitch").checked;
  let dirRight = motionDirection.x == "right" ? true : false;
  let movement = motionDifference.x > 8 ? true : false;

  if (
    (fx && dirRight && movement && !isPointerUp) ||
    (!fx && !dirRight && movement && !isPointerUp)
  ) {
    $("#displaySwitch").checked = !$("#displaySwitch").checked;
    switchCurrency();
  }
}

function setPointer(e) {
  pointerDown = { x: e.x, y: e.y };
  isPointerUp = false;
}

function switchCurrency() {
  $("#fx").classList.toggle("switchCurrency");
  $("#switchCenter").classList.toggle("switchBGColor");
}

async function init() {
  let response = await fetch("./temp.json");
  let mainArr = await response.json();
  let cryptoArr = mainArr[0];
  let fxObj = mainArr[1].rates;

  getCrypto(cryptoArr);
  getFX(fxObj);

  if ("serviceWorker" in navigator) {
    navigator.serviceWorker
      .register("/sw.js")
      .then((registration) => {
        console.log("SW registered: ", registration);
      })
      .catch((registrationError) => {
        console.log("SW registration failed: ", registrationError);
      });
  }
}

function getCrypto(cryptoArr) {
  let cryptoHTML = `<div class="cryptoContainer">
    <div class="cryptoIcon"> {icon} </div>
    <div class="cryptoName"> {name} </div>
    <div class="cryptoPrice"> {price} </div>
  </div>`;

  for (let i = 0; i < 10; i++) {
    let crypto = cryptoArr[i];

    let temp = cryptoHTML;
    temp = temp.replace(
      "{icon}",
      `<img src='${"./crypto/" + crypto.symbol.toLowerCase() + ".png"}'/>`
    );

    temp = temp.replace("{name}", crypto.name);

    temp = temp.replace("{price}", `$${USDollar.format(+crypto.priceUsd)}`);

    $("#crypto").innerHTML += temp;
  }
}

function getFX(fxObj) {
  let fxHTML = `<div class="fxContainer">
    <div class="fxIcon"> {flag} </div>
    <div class="fxCountry"> {name} </div>
    <div class="fxPrice"> {price} </div>
  </div>`;

  let i = 0;

  for (const fx in fxObj) {
    if (!(i < 10)) return;

    let temp = fxHTML;
    temp = temp.replace(
      "{flag}",
      `<div style="width: 42px; height: 32px;" class='${
        "fflag-" + fx.slice(0, 2)
      } fflag ff-wave ff-app'></div>`
    );

    temp = temp.replace("{name}", fx);

    temp = temp.replace("{price}", `$${USDollar.format(fxObj[fx])}`);

    $("#fx").innerHTML += temp;

    i++;
  }
}

$("#displaySwitch").addEventListener("pointerup", switchCurrency);

document.addEventListener("pointerdown", setPointer);

document.addEventListener("pointermove", trackPointer);

document.addEventListener("pointerup", pointerUp);

init();
