if(!self.define){let e,r={};const c=(c,i)=>(c=new URL(c+".js",i).href,r[c]||new Promise((r=>{if("document"in self){const e=document.createElement("script");e.src=c,e.onload=r,document.head.appendChild(e)}else e=c,importScripts(c),r()})).then((()=>{let e=r[c];if(!e)throw new Error(`Module ${c} didn’t register its module`);return e})));self.define=(i,n)=>{const a=e||("document"in self?document.currentScript.src:"")||location.href;if(r[a])return;let o={};const d=e=>c(e,a),f={module:{uri:a},exports:o,require:d};r[a]=Promise.all(i.map((e=>f[e]||d(e)))).then((e=>(n(...e),o)))}}define(["./workbox-39235b66"],(function(e){"use strict";self.skipWaiting(),e.clientsClaim(),e.precacheAndRoute([{url:"android-chrome-192x192.png",revision:"d756453bae0aa5c975ace0b76a1422ab"},{url:"android-chrome-512x512.png",revision:"ee50f532fda4dcedab4f2c006c12ec5c"},{url:"apple-touch-icon.png",revision:"284a0a654b210502835216b7273c0460"},{url:"assets/index-Bvz1BG2i.css",revision:"fc8d4ac993d2f6b27aa108f9f9ba930e"},{url:"crypto/ada.png",revision:"631e3a53c50a07487a53969e129dbfb9"},{url:"crypto/bnb.png",revision:"36816cb725de241085084d19ddad084b"},{url:"crypto/btc.png",revision:"1d3a2e659c5ef46515109e284be090ac"},{url:"crypto/doge.png",revision:"14ab14f94d02575de3dcd2e399a23f6e"},{url:"crypto/eth.png",revision:"aca9541a9056e44f69a68595e5188033"},{url:"crypto/sol.png",revision:"dd714b016fe61b2448a4bc1d53f249fa"},{url:"crypto/trx.png",revision:"0535d4860f5cb2379c9044061eb453ef"},{url:"crypto/usdc.png",revision:"fa2b292ef1a3422613c3ddb32fc6eb7f"},{url:"crypto/usdt.png",revision:"a43e4090491da28ca584344f7beb95ba"},{url:"crypto/xrp.png",revision:"e04f61113822c3a4f97c63e89d37ea9d"},{url:"favicon-16x16.png",revision:"22544cf2afbab0b1c6bbfdd187ad40d8"},{url:"favicon-32x32.png",revision:"236bf6862b7696cb9bf01ce653b3b3e4"},{url:"favicon.ico",revision:"9b2afd5866e8527b736bdae524e09afb"},{url:"fx/flagSprite42.png",revision:"9376f9ca54eaf6a513ef109ea48c68ee"},{url:"fx/flagSprite60.png",revision:"11513569cf5fe23d81882b5a575c2efa"},{url:"fx/freakflags.css",revision:"6d449049c515d9bcfed8546fe6bc19ac"},{url:"index.html",revision:"afa1d05f9843d027216bb10626d14198"}],{}),e.registerRoute(/.*/,new e.NetworkFirst({cacheName:"app-name-cache",networkTimeoutSeconds:4,plugins:[new e.ExpirationPlugin({maxEntries:20,maxAgeSeconds:5})]}),"GET")}));
//# sourceMappingURL=sw.js.map