// import mkcert from "vite-plugin-mkcert";

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
    cors: false,
    headers: {
      "Cross-Origin-Opener-Policy": "same-origin",
      "Cross-Origin-Embedder-Policy": "require-corp",
    },
    fs: {
      strict: false,
    },
    https: false,
    port: 3000,
    host: true,
    // open: true,
  },
};
