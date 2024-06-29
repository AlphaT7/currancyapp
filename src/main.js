const log = console.log.bind(console);
const $ = document.querySelector.bind(document);

function switchCurrency() {
  $("#fx").classList.toggle("switchCurrency");
}

async function getCrypto() {
  let response = await fetch("./temp.json");
  let cryptoArr = (await response.json())[0];

  let cryptoHTML = `<div class="cryptoContainer">
    <div class="cryptoIcon"> {icon} </div>
    <div class="cryptoName"> {name} </div>
    <div class="cryptoPrice"> {price} </div>
  </div>`;

  //["BTC", "ETH", "USDT", "BNB", "SOL", "USDC", "XRP", "DOGE", "ADA", "TRX"]

  for (let i = 0; i < 10; i++) {
    let crypto = cryptoArr[i];

    let temp = cryptoHTML;
    temp = temp.replace(
      "{icon}",
      `<img src='${"./crypto/" + crypto.symbol.toLowerCase() + ".png"}'/>`
    );

    temp = temp.replace("{name}", crypto.name);

    temp = temp.replace("{price}", (+crypto.priceUsd).toFixed(3));

    $("#crypto").innerHTML += temp;
    log(crypto.symbol);
  }
}

getCrypto();

$("#displaySwitch").addEventListener("pointerup", switchCurrency);
