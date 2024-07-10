// import mkcert from "vite-plugin-mkcert";

// vite.config.js
export default {
  // plugins: [mkcert()],
  root: "./src/",
  publicDir: "../public/",
  build: {
    outDir: "../dist/",
    assetsDir: "static/",
    emptyOutDir: true,
    reportCompressedSize: true,
  },
  server: {
    https: false,
    port: 3000,
    host: true,
    open: true,
  },
};
