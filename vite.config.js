// export default {
//   root: "./src/",
//   publicDir: "../.venv/static",
//   build: {
//     outDir: "../.venv/templates/",
//     emptyOutDir: true,
//     reportCompressedSize: true,
//   },
//   server: {
//     https: false,
//     port: 3000,
//     host: true,
//     open: true,
//   },
// };

// import mkcert from "vite-plugin-mkcert";

// vite.config.js
export default {
  // plugins: [mkcert()],
  root: "./src/",
  publicDir: "../public/",
  build: {
    outDir: "../dist/",
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
