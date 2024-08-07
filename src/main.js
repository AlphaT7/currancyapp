import { initBackend } from "absurd-sql/dist/indexeddb-main-thread";

const log = console.log.bind(console);
const $ = document.querySelector.bind(document);
const abs = Math.abs.bind(Math);
const USDollar = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
});

// ["USD", "EUR", "JPY", "GBP", "CNH", "AUD", "CAD", "CHF", "HKD", "NZD"]

let installApp;
let showList = false;
let apiData;

window.addEventListener("beforeinstallprompt", (e) => {
  e.preventDefault();
  installApp = e;
  $("#installApp").addEventListener("pointerdown", () => {
    installApp.prompt();
  });
});

async function init() {
  let worker = await new Worker(new URL("./index.worker.js", import.meta.url), {
    type: "module",
  });
  initBackend(worker);
  // setTimeout(() => {
  // worker.postMessage("/prices/month1/");
  // }, 1000);
  worker.postMessage("run");
}

function getCrypto(cryptoObj) {
  let cryptoTable = `<table><caption>Historical Data</caption><thead><td>Ticker</td><td>Close Price</td><td>Time</td></thead><tbody id="cryptoTable"></tbody></table>`;

  let cryptoHTML = `<tr>{img}</tr>
                    <tr>{ticker}</tr>
                    <tr>{closePrice}</tr>
                    <tr>{time}</tr>`;

  let transactionArr = cryptoObj.results;

  for (transaction in transactionArr) {
    let html = cryptoHTML;
    html = html.replace(
      "{img}",
      `<img src='${
        "./static/crypto/" + crypto.symbol.toLowerCase() + ".png"
      }'/>`
    );

    html = html.replace("{ticker}", cryptoObj.ticker);

    html = html.replace("{price}", `$${USDollar.format(+transaction.c)}`);

    html = html.replace("time", new Date(+transaction.t));
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

    $("#c1").innerHTML += temp;

    i++;
  }
}

async function fillCurrencySelection(filteredList) {
  let currencyList = $("#currencyList");
  currencyList.innerHTML = "";

  let option = `<div data-currency="[currency]" class="optionContainer">
      <div data-currency="[currency]" class="flag-option fflag-[country] fflag ff-wave ff-app"></div>
      <div data-currency="[currency]" class="optionCurrency">[currency]</div>
  </div>`;

  for await (currency of filteredList) {
    let newOption = option;
    let country = currency.slice(0, 2);
    let currencyPattern = "[currency]";
    let countryPattern = "[country]";

    newOption = newOption.replaceAll(countryPattern, country);
    newOption = newOption.replaceAll(currencyPattern, currency);

    currencyList.innerHTML += newOption;
  }

  document.querySelectorAll(".optionContainer").forEach((el) => {
    el.addEventListener("pointerdown", setCurrencyBase);
  });
}

function showDropDown() {
  showList = !showList;
  if (showList) {
    $("#listContainer").style.display = "grid";
    $("#dropIndicator").innerHTML = "arrow_drop_up";
    setTimeout(() => {
      $("#listContainer").classList.toggle("changeOpacity");
      $("#findCurrency").focus();
    }, 50);
  } else {
    $("#listContainer").classList.toggle("changeOpacity");
    $("#dropIndicator").innerHTML = "arrow_drop_down";
    setTimeout(() => {
      $("#listContainer").style.display = "none";
    }, 300);
  }
}

async function filterCurrencyList() {
  let conditions = new RegExp(/^[A-Za-z]{0,3}$/, "gi");
  let userInput = $("#findCurrency").value;
  if (!conditions.test(userInput))
    $("#findCurrency").value = userInput.slice(0, userInput.length - 1);

  let filter = new RegExp("^" + $("#findCurrency").value, "gi");
  let currencyList = Object.entries(apiData[1].rates).map((arr) => arr[0]);

  let filteredList = currencyList.filter((currency) => {
    filter.lastIndex = 0; // necessary to reset the ".test()" to start at index 0 of userInput regular expression;
    if (filter.test(currency)) return currency;
  });

  await fillCurrencySelection(filteredList);
}

function setCurrencyBase(e) {
  let selection = e.target.dataset.currency;

  $("#currencyId").innerText = selection;
  $("#selectedCurrancyFlag").removeAttribute("class");
  $("#selectedCurrancyFlag").className = `flag-option fflag-${selection.slice(
    0,
    2
  )} fflag ff-wave ff-app`;
}

document.addEventListener("DOMContentLoaded", () => {
  $("#currencySelection").addEventListener("pointerup", showDropDown);

  $("#findCurrency").addEventListener("input", filterCurrencyList);

  $("#findCurrency").addEventListener("blur", showDropDown);

  init();
});
